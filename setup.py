from setuptools import setup, find_packages

setup(
    name="cobertura-clover-transform",
    version='1.0rc1',
    packages=find_packages(),
    description="Tools for transforming Cobertura test "
                "coverage XML into Clover-style XML",
    author='Chris Wacek',
    url='http://github.com/cwacek/cobertura-clover-transform',
    license='MIT',
    keywords='cobertura coverage test clover xml'
)