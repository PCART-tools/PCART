# -*- coding: utf-8 -*-
import numpy as np
import random
# import os
# import torch
# import math
# import matplotlib
# import matplotlib.pyplot as plt
import functions.synthetic as synthetic
from copy import deepcopy
import argparse
import scipy
from scipy import optimize
import time
import re


# python run.py --func=Ackley --dim=100 --method=AIBO_mixed-grad-UCB1.96 --iters=5000 --device=cpu
# python run.py --func=Ackley --dim=100 --method=AIBO_random-grad-UCB1.96 --iters=5000 --device=cpu



parser = argparse.ArgumentParser()
parser.add_argument('--func', help='specify the test function')#, choices=func_choice
parser.add_argument('--dim', type=int, help='specify the problem dimensions')
parser.add_argument('--method',default='AIBO_mixed-grad-EI')#, choices=method
parser.add_argument('--batch-size', type=int, default=10)
parser.add_argument('--iters', type=int, help='Total evaluation budget')
parser.add_argument('--istrackAF', type=bool, default=False)
parser.add_argument('--istrackcands', type=bool, default=False)
parser.add_argument('--device', default='cpu')
parser.add_argument('--dtype', default='float64')
parser.add_argument('--verbose',type=bool, default=False)
parser.add_argument('--popsize',type=int, default=50)

args = parser.parse_args()


if args.func in ['Ackley', 'Levy', 'Rastrigin', 'Rosenbrock', 'Griewank']:
    f_class = eval(f'synthetic.{args.func}')
    f = f_class(dim =args.dim, foldername=f'{args.method}-{args.batch_size}', verbose=args.verbose)
    fname = f'{args.func}{args.dim}'+'/'+f'{args.method}-{args.batch_size}'

elif args.func == 'Robotpush': 
    import functions.robot_push as robot_push
    f = robot_push.PushReward(method=f'{args.method}-{args.batch_size}', verbose=args.verbose)
    fname = 'RobotPush14'+'/'+f'{args.method}-{args.batch_size}'
elif args.func == 'Rover': 
    import functions.rover as rover
    f = rover.Rover(method=f'{args.method}-{args.batch_size}', verbose=args.verbose)
    fname = 'Rover60'+'/'+f'{args.method}-{args.batch_size}'
elif args.func == 'HalfCheetah': 
    import functions.mujoco as mujoco
    f = mujoco.HalfCheetah(method=f'{args.method}-{args.batch_size}', verbose=args.verbose)
    fname = 'HalfCheetah102'+'/'+f'{args.method}-{args.batch_size}'

    
# elif args.func == 'synt_hard': 
#     import functions.lasso as lasso
#     f = lasso.LassoBenchFunction(method=args.method, noise=False)
# elif args.func == 'synt_hard_noise': 
#     import functions.lasso as lasso
#     f = lasso.LassoBenchFunction(method=args.method, noise=True)
else:
    raise Exception('function not defined')


if args.method.startswith('AIBO'): # 'AIBO_mixed-es-UCB1.96'
    from AIBO.AIBO import AIBO
    
    _, initialization_mode, acqf_maxmizer, acqf_mode = re.split('_|-', args.method)
    if initialization_mode == 'mixed':
        acqf_initializer={"random":{},"cmaes":{'sigma0':0.2},"ga":{'pop_size':args.popsize}}
    elif initialization_mode == 'ga':
        acqf_initializer={"ga":{'pop_size':args.popsize}}
    elif initialization_mode == 'cmaes':
        acqf_initializer={"cmaes":{'sigma0':0.2}}
    elif initialization_mode == 'random':
        acqf_initializer={"random":{}}
    else:
        assert 1==0, 'select a correct initialization_mode'
    if acqf_mode.startswith('UCB'):
        beta = float(acqf_mode[3:])
        acqf_mode = 'UCB'
    else:
        beta = None

    t0=time.time()
    AIBO = AIBO(
        f=f,  # Handle to objective function
        fname=fname,
        lb=f.lb,  # Numpy array specifying lower bounds
        ub=f.ub,  # Numpy array specifying upper bounds
        n_init=50,
        max_evals = args.iters,  # Maximum number of evaluations
        batch_size = args.batch_size,
        n_init_acq=500,
        max_acq_size=256,
        n_restarts_acq=1,
        acqf_mode = acqf_mode,
        beta=beta,
        initial_guess = None,
        acqf_maxmizer = acqf_maxmizer,
        acqf_initializer = acqf_initializer, #"global":{}, "cmaes":{},"ga":{},"topN":{}
        # optimizers={"global":{},"topN":{},"cmaes":{},"multi_size_local":{'length':[ 0.5**1, 0.5**2, 0.5**3, 0.5**4]}},#"multi_size_local":{'length':[ 0.5**3, 0.5**4, 0.5**5, 0.5**6]}
        minimize=True,
        verbose=True,  # Print information from each batch
        use_ard=True,  # Set to true if you want to use ARD for the GP kernel
        max_cholesky_size=2000,  # changed,2000
        n_training_steps=50,  # Number of steps of ADAM to learn the hypers
        min_cuda=1024,  # Run on the CPU for small datasets
        device=args.device,  # "cpu" or "cuda"
        dtype=args.dtype,  # float64 or float32
        istrackcands = args.istrackcands,
        istrackAF = args.istrackAF,
    )
    AIBO.optimize()
    print('cost time:',time.time()-t0)
    print('='*20)



elif args.method == 'cmaes':
    x0 = np.random.rand(f.dim)
    sigma0=0.2
    import cma
    t0=time.time()
    es = cma.CMAEvolutionStrategy(
        x0 = x0,#np.random.rand(f.dim),
        sigma0=sigma0,
        inopts={'bounds': [0, 1], "popsize": args.batch_size}
    )#, 'maxfevals':5000, 'tolx':1e-4
    
    # es1 = cma.CMAEvolutionStrategy(
    #     x0 = 0.5*np.ones(f.dim), # np.random.rand(f.dim), 0.5*np.ones(f.dim)
    #     sigma0=0.001,
    #     inopts={'bounds': [0, 1], "popsize": args.batch_size}
    # )
    # xs1 = es1.ask()
    
    num=0
    n_evals=0
    
    # while not es.stop():
    while n_evals< args.iters and not es.stop(): #
        xs = es.ask()
        y=[f(np.array(f.lb)+(np.array(f.ub)-np.array(f.lb))*x) for x in xs]
        es.tell(xs, y)
        num += len(xs)
        n_evals += len(xs)
        # print(np.round(xs[0],3))
        if num>100:
            # print(np.round(xs[0],3))
            print(es.sigma)
            print('{}) {} fbest={}'.format(n_evals, args.func, es.best.f))
            num=0
    print('best y:',es.best.f)
    print('best x:',es.best.x)
    print('cost time:',time.time()-t0)
    





    
elif args.method == 'turbo':
    from baselines.TuRBO.turbo_1 import Turbo1
    t0=time.time()
    turbo1 = Turbo1(
        f=f,  # Handle to objective function
        lb=f.lb,  # Numpy array specifying lower bounds
        ub=f.ub,  # Numpy array specifying upper bounds
        n_init=2*args.batch_size,  # Number of initial bounds from an Latin hypercube design
        max_evals = args.iters,  # Maximum number of evaluations
        batch_size=args.batch_size,  # How large batch size TuRBO uses
        verbose=True,  # Print information from each batch
        use_ard=True,  # Set to true if you want to use ARD for the GP kernel
        max_cholesky_size=2000,  # When we switch from Cholesky to Lanczos
        n_training_steps=50,  # Number of steps of ADAM to learn the hypers
        min_cuda=1024,  # Run on the CPU for small datasets
        device=args.device,  # "cpu" or "cuda"
        dtype=args.dtype,  # float64 or float32
    )
    turbo1.optimize()
    print('cost time:',time.time()-t0)
    X = turbo1.X  # Evaluated points
    fX = turbo1.fX  # Observed values
    ind_best = np.argmin(fX)
    f_best, x_best = fX[ind_best], X[ind_best, :]
    print('best x:',x_best)
    print('best y:',f_best)
   

elif args.method == 'ga':
    from pymoo.algorithms.soo.nonconvex.ga import GA
    from pymoo.core.problem import Problem
    from pymoo.core.evaluator import Evaluator
    from pymoo.core.termination import NoTermination
    from pymoo.core.population import Population
    t0=time.time()
    problem = Problem(n_var=f.dim, n_obj=1, n_constr=0, xl=np.zeros(f.dim), xu=np.ones(f.dim))
    termination = NoTermination()
    pop_size=50
    n_offsprings=args.batch_size
    algorithm = GA(pop_size=pop_size,n_offsprings=n_offsprings)
    algorithm.setup(problem, termination=termination)
    num=0
    n_evals=0
    while n_evals< args.iters:
        pop = algorithm.ask()
        # pop1=deepcopy(pop)
        # if n_evals==0:
        #     for _ in range(1):
        #         xs=np.random.rand(pop_size,f.dim)
        #         pop1.set("X", xs)
        #         y=[f(np.array(f.lb)+(np.array(f.ub)-np.array(f.lb))*x) for x in xs]
        #         pop1.set("F", np.array(y).reshape(-1,1))
        #         pop=Population.merge(pop, pop1)

        # else:
        #     pop=pop[np.random.choice(n_offsprings, args.batch_size,replace=False)]
        xs = pop.get("X")
        y=[f(np.array(f.lb)+(np.array(f.ub)-np.array(f.lb))*x) for x in xs]
        pop.set("F", np.array(y).reshape(-1,1))
        # set_cv(pop)
        algorithm.tell(infills=pop)
        n_evals+=len(xs)
        num += len(xs)
        if num>100:
            print('{}) {} fbest={}'.format(n_evals, args.func, algorithm.result().F[0]))
            num=0
    res = algorithm.result()
    print('best y:',res.F[0])
    print('cost time:',time.time()-t0)

    
elif args.method == 'random':
    import nevergrad as ng
    init=f.lb+np.random.rand()*(f.ub-f.lb)
    init=0.5*(f.lb+f.ub)
    param = ng.p.Array(init=init).set_bounds(lower=f.lb, upper=f.ub)
    ran = ng.optimizers.RandomSearch(parametrization=param, budget = args.iters, num_workers=args.batch_size)
    recommendation = ran.minimize(f)











elif args.method == 'anneal':   
    bounds = []
    for idx in range(0, len(f.lb) ):
        bounds.append( ( float(f.lb[idx]), float(f.ub[idx])) )
    res = scipy.optimize.dual_annealing(f, 
                                        bounds=bounds, 
                                        maxfun=args.iters,
                                        local_search_options={'method':'L-BFGS-B','options':{'maxfun': args.iters}}
                                        )
    print('best y:',res.fun)
    
elif args.method == 'de':
    import nevergrad as ng
    init=f.lb+np.random.rand()*(f.ub-f.lb)
    init=0.5*(f.lb+f.ub)
    param = ng.p.Array(init=init).set_bounds(lower=f.lb, upper=f.ub)
    de = ng.optimizers.DE(parametrization=param, budget = args.iters, num_workers=args.batch_size)
    recommendation = de.minimize(f)

elif args.method == 'ngopt':
    import nevergrad as ng
    init=0.5*(f.lb+f.ub)
    param = ng.p.Array(init=init).set_bounds(lower=f.lb, upper=f.ub)
    ngo = ng.optimizers.NGOpt(parametrization=param, budget = args.iters, num_workers=args.batch_size)
    recommendation = ngo.minimize(f)
    x=recommendation.value
    print('best y:',f(x))
    
elif args.method == 'cgde':
    import nevergrad as ng
    param = ng.p.Array(init=0.5*(f.lb+f.ub)).set_bounds(lower=f.lb, upper=f.ub)
    de = ng.optimizers.GeneticDE(parametrization=param, budget = args.iters, num_workers=args.batch_size)
    recommendation = de.minimize(f)
    x=recommendation.value
    print('best y:',f(x))
    

        
elif args.method == 'lbfgsb':   
    bounds = []
    for idx in range(0, len(f.lb) ):
        bounds.append( ( float(f.lb[idx]), float(f.ub[idx])) )
    res = scipy.optimize.minimize(f, 
                            x0 = np.array(f.lb) + (np.array(f.ub)-      np.array(f.lb))*np.random.rand(f.dim), 
                            method='L-BFGS-B', 
                            bounds=bounds, 
                            options={'maxfun': args.iters, 'maxiter': 15000, 'iprint': - 1, 'maxls': 20}
                            )
    
elif args.method == 'bobyqa': 
    import pybobyqa
    x0=np.array(f.lb) + (np.array(f.ub)-np.array(f.lb))*np.random.rand(f.dim)
    soln=pybobyqa.solve(f, x0, bounds=(f.lb,f.ub), maxfun=args.iters)
    print('best y:',soln.f)

elif args.method == 'lamcts':
    from LAMCTS.lamcts import MCTS
    t0=time.time()
    if args.func =="Ant":
        Cp=10
        leaf_size=100
        kernel_type='linear'
    else:
        Cp=1
        

elif args.method == 'opentuner':
    from baselines.OpenTuner.tuner import OpenTuner
    args.f=f
    OpenTuner.main(args)
else:
    print("no such method")
    
# X = AIBO.X  # Evaluated points
# fX = AIBO.fX  # Observed values
# ind_best = np.argmin(fX)
# f_best, x_best = fX[ind_best], X[ind_best, :]

# print("Best value found:\n\tf(x) = %.3f\nObserved at:\n\tx = %s" % (f_best, np.around(x_best, 3)))

#fig = plt.figure(figsize=(7, 5))
#matplotlib.rcParams.update({'font.size': 16})
#plt.plot(fX, 'b.', ms=10)  # Plot all evaluated points as blue dots
#plt.plot(np.minimum.accumulate(fX), 'r', lw=3)  # Plot cumulative minimum as a red line
#plt.xlim([0, len(fX)])
#plt.ylim([0, 30])
#plt.title("20D Levy function")
#
#plt.tight_layout()
#plt.show()


