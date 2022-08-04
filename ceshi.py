import torch

x = torch.Tensor(2, 4, 2)
print(x[:,1,None, 1].shape)