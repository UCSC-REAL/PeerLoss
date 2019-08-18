import random
import numpy as np
import torch


def set_global_seeds(i):
    random.seed(i)
    np.random.seed(i)
    torch.manual_seed(i)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(i)


SEEDS = 16

def make_arg_list(arg):
    arg = arg.copy()
    args = []
    for seed in range(SEEDS):
        arg['seed'] = seed
        args.append(arg.copy())
    return args
