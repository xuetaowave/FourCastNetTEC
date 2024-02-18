#!/bin/bash -l
#SBATCH --time=01:00:00
#SBATCH -C gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --gpus-per-node=2
#SBATCH --cpus-per-task=8
#SBATCH -J afno
#SBATCH -o afno_backbone_finetune.out
#SBATCH -p GPU-8A100
#SBATCH --gres=gpu:a100:2
#SBATCH --qos=gpu_8a100

config_file=./config/AFNO.yaml
config='afno_backbone_tec_ustc'
run_num='0'

export HDF5_USE_FILE_LOCKING=FALSE
export NCCL_NET_GDR_LEVEL=PHB

export MASTER_ADDR=$(hostname)

set -x
srun -u --mpi=pmi2 shifter \
    bash -c "
    source export_DDP_vars.sh
    python train.py --enable_amp --yaml_config=$config_file --config=$config --run_num=$run_num
    "
