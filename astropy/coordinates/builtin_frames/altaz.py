# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import (absolute_import, unicode_literals, division,
                        print_function)

from warnings import warn

from ...utils.exceptions import AstropyWarning
from ..representation import SphericalRepresentation
from ..baseframe import (BaseCoordinateFrame, FrameAttribute,
                         TimeFrameAttribute, RepresentationMapping)

from .consts import EQUINOX_B1950


class AltAz(BaseCoordinateFrame):
    """
    A coordinate or frame in the Altitude-Azimuth system (i.e., Horizontal
    coordinates).

    .. warning::
        The AltAz class currently does not support any transformations. In a
        future version, it will support the standard IAU2000 AltAz<->ICRS
        transformations.  It is provided right now as a placeholder for storing
        as-observed horizontal coordinates.

    Parameters
    ----------
    representation : `BaseRepresentation` or None
        A representation object or None to have no data (or use the other keywords)
    az : `Angle`, optional, must be keyword
        The Azimuth for this object (``alt`` must also be given and
        ``representation`` must be None).
    alt : `Angle`, optional, must be keyword
        The Altitude for this object (``az`` must also be given and
        ``representation`` must be None).
    distance : :class:`~astropy.units.Quantity`, optional, must be keyword
        The Distance for this object along the line-of-sight.
    """

    frame_specific_representation_info = {
        'spherical': [RepresentationMapping('lon', 'az'),
                      RepresentationMapping('lat', 'alt')],
    }
    frame_specific_representation_info['unitspherical'] = \
        frame_specific_representation_info['spherical']

    default_representation = SphericalRepresentation
    equinox = TimeFrameAttribute(default=EQUINOX_B1950)
    location = FrameAttribute(default=None)
    obstime = TimeFrameAttribute(default=None)

    def __init__(self, *args, **kwargs):

        warn(AstropyWarning('The AltAz class currently does not support any '
                            'transformations.  In a future version, it will '
                            'support the standard IAU2000 AltAz<->ICRS '
                            'transformations.'))
        super(AltAz, self).__init__(*args, **kwargs)
