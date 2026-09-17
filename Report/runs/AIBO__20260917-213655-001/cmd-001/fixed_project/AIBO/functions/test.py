# -*- coding: utf-8 -*-

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
    
dims=20
f1 = Griewank(dim=dims)
f2 = Griewank_parallel(dim=dims)

X = np.random.rand(10, dims)
y1 = np.array([f1(x) for x in X])
y2 = f2(X)
print(y1-y2)




# import numpy as np
# import matplotlib.pyplot as plt

# def custom_exponential_decay_weights(length, first_value, last_value):
#     # 生成指数递减的向量，最后一位为 last_value，其他位置指数递减
#     exponential_vector = np.exp(np.linspace(0, 1, length) * np.log(last_value / first_value))
    
#     # 线性插值，确保第一位和最后一位的值
#     weights_vector = np.interp(np.linspace(0, 1, length), [0, 1], [first_value, last_value])
#     weights_vector *= exponential_vector
    
#     return weights_vector

# # 设置向量长度、第一位和最后一位的值
# length = 10
# first_value = 1.0
# last_value = 0.1

# # 生成递减速率为 exp(x) 的权重向量并控制第一位和最后一位的值
# weights_vector = custom_exponential_decay_weights(length, first_value, last_value)

# print(weights_vector)

# plt.plot(weights_vector, linestyle='-', label='Weight Vector')
# plt.show()