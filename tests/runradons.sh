export PYTHONPATH=`pwd`'/../../'
rm -rf .coverage
clear
radon cc "../" -a -s
