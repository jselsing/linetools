# Module to run tests on spectra.io
import os
import pytest
import astropy.io.ascii as ascii
from astropy import units as u
import numpy as np

from linetools.spectra import io


def data_path(filename):
    data_dir = os.path.join(os.path.dirname(__file__), 'files')
    return os.path.join(data_dir, filename)

# Separate flux/error files
def test_sep_files():
    spec = io.readspec(data_path('UM184_nF.fits'))
    idl = ascii.read(data_path('UM184.dat.gz'), names=['wave', 'flux', 'sig'])
    np.testing.assert_allclose(spec.dispersion, idl['wave'])
    np.testing.assert_allclose(spec.sig, idl['sig'], atol=1e-3, rtol=0)

    assert spec.dispersion.unit == u.Unit('AA')
