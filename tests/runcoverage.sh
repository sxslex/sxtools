export PYTHONPATH=`pwd`'/../../'
rm -rf .coverage
clear
nosetests --with-coverage --cover-erase --cover-html --cover-package ../ .
# radon cc $1 "$2". -a -s
