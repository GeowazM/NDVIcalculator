# -*- coding: utf-8 -*-
"""
/***************************************************************************
 NDVIcalculator
                                 A QGIS plugin
 Calculates the NDVI for an image
                              -------------------
        begin                : 2016-06-07
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Christina Ludwig
        email                : s6chludw@uni-trier.de
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
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from NDVI_calculator_dialog import NDVIcalculatorDialog
import os.path
from osgeo import gdal
from gdalconst import *
from arraysplitter import splitter
import numpy as np


class NDVIcalculator:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'NDVIcalculator_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = NDVIcalculatorDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&NDVI calculator')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'NDVIcalculator')
        self.toolbar.setObjectName(u'NDVIcalculator')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('NDVIcalculator', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/NDVIcalculator/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Calculates NDVI'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&NDVI calculator'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Variables
            inputFile = self.dlg.lineEdit_input.text()
            outputFile = self.dlg.lineEdit_output.text()
            bandNir = self.dlg.spinBox_nir.value()
            bandRed = self.dlg.spinBox_red.value()
            ncols = self.dlg.spinBox_x.value()
            nrows = self.dlg.spinBox_y.value()
            nodataValue = -32768

            # Open dataset
            dataset = gdal.Open(inputFile, GA_ReadOnly )
            #nrows, ncols = dataset.GetRasterBand(1).ReadAsArray().shape

            # Get Geotransformation and projection from input file for output file
            geotrans = dataset.GetGeoTransform()
            proj = dataset.GetProjection()
            del dataset

            # Set up array splitter
            redTiles = splitter(inputFile, bandRed, ncols, nrows )
            nirTiles = splitter(inputFile, bandNir, ncols, nrows )

            # Create output file
            driver = gdal.GetDriverByName("GTIFF")
            NDVIout = driver.Create(outputFile, ncols, nrows, 1, gdal.GDT_Float32)
            NDVIout.GetRasterBand(1).SetNoDataValue(nodataValue)
            NDVIout.SetGeoTransform(geotrans)
            NDVIout.SetProjection(proj)

            for tile in range(redTiles.GetTileCount()):

                # Get next tile of red and nir channel
                red = redTiles.GetNextTile()
                nir = nirTiles.GetNextTile()

                # Calculate NDVI
                NDVI = (nir - red) / (nir + red)

                # Write to output file
                tileCoords = redTiles.GetCurrentTileCoordinates()
                print tileCoords
                NDVI = np.where(np.isnan(NDVI), nodataValue, NDVI )
                NDVIout.GetRasterBand(1).WriteArray(NDVI, tileCoords[0], tileCoords[1])

            del NDVIout

#
# def outFile( self ):
#     ( self.filePath, self.encoding ) = saveDialog( self.dlg )
#     if self.filePath is None or self.encoding is None:
#         return
#
#     outPath = self.filePath
#     if "\\" in outPath:
#         digit = -((len(outPath) - outPath.rfind("\\")) - 1)
#         self.fileName = outPath[digit:]
#     else:
#         digit = -((len(outPath) - outPath.rfind("/")) - 1)
#         self.fileName = outPath[digit:]
#     outName = self.fileName
#     if outName[-4:] == ".shp":
#         digit = len(outName) - 4
#         self.fileName = self.fileName[:digit]
#
#
# # Generate a save file dialog with a dropdown box for choosing encoding style
# def saveDialog( parent, filtering="Shapefiles (*.shp *.SHP)"):
#     settings = QSettings()
#     dirName = settings.value( "/UI/lastShapefileDir" )
#     encode = settings.value( "/UI/encoding" )
#     fileDialog = QgsEncodingFileDialog( parent, "Save output shapefile", dirName, filtering, encode )
#     fileDialog.setDefaultSuffix( "shp" )
#     fileDialog.setFileMode( QFileDialog.AnyFile )
#     fileDialog.setAcceptMode( QFileDialog.AcceptSave )
#     fileDialog.setConfirmOverwrite( True )
#     if not fileDialog.exec_() == QDialog.Accepted:
#             return None, None
#     files = fileDialog.selectedFiles()
#     settings.setValue("/UI/lastShapefileDir", QFileInfo( unicode( files[0] ) ).absolutePath() )
#     return ( unicode( files[0] ), unicode( fileDialog.encoding() ) )
