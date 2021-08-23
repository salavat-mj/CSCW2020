## bash

# conda install
MINICONDA=Miniconda3-4.5.4-Linux-x86_64.sh
wget -nc https://repo.continuum.io/miniconda/$MINICONDA -O Miniconda.sh
chmod +x Miniconda.sh
sudo mkdir -p /usr/local/conda
./Miniconda.sh -b -f -p /usr/local/conda 

# conda
source ./conda/bin/activate
pip install -r requirements.txtcrea

# jupyter
conda create --name jupyter 
source activate jupyter
conda install -c conda-forge jupyterlab

# envirovent
conda env create -f environment.yml python=3.5
source activate semantic
# conda install python=3.5
python -c 'import torch; print(torch.version.cuda)'

# env
source activate semantic
conda env update --file environment.yml --prune

# demo
source ./conda/bin/activate
source activate semantic
CHECK=./real_weights/black.pth
DEMO=./Dribbble_test/website
RESULT=./result
GLOVE=./glove.6B.50d.txt
python demo.py --tag=sport --checkpoint_path=$CHECK --demo_path=$DEMO --result_path=$RESULT --glove_path=$GLOVE --cuda=False
