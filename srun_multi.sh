srun -u --mpi=pmi2 --nodes=1 --ntasks-per-node=2 --cpus-per-task=8 -p GPU-8A100 --time=1:00:00 --gres=gpu:a100:2 --qos=gpu_8a100 \
     bash -c "
    /home/ess/cxt/miniconda3/bin/conda init bash
    source export_DDP_vars.sh
    conda activate pytorch
    python train.py --enable_amp --yaml_config=./config/AFNO.yaml --config=afno_backbone_tec_ustc --run_num=1
    "
