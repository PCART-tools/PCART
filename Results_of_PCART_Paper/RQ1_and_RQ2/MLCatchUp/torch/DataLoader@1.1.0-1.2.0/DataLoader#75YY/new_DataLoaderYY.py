import torch
from torch.utils.data import DataLoader, TensorDataset
data = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [7.0, 8.0]], dtype=torch.float32)
labels = torch.tensor([0, 1, 0, 1], dtype=torch.int64)
dataset = TensorDataset(data, labels)
batch_size = 2
shuffle = True
num_workers = 2
dataloader = DataLoader(dataset, batch_size, shuffle=shuffle, sampler=None, batch_sampler=None, num_workers=num_workers, collate_fn=callable, pin_memory=False, drop_last=False, timeout=0, worker_init_fn=None, multiprocessing_context=None)
