import torch
a = torch.tensor([[12.0, -51, 4], [6, 167, -68], [-4, 24, -41]])
(q, r) = torch.qr(a, out=None, some=True)
