# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Skraafoto
                                 A QGIS plugin
 Klik i kortet og se skråfotos af det angivet punkt
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-01-31
        copyright            : (C) 2024 by Kalundborg Kommune
        email                : andj@kalundborg.dk
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
    """Load Skraafoto class from file Skraafoto.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .skraafoto import Skraafoto
    return Skraafoto(iface)