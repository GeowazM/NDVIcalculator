# -*- coding: utf-8 -*-
"""
/***************************************************************************
 NDVIcalculator
                                 A QGIS plugin
 Calculates the NDVI for an image
                             -------------------
        begin                : 2016-06-07
        copyright            : (C) 2016 by Christina Ludwig
        email                : s6chludw@uni-trier.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load NDVIcalculator class from file NDVIcalculator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .NDVI_calculator import NDVIcalculator
    return NDVIcalculator(iface)
