export PYTHONPATH=`pwd`'/../../'
rm -rf .coverage
clear
nosetests -dsv --with-yanc --with-coverage --cover-erase --cover-html --cover-package $1 $2
#
# radon cc $1 "$2". -a -s
