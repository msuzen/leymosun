#!/bin/bash
#
# Run notebooks after nbconvert
#
# Set -e: exit immediately if any command fails
set -e

# Set -u: error if undefined variable used
set -u

# Set -o pipefail: fail on pipeline failure (e.g., command fails in pipe)
set -o pipefail

# wigner_cats.ipynb
echo " "
echo " Running wigner_cats.ipynb"
echo " "
rm -f lecturePy/wigner_cats.py
jupyter nbconvert --to python lectures/wigner_cats.ipynb --output-dir=./lecturePy --log-level=ERROR
python lecturePy/wigner_cats.py
echo " "
echo " Success running wigner_cats.ipynb"
echo " "

# wigner_dyson_spacing.ipynb
echo " "
echo " Running wigner_dyson_spacing.ipynb"
echo " "
rm -f lecturePy/wigner_dyson_spacing.py
jupyter nbconvert --to python lectures/wigner_dyson_spacing.ipynb --output-dir=./lecturePy --log-level=ERROR
python lecturePy/wigner_dyson_spacing.py
echo " "
echo " Success running wigner_dyson_spacing.ipynb"
echo " "

# wigner_semicircle.ipynb
echo " "
echo " Running wigner_semicircle.ipynb"
echo " "
rm -f lecturePy/wigner_semicircle.py
jupyter nbconvert --to python lectures/wigner_semicircle.ipynb --output-dir=./lecturePy --log-level=ERROR
python lecturePy/wigner_semicircle.py
echo " "
echo " Success running wigner_semicircle.ipynb"
echo " "
