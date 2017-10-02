import numpy as np
import cv2

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

        label = 1

        for row in range(image.shape[0]):
            for col in range(image.shape[1]):

                # Get pixel value at coordinate (row,col) or (y,x)
                pixel = np.average(image[row, col])

                # Get pixel value on the left of the coordinate (row,col)
                if (col == 0):
                    continue
                else:
                    leftPixel = np.average(image[row, col - 1])

                # Get pixel value above of the coordinate (row,col)
                if (row == 0):
                    continue
                else:
                    upPixel = np.average(image[row - 1, col])

                # Assign label at coordinate (row,col)
                if (pixel > 0 and leftPixel == 0 and upPixel == 0):
                    regions[row, col] = label
                    label += 1

                # Compare with pixel above
                if (pixel > 0 and leftPixel == 0 and upPixel > 0):
                    regions[row, col] = regions[row - 1, col]

                # Compare with pixel on the left
                if (pixel > 0 and leftPixel > 0 and upPixel == 0):
                    regions[row, col] = regions[row, col - 1]

                # Compare with pixel on the left and pixel above
                if (pixel > 0 and leftPixel > 0 and upPixel > 0):

                    if (regions[row - 1, col] == 0 and regions[row, col - 1] == 0):
                        regions[row, col] = label
                        regions[row - 1, col] = label
                        regions[row, col - 1] = label
                        label += 1
                    else:
                        regions[row, col] = regions[row - 1, col]

                # Compare if pixel on the left = with pixel above
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

        # Create a stats dictionary to store statistics
        stats = dict()

        tempStats = dict()
        locationList = dict()
        key = 1

        # Get maximum label value in region dictionary
        row, col = max(region, key=region.get)
        maximum = region[row, col]

        # Declare empty array for area from index 0 - 360
        # Maximum value in region is 361
        area = [0] * maximum

        for i in range(maximum):
            totalX = []
            totalY = []

            for k, v in region.items():
                if (v == key):
                    # Calculate the location using np.average
                    row, col = k
                    totalY.append(row)
                    totalX.append(col)

                    # Calculate total area for each key value from 1 to 361
                    area[key - 1] += 1

            # Calculate the centroid using average
            avgX = np.average(totalX)
            avgY = np.average(totalY)

            # Empty the list of x and y locations
            del totalY[:]
            del totalX[:]

            # Add the centroid location into a list
            locationList[key - 1] = (avgY, avgX)

            # Update key
            key += 1

        # Store all information into tempStats dictionary
        for i in range(maximum):
            tempStats[i] = ((i + 1), area[i], locationList[i])

        # Check and delete item that has area value less than 15
        x = 0
        for key, value in tempStats.items():
            reg, area, loc = value

            if (area >= 15):
                stats[x] = value
                x += 1


        return stats

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        x, y = max(image.keys())
        # Create new image of size of image input
        newImg = np.zeros((x + 1, y + 1, 3), np.uint8)

        # Get region that has area greater or equal to 15
        listReg = []
        for key, value in stats.items():
            reg, area, location = value
            if (area >= 15):
                listReg.append(reg)

        # Compare each pixel's label in image dictionary with region in stats dictionary to assign black or white for pixel's color
        for row in range(newImg.shape[0]):
            for col in range(newImg.shape[1]):

                for i in range(len(listReg)):

                    if (image[row, col] == listReg[i]):
                        newImg[row, col] = 255

        # Write text on image

        for key, value in stats.items():

            reg, area, loc = value
            text = "%s, %s" %(reg, area)
            col,row = loc
            row = int(row)
            col = int(col)
            cv2.putText(newImg, "*", (row,col), cv2.FONT_ITALIC, 0.5, color=(0,0,255))
            cv2.putText(newImg, "%s" %(text), (row+1, col+1), cv2.FONT_ITALIC, 0.2, color=(0, 0, 0))



        # cv2.putText(newImg, "*", (5,5), cv2.FONT_ITALIC, 0.35, color=(0, 0, 255))
        # print(stats)
        cv2.imwrite('output\marked_binary_image.png', newImg)

        return newImg


