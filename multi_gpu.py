import os

os.environ['MASTER_ADDR'] = '0'
os.environ['RANK'] = '0'
os.environ['WORLD_RANK'] = '0'
os.environ['LOCAL_RANK'] = '0'
os.environ['WORLD_SIZE'] = '2'
os.environ['WANDB_START_METHOD'] = 'thread'
os.environ['MASTER_PORT'] = '19500'

import torch.distributed as dist
dist.init_process_group()
pass