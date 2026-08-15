# Python Practice

## Install Python
brew install python

## Check Python Version
python3 --version

## Check where it is installed
which python3

## Check pip
pip3 --version

or

python3 -m pip --version

### Note: -m refers to module

## install package
python3 -m pip install package-name

## Create a virtual environment
python3 -m venv venv

or 

python3 -m venv .venv

## Activate virtual environment
source venv/bin/activate

or

source .venv/bin/activate

## Now check Python version, where it is installed and pip version
python --version
which python
pip --version

## Upgrade pip
python -m pip install --upgrade pip
pip --version

## Test Python
python
print("Hello Python")

## Exit from Python
exit()

or 

ctl + z

## Deactivate Virtual environment
deactivate
