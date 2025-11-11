# Leymosun: High-Entropy Statistical Research Toolkit

[![PyPI version](https://img.shields.io/pypi/v/leymosun.svg?maxAge=2591000)](https://pypi.org/project/leymosun/)
[![Downloads](https://static.pepy.tech/badge/leymosun)](https://pepy.tech/project/leymosun)
[![Downloads](https://pepy.tech/badge/leymosun/month)](https://pepy.tech/project/leymosun)
[![Static Badge](https://img.shields.io/badge/HAL--Science-hal--03464130-blue)](https://hal.science/hal-03464130/)
![Static Badge](https://img.shields.io/badge/Produce--of-Cyprus-D57800)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17578757.svg)](https://doi.org/10.5281/zenodo.17578757)


A package for randomness based research topics.    

>![](https://github.com/msuzen/leymosun/blob/main/assets/cat.png)   
> **Figure** Empirical spectral density for mixed ensemble at $\mu=0.8$, so called `Wigner's Cats`.

## Approach and features

The package provides tools and utilities for randomness based research with `High-Entropy Random Number Generation (HE-RNG)`. It means generation is performed with non-deterministic seeds every time a random
library function is called. 

There is a common misconception in computational sciences that speed is the ultimate goal, however primary objective is scientific correctness first. For this reasons, scientific correctness is taken precedence over speed in the development of the package. For proven methods being a baseline, we might implement faster versions. 

### High-entropy random number utilities 

The core package is providing strong randomness improving the simulation quality. We use NumPy grammar and as a backend.
* HE-RNG random states. 
* Distributions: 
  * Bionomial
  * Uniform integer on the given range
  * Uniform float on the given range
  * Normal distribution (Gaussian)

### Random Matrices
* Generation of Gaussian ensembles (Orthogonal).
* Generation of Mixed Gaussian ensembles (Orthogonal).
* Extract offdiagonal elements.
* Spectra generation given ensemble.
* Analytic distributions: Wigner semi-circle law. 

### Data manager
* Storage object utilities.

## Lectures

Lectures notes that introduce randomization concepts with the usage of `Leymosun`.

* [wigner_semicircle.ipynb](https://github.com/msuzen/leymosun/blob/main/lectures/wigner_semicircle.ipynb): `Lecture on the Wigner's semicircle law`. The Wigner Semicircle law for the Gaussian Orthogonal Ensemble (GOE), comparison with the analytical case. 
* [wigner_semicircle_mixed.ipynb](https://github.com/msuzen/leymosun/blob/main/lectures/wigner_semicircle_mixed.ipynb): `Lecture on the Wigner's cats`. Deviations from the Wigner Semicircle law for the mixed-Gaussian Orthogonal Ensemble (GOE). This would demonstrate, so-called "Wigner's Cats", i.e., the deviation makes the density looks like cat. 
* [he_rng_nist.ipynb](https://github.com/msuzen/leymosun/blob/main/lectures/he_rng_nist.ipynb): `Lecture on Understanding High-Entropy RNGs with NIST  benchmark`. This lecture provides a way to test different RNGs or usage of RNGs via standard quality 
tests. 

## Publications

Papers, datasets and other material that used `leymosun`. 

* Empirical deviations of semicircle law in mixed-matrix ensembles, M. Suzen, HAL-Science, [hal-03464130](https://hal.science/hal-03464130/) (2021).    
 2025 improvements with the `leymosun` package.

## Citation

We would be grateful for a citation of our paper(s) if you use `leymosun` or ideas from the package in your research.  The following is the bibtex entry

```
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
 [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/).

(c) 2025   
M. Süzen

All codes are released under GPLv3.  
Documentations are released under CC BY 4.0. 

