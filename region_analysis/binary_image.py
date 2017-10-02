import numpy as np
import cv2
import matplotlib.pyplot as plt

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        hist = [0]*256

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                intensity = 0
                for x in range(len(image[i][j])):

                    #Get intensity of pixel
                    intensity += image[i][j][x]

                #Add intensity into histogram
                hist[int(intensity / 3)] += 1
        #Save histogram plot in output folder
        plt.savefig('output\Binarized_image.png')
        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        # Get size of histogram
        size = len(hist)

        # Get total pixel
        totalPixel = 0
        for i in range(size):
            totalPixel += hist[i]

        current_max = 0
        threshold = 0
        sumT = 0
        sumF = 0
        sumB = 0
        wB = 0
        wF = 0
        varBetween = 0
        uB = 0
        uF = 0

        for i in range(size):
            sumT += i * hist[i]

        for i in range(size):

            #Get weight of background
            wB += hist[i]
            if (wB == 0):
                continue

            #Get weight of frontground
            wF = totalPixel - wB
            if wF == 0:
                break

            sumB += i * hist[i]
            sumF = sumT - sumB

            #Get mean of background
            uB = sumB / wB

            #Get mean of frontground
            uF = (sumF) / wF

            #Calculate between variance
            varBetween = float(wB) * float(wF) * (uB - uF) * (uB - uF)

            #Check if new maximum found
            if varBetween > current_max:
                current_max = varBetween
                threshold = i

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()

        # Get histogram of the image
        hist = self.compute_histogram(image)

        # Find the optimal threshold of the image
        threshold = self.find_optimal_threshold(hist)

        for row in range(bin_img.shape[0]):
            for col in range(bin_img.shape[1]):

                # Get average value of pixel (Red, Green, and Blue)
                adjusted = np.average(bin_img[row, col])

                # Compare the average value with threshold to assign black or white
                if (adjusted > threshold):
                    bin_img[row, col] = 0
                if (adjusted < threshold):
                    bin_img[row, col] = 255

        #Save binarized image in output folder
        cv2.imwrite('output\Binarized_image.png', bin_img)
        return bin_img


