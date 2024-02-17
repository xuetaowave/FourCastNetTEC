# Python 代码
import GPUtil

# 获取所有 GPU 的信息
gpus = GPUtil.getGPUs()

for gpu in gpus:
    print(f"GPU ID: {gpu.id}, GPU Name: {gpu.name}")
    print(f"Memory Total: {gpu.memoryTotal} MB, Memory Free: {gpu.memoryFree} MB, Memory Used: {gpu.memoryUsed} MB")
    print(f"GPU Load: {gpu.load * 100}%\n")
