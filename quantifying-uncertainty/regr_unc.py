import matplotlib.pyplot as plt
from tqdm.auto import tqdm
import torch
from torch import Tensor
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from torchvision import datasets, transforms
from typing import Dict, List, Optional, Union

class EnsembleModel(nn.Module):

    def __init__(self, ensemble_members:[nn.Module]):
        super().__init__()
        self._models = ensemble_members

    def forward(self, x:Tensor) -> Tensor:
        votes = [m(x) for m in self._models]
        votes = torch.stack(votes)
        mu = torch.mean(votes, dim=0)
        return mu

    def stdev(self, x:Tensor) -> Tensor:
        votes = [m(x) for m in self._models]
        votes = torch.stack(votes)
        std = torch.std(votes, dim=0)
        return std

    def train(self):
        for m in self._models:
            m.train()
            
    def eval(self):
        for m in self._models:
            m.eval()
            

def mc_dropout_mu_stdev(net:nn.Module, x:Tensor, n:int=20) -> [Tensor, Tensor]:
    net.train()
    samples = []
    for _ in range(n):
        samples.append(net(x))
    samples = torch.stack(samples)
    mu = torch.mean(samples, dim=0)
    stdev = torch.std(samples, dim=0)
    return mu, stdev
        
