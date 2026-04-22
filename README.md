# Leymosun: High-Entropy Randomness Research Toolkit

[![PyPI version](https://img.shields.io/pypi/v/leymosun.svg?maxAge=2591000)](https://pypi.org/project/leymosun/)
[![Downloads](https://static.pepy.tech/badge/leymosun)](https://pepy.tech/project/leymosun)
[![Downloads](https://pepy.tech/badge/leymosun/month)](https://pepy.tech/project/leymosun)
[![Static Badge](https://img.shields.io/badge/HAL--Science-hal--03464130-blue)](https://hal.science/hal-03464130/)
![Static Badge](https://img.shields.io/badge/Produce--of-Cyprus-D57800)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17912257.svg)](https://doi.org/10.5281/zenodo.17912257)  
[![arXiv:2512.22169](https://img.shields.io/badge/arXiv-2512.22169-B31B1B.svg)](https://arxiv.org/abs/2512.22169)
[![arXiv:2604.14224](https://img.shields.io/badge/arXiv-2604.14224-B31B1B.svg)](https://arxiv.org/abs/2604.14224)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18171032.svg)](https://doi.org/10.5281/zenodo.18171032)  

A package for randomness based research: Collection of reference implementations.

> ![](https://raw.githubusercontent.com/msuzen/leymosun/refs/heads/main/assets/cat.png)  
> **Figure** Empirical spectral density for mixed ensemble at $\mu=0.8$, so called `Wigner's Cats` with error bars. (See the lecture.)
> This is also known as `Wigner Cat Phases`, see [video](https://www.youtube.com/watch?v=hUih86O_uaw).
> [suzen25](https://arxiv.org/abs/2512.22169).

## Approach and features

The package provides tools and utilities for randomness based research with `High-Entropy Random Number Generation (HE-RNG)`. It means generation is performed with non-deterministic seeds every time a random library function is called.

Having non-reproducible and unpredictable RNGs could improve Monte Carlo and similar randomness
based computational science experimentation. Non-reproducible RNGs can still generate reproducible
research. Critical components in this direction is Uncertainty Quantification (UQ). Leymosun
implements bootstrapped based UQ and confidence interval generations.

### High-entropy random number utilities

The core package is providing strong randomness improving the simulation quality. We use NumPy grammar and as a backend.

* HE-RNG random states.
* Distributions:
  * Bionomial
  * Uniform integer on the given range
  * Uniform float on the given range
  * Normal distribution (Gaussian)
  * Random sampling from a set, choice.

### Random Matrices

* Generation of Gaussian ensembles (Orthogonal).
* Generation of Mixed Gaussian ensembles (Orthogonal) via `Mixed Matrix Ensemble Sampling (MMES) algoritm`
* Extract offdiagonal elements.
* Spectra generation given ensemble.
* Robust Spectral unfolding.
* Nearest-Neigbour Spacing Densities (NNSD).
* Adjacent gap ratio.
* Analytic distributions: Wigner semi-circle law, nearest-neigbour spacing.
* Generation of Rosenzweig-Porter ensemble.

### Linear Algebra

* Gram-Schmidt procedure.
* Krylov bases and Lanczos algorithm.

## Quantum Core

* Basic two states.
* Prepare maximally entangled.
* Pure state fidelity and spread complexity unitary evolution.
* Spread complexity Krylov unitary evolution.

### Statistics

* Centered PDF computation.
* Bootstrapped uncertainty quantification given observation matrix.

## Installation

It is recommended that latest stable package is released on the Python Package Index ([PyPI](https://pypi.org/project/leymosun/)). PyPI version should be installed via `pip`.

```bash
pip install leymosun
```

It is recommended that package shouldn't be installed via github version control, unless it is a
specific release.  

## Lectures

Lectures notes that introduce randomization concepts with the usage of `Leymosun`.
They also serve as functional tests.

* [](https://github.com/msuzen/leymosun/blob/main/lectures/.ipynb): `Title`. Short.

* Lecture 1: [wigner_semicircle.ipynb](https://github.com/msuzen/leymosun/blob/main/lectures/wigner_semicircle.ipynb): `Lecture on the Wigner's semicircle law`. The Wigner Semicircle law for the Gaussian Orthogonal Ensemble (GOE), comparison with the analytical case.
* Lecture 2: [wigner_dyson_spacing.ipynb](https://github.com/msuzen/leymosun/blob/main/lectures/wigner_dyson_spacing.ipynb): `Lecture on the Wigner-Dyson nearest-neighbour distribution`. The Wigner-Dyson spacing law for the Gaussian Orthogonal Ensemble (GOE), comparison with the analytical case.
* Lecture 3: [spectral_unfolding.ipynb](https://github.com/msuzen/leymosun/blob/main/lectures/spectral_unfolding.ipynb): `Self-consistent spectral unfolding` understanding what is a spectral unfolding.
* Lecture 4: [mixed_construction.ipynb.ipynb](https://github.com/msuzen/leymosun/blob/main/lectures/mixed_construction.ipynb.ipynb): `Construction of a mixed random matrix ensemble` understanding the inner details of constructing mixed ensemble.
* Lecture 5: [wigner_cats.ipynb](https://github.com/msuzen/leymosun/blob/main/lectures/wigner_cats.ipynb): `On the Wigner's cats`. Phenomenon of wigner cats.
* Lecture 6: [freezing_mgoe.ipynb](https://github.com/msuzen/leymosun/blob/main/lectures/freezing_mgoe.ipynb): `Frozen states and selective observation equivalence to mixed ensemble`. This is the physical setting for the wigner cats, frozen qubit and chaotic system.
* Lecture 7: [rosenzweig_porter_gap_ratio.ipynb](https://github.com/msuzen/leymosun/blob/main/lectures/rosenzweig_porter_gap_ratio.ipynb): `Rosenzweig-Porter Ensemble and Gap ratio:  Regular to chaotic quantum system`. A random matrix ensemble that can exhibit different phases.
* Lecture 8: [krylov_fidelity_entangled.ipynb](https://github.com/msuzen/leymosun/blob/main/lectures/krylov_fidelity_entangled.ipynb): `Spread Complexity and fidelity for entangled states`.
Demonstration of computing fidelity and spread complexity.

Additional lecture:

* [he_rng_nist.ipynb](https://github.com/msuzen/leymosun/blob/main/lectures/he_rng_nist.ipynb): `Lecture on Understanding High-Entropy RNGs with NIST  benchmark`. This lecture provides a way to test different RNGs or usage of RNGs via standard quality tests.

## Development notes

* Philosophy  
  There is a common misconception in computational sciences that speed is the ultimate goal, however primary objective is scientific correctness first. For this reasons, scientific correctness is taken precedence over speed in the development of the package. For proven methods being a baseline, we might implement faster versions.
* Testing
  * `tests` and `nbconvert` should be present as recommended dependency.
  * Test script should pass before any release.
    Unit tests `runtests.sh` and lectures `runlectures.sh`. (`lecturePy` directory is needed but this is ignored in the repo via `.gitignore`).
  * Add unit tests for each new method and features.
  * Add run portion for the new lecture in `runlecture.sh`.
* Release:
  * Build `python setup.py sdist`
  * Release to PyPI `twine upload dist/your_got.tar.gz`
  * Make sure that github repo release versions are matching.

## Citation

Please cite this package as follows

```bibtex
@misc{suzen25,
  author       = {Suzen, Mehmet},
  title        = {Leymosun: High-Entropy Randomness Research Toolkit},
  month        = dec,
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17937440},
  url          = {https://doi.org/10.5281/zenodo.17937440},
}
```

## Publications

Papers, manuscripts, datasets and other material that used `leymosun`.

* Scrambling of Entanglement from Integrability to Chaos: Bootstrapped Time-Integrated Spread Complexity, M. Suzen, arXiv, [arXiv:2604.14224](https://arxiv.org/abs/2604.14224) (2026)
* Wigner Cat Phases: A finely tunable system for exploring the transition to quantum chaos, M. Suzen, arXiv, [arXiv:2512.22169](https://arxiv.org/abs/2512.22169) (2025).
  * Associated dataset [Zenodo](https://zenodo.org/records/18171032)
* Empirical deviations of semicircle law in mixed-matrix ensembles, M. Suzen, HAL-Science, [hal-03464130](https://hal.science/hal-03464130/) (2021).
 2025 improvements with the `leymosun` package.

We would be grateful for a citation of our paper(s) if you use `leymosun` or ideas from the package in your research. Initial introduction of mixed matrix ensembles and MMES algorithm with M-shaped (Wigner's Cat) density [suzen21, suzen25], integrated spread complexity [suzen26a]. The following is the bibtex entries:

```bibtex
@article{suzen26a,
  title={Scrambling of Entanglement from Integrability to Chaos: Bootstrapped Time-Integrated Spread Complexity}, 
  author={S{\"u}zen, M.},
  year={2026},
  eprint={2604.14224},
  archivePrefix={arXiv},
  primaryClass={quant-ph},
  url={https://arxiv.org/abs/2604.14224}, 
}

@article{suzen25,
  title={Wigner Cat Phases: A finely tunable system for exploring the transition to quantum chaos}, 
  author={S{\"u}zen, M.},
  year={2025},
  eprint={2512.22169},
  archivePrefix={arXiv},
  primaryClass={quant-ph},
  url={https://arxiv.org/abs/2512.22169}, 
}

@article{suzen21,
  title={Empirical deviations of semicircle law in mixed-matrix ensembles},
  author={S{\"u}zen, Mehmet},
  year={2021},
  journal={HAL-Science},
  url={https://hal.science/hal-03464130/}
}
```

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
 [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

(c) 2026
M. Süzen

All codes are released under GPLv3.  
Documentations are released under CC BY 4.0.
