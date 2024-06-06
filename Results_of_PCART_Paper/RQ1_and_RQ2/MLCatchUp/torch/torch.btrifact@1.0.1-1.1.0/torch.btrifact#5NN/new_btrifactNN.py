import torch
A = torch.randn(2, 3, 3)
(A_LU, pivots) = torch.btrifact(A=A, info=None)
