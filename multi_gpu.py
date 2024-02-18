
from utils import logging_utils
logging_utils.config_logger()

import torch.distributed as dist
dist.init_process_group(backend='nccl',
                            init_method='env://')