export PYTHONPATH=`pwd`'/../../'
rm -rf .coverage
clear
nosetests -dsv --with-yanc ../
# nosetests -dsv --with-yanc --with-coverage --cover-erase --cover-html --cover-package ../ .
# radon cc $1 "$2". -a -s
