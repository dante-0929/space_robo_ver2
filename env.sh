#!/usr/bin/bash

wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
python3 -m pip install --upgrade pip
python3 -m pip install -U opencv-python
python3 -m pip install -U Pillow
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
suod apt-get install qt4-dev-tools qt4-doc