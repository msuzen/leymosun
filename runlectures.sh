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

# Lecture 1: wigner_semicircle.ipynb
echo " "
echo " Running wigner_semicircle.ipynb"
echo " "
rm -f lecturePy/wigner_semicircle.py
jupyter nbconvert --to python lectures/wigner_semicircle.ipynb --output-dir=./lecturePy --log-level=ERROR
python lecturePy/wigner_semicircle.py
echo " "
echo " Success running wigner_semicircle.ipynb"
echo " "

# Lecture 2: wigner_dyson_spacing.ipynb
echo " "
echo " Running wigner_dyson_spacing.ipynb"
echo " "
rm -f lecturePy/wigner_dyson_spacing.py
jupyter nbconvert --to python lectures/wigner_dyson_spacing.ipynb --output-dir=./lecturePy --log-level=ERROR
python lecturePy/wigner_dyson_spacing.py
echo " "
echo " Success running wigner_dyson_spacing.ipynb"
echo " "

# Lecture 3: spectral_unfolding.ipynb
echo " "
echo " Running spectral_unfolding.ipynb"
echo " "
rm -f lecturePy/spectral_unfolding.py
jupyter nbconvert --to python lectures/spectral_unfolding.ipynb --output-dir=./lecturePy --log-level=ERROR
python lecturePy/spectral_unfolding.py
echo " "
echo " Success running spectral_unfolding.ipynb"
echo " "

# Lecture 4: mixed_construction.ipynb
echo " "
echo " Running mixed_construction.ipynb"
echo " "
rm -f lecturePy/mixed_construction.py
jupyter nbconvert --to python lectures/mixed_construction.ipynb --output-dir=./lecturePy --log-level=ERROR
python lecturePy/mixed_construction.py
echo " "
echo " Success running mixed_construction.ipynb"
echo " "

# Lecture 5: wigner_cats.ipynb
echo " "
echo " Running wigner_cats.ipynb"
echo " "
rm -f lecturePy/wigner_cats.py
jupyter nbconvert --to python lectures/wigner_cats.ipynb --output-dir=./lecturePy --log-level=ERROR
python lecturePy/wigner_cats.py
echo " "
echo " Success running wigner_cats.ipynb"
echo " "

# Lecture 6: freezing_mgoe.ipynb
echo " "
echo " Running freezing_mgoe.ipynb"
echo " "
rm -f lecturePy/freezing_mgoe.py
jupyter nbconvert --to python lectures/freezing_mgoe.ipynb --output-dir=./lecturePy --log-level=ERROR
python lecturePy/freezing_mgoe.py
echo " "
echo " Success running freezing_mgoe.ipynb"
echo " "

# Lecture 7: rosenzweig_porter_gap_ratio.ipynb 
echo " "
echo " Running rosenzweig_porter_gap_ratio.ipynb"
echo " "
rm -f lecturePy/rosenzweig_porter_gap_ratio.py
jupyter nbconvert --to python lectures/rosenzweig_porter_gap_ratio.ipynb --output-dir=./lecturePy --log-level=ERROR
python lecturePy/rosenzweig_porter_gap_ratio.py
echo " "
echo " Success running rosenzweig_porter_gap_ratio.ipynb"
echo " "

# Lecture 8: krylov_fidelity_entangled.ipynb
echo " "
echo " Running krylov_fidelity_entangled.ipynb"
echo " "
rm -f lecturePy/krylov_fidelity_entangled.py
jupyter nbconvert --to python lectures/krylov_fidelity_entangled.ipynb --output-dir=./lecturePy --log-level=ERROR
python lecturePy/krylov_fidelity_entangled.py
echo " "
echo " Success running krylov_fidelity_entangled.ipynb"
echo " "




