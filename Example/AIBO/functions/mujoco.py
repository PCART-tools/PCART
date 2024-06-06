
import numpy as np
import gym
import time
from .synthetic import tracker
import subprocess

class Hopper:
    
    def __init__(self, method='', verbose=False):
        self.mean    = np.array([1.41599384, -0.05478602, -0.25522216, -0.25404721, 
                                 0.27525085, 2.60889529,  -0.0085352, 0.0068375, 
                                 -0.07123674, -0.05044839, -0.45569644])
        self.std     = np.array([0.19805723, 0.07824488,  0.17120271, 0.32000514, 
                                 0.62401884, 0.82814161,  1.51915814, 1.17378372, 
                                 1.87761249, 3.63482761, 5.7164752 ])
        self.dim    = 33
        self.lb      = -1 * np.ones(self.dim)
        self.ub      =  1 * np.ones(self.dim)
        self.counter = 0
        self.env     = gym.make('Hopper-v2')
        self.num_rollouts = 10
        self.render  = False
        self.policy_shape = (3, 11)
        self.tracker     = tracker('Hopper'+ '/'+method, verbose=verbose)
        
        
        # print("===========initialization===========")
        # print("mean:", self.mean)
        # print("std:", self.std)
        # print("dim:", self.dim)
        # print("policy:", self.policy_shape )
            
    def __call__(self, x):
        self.counter += 1
        assert len(x) == self.dim
        assert x.ndim == 1
        assert np.all(x <= self.ub) and np.all(x >= self.lb), "x={}".format(x)
        
        M = x.reshape(self.policy_shape)
        
        returns = []
        observations = []
        actions = []
        
        for i in range(self.num_rollouts):
            obs    = self.env.reset()
            done   = False
            totalr = 0.
            steps  = 0
            while not done:
                # M      = self.policy
                inputs = (obs - self.mean)/self.std
                action = np.dot(M, inputs)
                observations.append(obs)
                actions.append(action)
                obs, r, done, _ = self.env.step(action)
                totalr += r
                steps  += 1
                if self.render:
                    self.env.render()
            returns.append(totalr)
        print(returns)
        self.tracker.track( np.mean(returns)*-1, x) 
        return np.mean(returns)*-1

class HalfCheetah:
    def __init__(self, method='', verbose=False):
        self.env     = gym.make('HalfCheetah-v2')
        self.env.seed(1234)
        self.mean = np.array(
                [-0.09292823,  0.07602245,  0.08993747,  0.02011249,  0.07981564,
               -0.08428448, -0.02150131, -0.03109106,  4.82287926, -0.05346475,
               -0.0318163 , -0.03715201, -0.18675299,  0.0663168 , -0.09290028,
                0.15043391,  0.2042574 ]
                )
        self.std     = np.array(
                [ 0.06852463,  0.35843727,  0.37874848,  0.36028137,  0.40588222,
                0.44399708,  0.3060632 ,  0.37465409,  2.24987835,  0.75029144,
                1.99427694,  8.82329989,  7.6671886 ,  9.35798155, 10.53909492,
                8.26358612,  9.38187307]
                ) 
        self.dim    = 102
        self.lb      = -1 * np.ones(self.dim)
        self.ub      =  1 * np.ones(self.dim)
        self.counter = 0    
        self.num_rollouts = 1
        self.render  = False
        self.policy_shape = (6, 17)
        self.tracker     = tracker('HalfCheetah102'+ '/'+method, verbose=verbose)
        

    def _rollout(self, M):
        obs    = self.env.reset()
        done   = False
        totalr = 0.
        steps  = 0
        while not done:
            # M      = self.policy
            inputs = (obs - self.mean)/self.std
            action = np.dot(M, inputs)
            obs, r, done, _ = self.env.step(action)
            totalr += r
            steps  += 1
            if self.render:
                self.env.render()
        return totalr
    
    def __call__(self, x):
        self.counter += 1
        assert len(x) == self.dim
        assert x.ndim == 1
        assert np.all(x <= self.ub) and np.all(x >= self.lb), "x={}".format(x)
        
        M = x.reshape(self.policy_shape)
        
        returns = []
        
        for i in range(self.num_rollouts):
            totalr = self._rollout(M)
            returns.append(totalr)
            if len(returns)>2 and np.std(returns)/np.mean(returns) < 0.02:
                break
        # print(returns)
        self.tracker.track( np.mean(returns)*-1, x) 
        return np.mean(returns)*-1

class Ant:
    
    def __init__(self, method='', verbose=False):
        self.env     = gym.make('Ant-v2')
        self.mean = np.array(
                [5.56454034e-01,  9.18653169e-01, -3.59727363e-03, -6.20272098e-02,
               -2.26681512e-01, -1.66021313e-01,  7.98706445e-01, -8.83793477e-02,
               -5.95357357e-01,  3.14583015e-01, -5.85966639e-01,  6.84079972e-02,
                6.99618809e-01,  2.95780894e+00,  1.31451677e-01,  4.08239776e-04,
                6.25140579e-04, -1.32464936e-02, -1.06268142e-02, -9.34088418e-04,
                1.12352209e-02, -3.71601166e-03, -1.86311242e-02, -1.94318787e-04,
               -2.35572098e-02,  1.33548941e-02,  1.25946113e-02,  0.00000000e+00,
                0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
                0.00000000e+00, -2.49252117e-04,  5.29426882e-06,  4.75874376e-06,
                2.32847072e-04,  5.75762573e-04,  8.34222363e-03,  0.00000000e+00,
                0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
                0.00000000e+00, -3.80581767e-05,  2.94468940e-05,  4.62228439e-05,
                2.04639349e-05, -2.98257872e-07,  3.23278948e-04,  1.19086373e-02,
               -2.88474509e-02, -1.60491286e-03, -1.15468224e-02, -5.18573673e-03,
                4.39587093e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
                0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  1.03066125e-04,
                4.18215532e-05, -3.65999652e-05,  3.74175884e-05, -1.98523872e-05,
                4.99099166e-04,  1.11910926e-01,  7.45127049e-03, -4.38796289e-02,
                2.97467313e-02,  4.89358585e-03,  1.28974957e-01,  0.00000000e+00,
                0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
                0.00000000e+00,  1.12650435e-04, -3.26512663e-05,  4.19272407e-05,
               -3.59913591e-05, -5.05936497e-05,  5.51822438e-04, -6.10782510e-02,
                6.99737676e-02, -1.27123567e-03, -4.54646225e-02, -1.65620982e-02,
                8.93125444e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
                0.00000000e+00,  0.00000000e+00,  0.00000000e+00, -5.55830763e-05,
               -6.29738077e-05, -6.13326988e-05, -4.75298058e-05,  2.61688022e-05,
                3.86520440e-04, -8.61966297e-02, -7.39283562e-02,  6.34951925e-02,
                4.75871842e-02,  1.46840689e-02,  1.04875544e-01])
        self.std     = np.array(
                [9.82386131e-02, 1.71413676e-01, 9.23065066e-02, 9.85791366e-02,
                2.30674141e-01, 3.19296252e-01, 2.78954135e-01, 4.25299638e-01,
                1.72736123e-01, 3.02430663e-01, 1.54406290e-01, 4.27092806e-01,
                2.12280098e-01, 1.62722323e+00, 8.18724778e-01, 9.55245088e-01,
                9.84276957e-01, 1.16302552e+00, 9.57916411e-01, 2.15066069e+00,
                3.60287543e+00, 5.62826909e+00, 9.92029067e-01, 2.12230037e+00,
                1.00035298e+00, 5.57262447e+00, 2.12884125e+00, 1.00000000e-08,
                1.00000000e-08, 1.00000000e-08, 1.00000000e-08, 1.00000000e-08,
                1.00000000e-08, 4.91261195e-02, 4.88916452e-02, 1.08286676e-02,
                7.23307828e-02, 7.26715002e-02, 9.09353971e-02, 1.00000000e-08,
                1.00000000e-08, 1.00000000e-08, 1.00000000e-08, 1.00000000e-08,
                1.00000000e-08, 1.52511323e-02, 1.51985990e-02, 1.43327130e-02,
                1.65332113e-02, 1.65517821e-02, 1.78261478e-02, 1.96089902e-01,
                2.00366360e-01, 1.86725875e-01, 1.98295932e-01, 1.96883391e-01,
                2.04547798e-01, 1.00000000e-08, 1.00000000e-08, 1.00000000e-08,
                1.00000000e-08, 1.00000000e-08, 1.00000000e-08, 1.84328950e-02,
                1.84974517e-02, 1.72217249e-02, 2.04573899e-02, 2.04837390e-02,
                2.21338164e-02, 3.35090685e-01, 3.32503591e-01, 3.39000967e-01,
                3.44379780e-01, 3.43916394e-01, 3.34484134e-01, 1.00000000e-08,
                1.00000000e-08, 1.00000000e-08, 1.00000000e-08, 1.00000000e-08,
                1.00000000e-08, 1.95365620e-02, 1.93568339e-02, 1.78721599e-02,
                2.15286944e-02, 2.16180668e-02, 2.33170648e-02, 2.82565159e-01,
                2.80505321e-01, 2.74944700e-01, 2.83438560e-01, 2.82863715e-01,
                2.84554295e-01, 1.00000000e-08, 1.00000000e-08, 1.00000000e-08,
                1.00000000e-08, 1.00000000e-08, 1.00000000e-08, 1.63294077e-02,
                1.63954634e-02, 1.55359386e-02, 1.80949693e-02, 1.80648025e-02,
                1.95055714e-02, 3.05150764e-01, 3.04174152e-01, 2.99804816e-01,
                3.09838747e-01, 3.10409375e-01, 3.05981876e-01])
        self.dim    = 888
        self.lb      = -1 * np.ones(self.dim)
        self.ub      =  1 * np.ones(self.dim)
        self.counter = 0    
        self.num_rollouts = 10
        self.render  = False
        self.policy_shape = (8, 111)
        self.tracker     = tracker('Ant'+ '/'+method, verbose=verbose)
        

            
    def __call__(self, x):
        self.counter += 1
        assert len(x) == self.dim
        assert x.ndim == 1
        assert np.all(x <= self.ub) and np.all(x >= self.lb), "x={}".format(x)
        
        M = x.reshape(self.policy_shape)
        
        returns = []
        observations = []
        actions = []
        
        for i in range(self.num_rollouts):
            obs    = self.env.reset()
            done   = False
            totalr = 0.
            steps  = 0
            while not done:
                # M      = self.policy
                inputs = (obs - self.mean)/self.std
                action = np.dot(M, inputs)
                observations.append(obs)
                actions.append(action)
                obs, r, done, _ = self.env.step(action)
                totalr += r
                steps  += 1
                if self.render:
                    self.env.render()
            returns.append(totalr)
        #print(returns)
        self.tracker.track( np.mean(returns)*-1, x) 
        return np.mean(returns)*-1