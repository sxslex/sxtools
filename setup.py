from sxtools import __description__
from sxtools import __version__
from setuptools import setup
from setuptools import find_packages

setup(
    name='sxtools',
    author='SleX',
    author_email='slex@slex.com.br',
    version=__version__,
    description=__description__,
    keywords='sxtools cachedef cache method tools',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
)
