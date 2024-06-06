
import numpy as np
import json
import os
import time
from datetime import datetime


class tracker:
    def __init__(self, foldername, verbose=False, filename='result'):
        self.counter   = 0
        self.results   = []
        self.curt_best = float("inf")
        self.curt_best_x = None
        self.foldername = foldername
        self.filename = filename
        self.verbose=verbose
        os.makedirs('result/'+foldername, exist_ok=True)

    def dump_trace(self):
        trace_path = 'result/'+self.foldername + '/' + self.filename + str(len(self.results))+'.json'
        final_results_str = json.dumps(self.results)
        with open(trace_path, "a") as f:
            f.write(final_results_str + '\n')
            
    def track(self, result, x = None):
        if result < self.curt_best:
            self.curt_best = result
            self.curt_best_x = x
        if self.verbose and self.counter%10==0:
            print("")
            print("="*10)
            print("iteration:", self.counter, "total samples:", len(self.results) )
            print("="*10)
            print("current best f(x):", self.curt_best)
            print("current best x:", np.around(self.curt_best_x, decimals=2))
        self.results.append(self.curt_best)
        self.counter += 1
        if len(self.results) % 200 == 0:
            self.dump_trace()
            
class dict_tracker:
    def __init__(self, foldername, verbose=False, filename='cands'):
        self.counter   = 0
        self.curt_best = float("inf")
        self.curt_best_x = None
        self.foldername = foldername
        self.filename = filename
        self.verbose = verbose
        os.makedirs('result/'+foldername, exist_ok=True)
        current_datetime = datetime.now()
        ustr = current_datetime.strftime("%Y%m%d_%H%M%S")
        self.trace_path = 'result/'+self.foldername + '/' + self.filename + ustr +'.json'

    
    def track(self, result_dict, x = None):
        results_str = json.dumps(result_dict)
        with open(self.trace_path, "a") as f:
            f.write(results_str + '\n')
        
            
        
class Levy:
    def __init__(self, dim=1, foldername='', verbose=False):
        self.dim    = dim
        self.lb      = -10 * np.ones(dim)
        self.ub      =  10 * np.ones(dim)
        self.counter = 0
        print("####dim:", dim)
        self.tracker = tracker('Levy'+str(dim)+'/'+foldername, verbose=verbose)

    def __call__(self, x):
        x = np.array(x)
        self.counter += 1
        assert len(x) == self.dim
        assert x.ndim == 1
        assert np.all(x <= self.ub) and np.all(x >= self.lb)
        w = []
        for idx in range(0, len(x)):
            w.append( 1 + (x[idx] - 1) / 4 )
        w = np.array(w)
        
        term1 = ( np.sin( np.pi*w[0] ) )**2;
        
        term3 = ( w[-1] - 1 )**2 * ( 1 + ( np.sin( 2 * np.pi * w[-1] ) )**2 );
        
        
        term2 = 0;
        for idx in range(1, len(w) ):
            wi  = w[idx]
            new = (wi-1)**2 * ( 1 + 10 * ( np.sin( np.pi* wi + 1 ) )**2)
            term2 = term2 + new
        
        result = term1 + term2 + term3

        self.tracker.track( result, x )

        return result
    
        
class Ackley:
    def __init__(self, dim=3, foldername='', verbose=False):
        self.dim    = dim
        self.lb      = -5 * np.ones(dim) # -5
        self.ub      = 10 * np.ones(dim) # -10
        self.counter = 0
        self.tracker = tracker('Ackley'+str(dim) + '/'+foldername, verbose=verbose)

    def __call__(self, x):
        x = np.array(x)
        self.counter += 1
        assert len(x) == self.dim
        assert x.ndim == 1
        # assert np.all(x <= self.ub) and np.all(x >= self.lb)
        result = (-20*np.exp(-0.2 * np.sqrt(np.inner(x,x) / x.size )) - np.exp(np.cos(2*np.pi*x).sum() /x.size) + 20 + np.e)
        self.tracker.track( result, x )
        return result

class Rastrigin:
    def __init__(self, dim=3, foldername='', verbose=False):
        self.dim    = dim
        self.lb      = -5.12 * np.ones(dim)
        self.ub      = 5.12 * np.ones(dim)
        self.counter = 0
        self.tracker = tracker('Rastrigin'+str(dim)+ '/'+foldername, verbose=verbose)
        

    def __call__(self, x):
        x = np.array(x)
        self.counter += 1
        assert len(x) == self.dim
        assert x.ndim == 1
        # assert np.all(x <= self.ub) and np.all(x >= self.lb)
        w = 1 + (x - 1.0) / 4.0
        result = 10*self.dim + np.sum(x**2-10*np.cos(2*np.pi*x))
        self.tracker.track( result, x )
        return result

class Rosenbrock :
    def __init__(self, dim=3, foldername='', verbose=False):
        self.dim    = dim
        self.lb      = -5 * np.ones(dim)
        self.ub      = 10 * np.ones(dim)
        self.counter = 0
        self.tracker = tracker('Rosenbrock'+str(dim)+ '/'+foldername, verbose=verbose)
        

    def __call__(self, x):
        x = np.array(x)
        self.counter += 1
        assert len(x) == self.dim
        assert x.ndim == 1
        # assert np.all(x <= self.ub) and np.all(x >= self.lb)
        result=0
        for i in range(self.dim-1):
            result += 100*(x[i+1]-x[i]**2)**2+(x[i]-1)**2
        self.tracker.track( result, x )
        # result=np.log10(result)
        return result


class Griewank:
    def __init__(self, dim=3, foldername='', verbose=False):
        self.dim    = dim
        self.lb      = -600 * np.ones(dim)
        self.ub      = 600 * np.ones(dim)
        self.counter = 0
        self.tracker = tracker('Griewank'+str(dim)+ '/'+foldername,verbose=verbose)
        

    def __call__(self, x):
        x = np.array(x)
        self.counter += 1
        assert len(x) == self.dim
        assert x.ndim == 1
        # assert np.all(x <= self.ub) and np.all(x >= self.lb)
        result = np.sum(x**2/4000)-np.prod(np.cos(x/np.sqrt(1+np.arange(self.dim))))+1
        self.tracker.track( result, x )
        return result

class Schwefel:
    def __init__(self, dim=20, foldername='', verbose=False):
        self.dim    = dim
        self.lb      = -500 * np.ones(dim)
        self.ub      = 500 * np.ones(dim)
        self.counter = 0
        self.tracker = tracker('Schwefel'+str(dim)+ '/'+foldername,verbose=verbose)
        

    def __call__(self, x):
        x = np.array(x)
        self.counter += 1
        assert len(x) == self.dim
        assert x.ndim == 1
        # assert np.all(x <= self.ub) and np.all(x >= self.lb)
        result = 418.9829*self.dim - np.sum(x*np.sin(np.sqrt(np.abs(x))))
        self.tracker.track( result, x )
        return result


class Ackley_parallel:
    def __init__(self, dim=3, method='', verbose=False):
        self.dim    = dim
        self.lb      = -5 * np.ones(dim)
        self.ub      = 10 * np.ones(dim)
        self.counter = 0

    def __call__(self, x):
        x = np.array(x)
        result = -20*np.exp(-0.2 * np.sqrt(np.mean(x*x,1))) - np.exp(np.mean(np.cos(2*np.pi*x),1)) + 20 + np.e
        return result


class Rastrigin_parallel:
    def __init__(self, dim=3, foldername='', verbose=False):
        self.dim    = dim
        self.lb      = -5.12 * np.ones(dim)
        self.ub      = 5.12 * np.ones(dim)
        self.counter = 0
        

    def __call__(self, x):
        x = np.array(x)
        self.counter += 1
        assert x.shape[-1] == self.dim
        # assert np.all(x <= self.ub) and np.all(x >= self.lb)
        w = 1 + (x - 1.0) / 4.0
        result = 10*self.dim + np.sum(x**2-10*np.cos(2*np.pi*x), axis=1)
        return result
    
class Rosenbrock_parallel:
    def __init__(self, dim=3, foldername='', verbose=False):
        self.dim    = dim
        self.lb      = -5 * np.ones(dim)
        self.ub      = 10 * np.ones(dim)
        self.counter = 0
        

    def __call__(self, x):
        x = np.array(x)
        self.counter += 1
        assert x.shape[-1] == self.dim
        result=np.zeros(len(x))
        for i in range(self.dim-1):
            result += 100*(x[:,i+1]-x[:,i]**2)**2+(x[:,i]-1)**2
        return result


class Griewank_parallel:
    def __init__(self, dim=3, foldername='', verbose=False):
        self.dim    = dim
        self.lb      = -600 * np.ones(dim)
        self.ub      = 600 * np.ones(dim)
        self.counter = 0
        

    def __call__(self, x):
        x = np.array(x)
        self.counter += 1
        assert x.shape[-1] == self.dim
        result = np.sum(x**2/4000, axis=1)-np.prod(np.cos(x/np.sqrt(1+np.arange(self.dim))), axis=1)+1
        return result