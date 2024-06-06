from .synthetic import tracker
import LassoBench
import numpy as np


class LassoBenchFunction:
    """
    Select a benchmark from LassoBench.
    """

    def __init__(self, method='', noise=False, verbose=False):
        """
        For synthentic benchmarks, we test TuRBO on the noisy and noiseless case.
        Args:
            noise (boolean): selecting noisy or noiseless benchmark
        """
        self.synt_bench = LassoBench.SyntheticBenchmark(pick_bench='synt_hard', noise=noise)
        dim = self.synt_bench.n_features
        self.dim = dim
        self.lb = -1 * np.ones(dim)
        self.ub = 1 * np.ones(dim)
        if noise:
            dir_name='synt_hard_noise'
        else:
            dir_name='synt_hard'
        self.tracker = tracker(dir_name+ '/'+method, verbose=verbose)

    def __call__(self, x):

        assert len(x) == self.dim
        assert x.ndim == 1
        assert np.all(x <= self.ub) and np.all(x >= self.lb)

        y = self.synt_bench.evaluate(x)
        self.tracker.track( y, x )
        return y