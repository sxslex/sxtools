from sxtools import __description__
from sxtools import __version__
from setuptools import setup
from setuptools import find_packages

setup(
    name='sxtools',
    author='Alexandre Villela (SleX)',
    author_email='sx.slex@gmail.com',
    version=__version__,
    description=__description__,
    keywords='sxtools tools cache cache_def image string capitalize_name',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
)
