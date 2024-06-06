import torch
tensor = torch.randn(3, 3).cuda()
result = tensor * 2
torch.cuda.synchronize(device=None)
