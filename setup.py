from setuptools import setup

fp = open("./leymosun/version.py")
sversion = fp.read()
__version__ = sversion.split('=')[1][1:-1]

with open("README.md") as f:
    long_description = f.read()

import sys

if (sys.version_info.major, sys.version_info.minor) < (3, 15):
    sys.exit(" Python < 3.15 is not supported or preferred")

setup(
    name="leymosun",
    version=__version__,
    description="Quantum information, statistics, dynamics and closely related computational tools. \
                 Quantum core, random matrix tools, spectral analysis tool, advanced linear algebra. \
                 Randomness tools.", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/msuzen/leymosun",
    author="M.Suzen",
    author_email="suzen@acm.org",
    license="GPL-3",
    packages=["leymosun"],
    install_requires=[
        "numpy >= 2.5.3",
        "matplotlib >= 3.10.3",
        "dill >= 0.4.1"
    ],
    test_suite="tests",
    extras_require={
        "dev": [
            "pytest >= 8.4.2",
            "coverage >= 7.10.7",
            "pytest-cov >= 7.0.0",
            "nbconvert >= 7.16.6",
            "ipython >= 9.17.1",
        ]
    },
    zip_safe=False,
)
