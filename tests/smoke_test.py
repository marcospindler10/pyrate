"""
Pyrate - Optical raytracing based on Python

Copyright (C) 2014 Moritz Esslinger <moritz.esslinger@web.de>
               and Johannes Hartung <j.hartung@gmx.net>
               and     Uwe Lippmann <uwe.lippmann@web.de>
               and    Thomas Heinze <t.heinze@fn.de>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
"""

from nose.tools import with_setup

__author__ = 'Thomas Heinze'

def setup_function():
    """Setup function, which is called before every test."""
    # we use the matplotlib's do nothing backend for testing
    # matplotlib/lib/matplotlib/backends/backend_template.py
    import matplotlib
    matplotlib.use('Template')

@with_setup(setup_function)
def test_smoke_doublet():
    """Smoke test based on demo_doublet.py."""
    import demo_doublet
    assert True

@with_setup(setup_function)
def test_smoke_mirrors():
    """Smoke test based on demo_doublet.py."""
    import demo_mirrors
    assert True
