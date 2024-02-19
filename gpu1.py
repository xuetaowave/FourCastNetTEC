import torch.distributed as dist
import os
# 设置主进程的 IP 地址和端口号
os.environ['MASTER_ADDR'] = '127.0.0.1'
os.environ['MASTER_PORT'] = '29501'
# 设置当前进程的局部排名（local_rank）
os.environ['RANK'] = '1'
os.environ['WORLD_SIZE'] = '2'

dist.init_process_group(backend='nccl') # 初始化分布式训练环境
# 获取当前进程的排名和总进程数
rank = dist.get_rank()
world_size = dist.get_world_size()
# 在分布式训练中使用排名和总进程数
print(f"Rank: {rank}, World size: {world_size}")
# 执行分布式训练代码
# ...
dist.destroy_process_group()  # 释放资源

