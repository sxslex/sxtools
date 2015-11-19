export PYTHONPATH=`pwd`'/../../'
rm -rf .coverage
clear
radon cc $1 -a -s
