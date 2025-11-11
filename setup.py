from setuptools import setup

fp = open("./leymosun/version.py")
exec(fp.read())

with open("README.md") as f:
    long_description = f.read()

import sys

if (sys.version_info.major, sys.version_info.minor) < (3, 11):
    sys.exit(" Python <= 3.11 is not supported or preferred")

setup(
    name="leymosun",
    version=__version__,
    description="High-Entropy Statistical Research Toolkit. Generation of \
                random matrices in canonical and mixed ensembles. Matrix utilities, \
                spectral analysis tools, analytic expressions from theory.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/msuzen/leymosun",
    author="M.Suzen",
    author_email="suzen@acm.org",
    license="GPL-3",
    packages=["leymosun"],
    install_requires=[
        "numpy == 2.3.1",
        "matplotlib == 3.10.3",
        "dill == 0.4.0"
    ],
    test_suite="tests",
    extras_require={
        "test":["pytest==8.4.2", "coverage==7.10.7", "pytest-cov==7.0.0"]
    },
    zip_safe=False,
)
