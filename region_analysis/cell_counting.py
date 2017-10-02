import numpy as np

class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""

        regions = dict()

        # Set all values in dictionary to 0
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                regions[row, col] = 0

        # Black = 1
        # White = 0
        label = 1
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):

                # Get pixel value at coordinate (row,col) or (y,x)
                pixel = np.average(image[row, col])

                # Get pixel value on the left of the coordinate (row,col)
                if (col == 0):
                    continue
                else:
                    upPixel = np.average(image[row, col - 1])

                # Get pixel value above of the coordinate (row,col)
                if (row == 0):
                    continue
                else:
                    leftPixel = np.average(image[row - 1, col])

                # Assign label at coordinate (row,col)
                if (pixel == 255 and leftPixel == 0 and upPixel == 0):
                    regions[row, col] = label
                    label += 1

                if (pixel == 255 and leftPixel == 0 and upPixel == 255):
                    regions[row, col] = regions[row - 1, col]

                if (pixel == 255 and leftPixel == 255 and upPixel == 0):
                    regions[row, col] = regions[row, col - 1]

                if (pixel == 255 and leftPixel == 255 and upPixel == 255):
                    regions[row, col] = regions[row - 1, col]

                if (regions[row, col - 1] == regions[row - 1, col]):
                    regions[row, col - 1] = regions[row - 1, col]

        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""



        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return 0

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        return image

