import numpy as np
from leymosun.stats import pdf
from leymosun.random import normal, choice

def test_pdf():
    values = normal(0, 1.0, 1000)
    locations = np.arange(-5.0, 5.1, 0.1)
    density, locations = pdf(values, locations)
    mean_index = np.argmax(density)
    assert locations[mean_index] > -1.0
    assert locations[mean_index] < 1.0
    
def test_pdf2():
    values = normal(size=1000)
    locations_all = np.arange(-5.0, 5.0, step=1e-2)
    inx = choice(len(locations_all), 100, replace=False)
    locations = np.sort(locations_all[inx])# non-equidistant
    density, _locations = pdf(values, locations)
    len(density) == len(_locations)
