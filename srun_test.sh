srun --nodes=1 --ntasks-per-node=2 --cpus-per-task=8 -p GPU-8A100 --time=1:00:00 --gres=gpu:a100:2 --qos=gpu_8a100 --pty bash
