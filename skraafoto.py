# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Skraafoto
                                 A QGIS plugin
 Klik i kortet og se skråfotos af det angivet punkt
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-01-31
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Kalundborg Kommune
        email                : andj@kalundborg.dk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, QUrl, Qt
from qgis.PyQt.QtGui import QIcon, QDesktopServices
from qgis.PyQt.QtWidgets import QAction
from qgis.gui import QgsMapTool, QgsMapToolEmitPoint
from qgis.utils import iface

from .resources import *  # Import the code for the icon
import os.path

class PointSelectorMapTool(QgsMapTool):
    def __init__(self, canvas):
        super(PointSelectorMapTool, self).__init__(canvas)
        self.canvas = canvas

    def canvasReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = event.mapPoint().x()
            y = event.mapPoint().y()
            url = f'https://skraafoto.dataforsyningen.dk/?orientation=north&center={x},{y}'
            QDesktopServices.openUrl(QUrl(url))

class Skraafoto:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(self.plugin_dir, 'i18n', 'Skraafoto_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        self.actions = []
        self.menu = self.tr(u'&Skraafoto')
        self.first_start = None
        self.mapCanvas = iface.mapCanvas()
        self.pointSelectorMapTool = PointSelectorMapTool(self.mapCanvas)

    def tr(self, message):
        return QCoreApplication.translate('Skraafoto', message)

    def add_action(self, icon_path, text, callback, enabled_flag=True, add_to_menu=True, add_to_toolbar=True, status_tip=None, whats_this=None, parent=None):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)
        return action

    def initGui(self):
        icon_path = ':/plugins/skraafoto/icon.png'
        self.add_action(icon_path, text=self.tr(u'Skraafoto'), callback=self.run, parent=self.iface.mainWindow())
        self.first_start = True

    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(self.tr(u'&Skraafoto'), action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        self.mapCanvas.setMapTool(self.pointSelectorMapTool)

