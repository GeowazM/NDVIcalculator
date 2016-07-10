from gdalconst import GA_ReadOnly
import numpy as np
from osgeo import gdal

class splitter():

    def __init__(self, data, bandNo, ncols, nrows):

        self.tile_nr = 0
        self.dataset = gdal.Open(data, GA_ReadOnly)
        self.band = self.dataset.GetRasterBand(bandNo)
        self.nodataValue = self.band.GetNoDataValue()

        endY, endX = self.band.ReadAsArray().shape

        startX = 0
        startY = 0

        stepSizeX = endX / ncols
        stepSizeY = endY / nrows

        if endY <= nrows:
            ncols = endY

        if endX <= ncols:
            nrows = endX

        lolimY = np.arange(startY, endY, stepSizeY)[:-1]
        stepsY = np.diff(lolimY)
        stepsY = np.append(stepsY, endY - lolimY[-1])

        lolimX = np.arange(startX, endX, stepSizeX)[:-1]
        stepsX = np.diff(lolimX)
        stepsX = np.append(stepsX, endX - lolimX[-1])

        self.tiles = []
        for i in range(0, len(lolimY)):
            for j in range(0, len(lolimX)):
                tile = (int(lolimX[j]), int(lolimY[i]), int(stepsX[j]), int(stepsY[i]))
                self.tiles.append(tile)
                

    def GetNextTile(self):
        self.tile = self.band.ReadAsArray(self.tiles[self.tile_nr][0], self.tiles[self.tile_nr][1], self.tiles[self.tile_nr][2], self.tiles[self.tile_nr][3]).astype(np.float64)
        if self.nodataValue != None:
            self.tile = np.where(self.tile == self.nodataValue, np.nan, self.tile)
        self.tile_nr += 1
        return self.tile

    def GetTileCount(self):
        nr_tiles = len(self.tiles)
        return nr_tiles

    def GetCurrentTileCoordinates(self):
        return self.tiles[self.tile_nr-1]

    def reset(self):
        self.tile_nr = 0

    def Close(self):
        del self.band
        del self.tiles
        del self.tile
        del self.dataset