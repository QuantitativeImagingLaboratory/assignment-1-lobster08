********************
resample.py
********************


#############################
def nearest_neighbor():

First, create a new empty image of the scaled size of input image
Then, calculate the ratio of width and height
Next, divide the coordinate by the ratio respectively: row / row_ratio and col / col_ratio
Finally, use that calculated coordinate to get pixel value from input image and put it in new scaled image


#############################
def bilinear_interpolation():

First, create a new empty image of the scaled size of input image
Then, calculate the ratio of width and height of both image
Next, divide the coordinate by the ratio respectively: row / row_ratio and col / col_ratio
Use the calculated coordinate (original coordinate) input to the calculate_interpolation function to get the pixel value


#############################
def calculate_interpolation():

First, extract the integer and fractional parts of coordinate x and y
Second, choose the minimum values between integer parts and original coordinates
Third, get the pixel values from 4 corners in each channel
Then, calculate the interpolation using the formula from lecture
Finally, save the pixel values into a temporary list, and return it back to bilinear_interpolation function


*********************
interpolation.py
*********************

#############################
def linear_interpolation():

Assume that pt1, pt2, and unknown are lists. Each contains a coordinate (x,y) and a intensity value
Assume that intensity of unknown is 0 at the moment, we will update it after computing
    pt1 = [x,y,intensity]
    pt2= [x,y,intensity]
    unknown = [x,y,intensity]

Formula to use to calculate the intensity
    part1 = [ [(pt2(x) - unknown(x)) / (pt2(x) - pt1(x))] * (pt1(intensity) ]
    part2 = [ [(unknown(x) - pt1(x)) / (pt2(x) - pt1(x)] * (pt2(intensity)) ]
    unknown(intensity) = part1 + part2
    
#############################
def bilinear_interpolation():

Assume that pt1, pt2, and unknown are lists. Each contains a coordinate (x,y) and a intensity value
Assume that intensity of unknown is 0 at the moment, we will update it after computing
    pt1 = [x,y,intensity]
    pt2= [x,y,intensity]
    pt3= [x,y,intensity]
    pt4= [x,y,intensity]
    unknown = [x,y,intensity]
Then, use the linear_interpolation function to compute the intensity of point between pt1 and pt2, pt3 and pt4
Finally, use the computed intensity values to compute the unknown's intensity value using the linear_interpolation function


*************************************************************************
*************************************************************************
*************************************************************************
*********************
binary_image.py
*********************


#############################
def compute_histogram():

First, declare empty array with appropriate size
Second, use 3 nested for-loop:
    The first 2 loops are for going through each pixel in the image
    The third loop is get the intensity of the pixel
After finishing the third loop, divide the intensity by 3 to get the average and save it into the array


#############################
def find_optimal_threshold():

First, get all the variables ready: size of histogram, total pixels, threshold,...
Then, use a for loop to get sum total of pixel * frequency = sumT (sum total)
Next, use another for loop to find the optimal threshold
    First, get the weight of the background (skip, if value = 0)
    Second, get the weight of the foreground
    Now, get sum of the background, and calculate the sum of foreground = sumT - sumB
    Next, get the mean of the background = sumB / weight of the background
    Do the same to get mean of foreground
    Now, calculate the variance between class: weight of background * weight of foreground * 2*(difference between 2 means)
    Finally, check if variance between class if maximum or not. If it is, then return the counter of the for loop as the optimal threshold


#############################
def binarize():

First, make a copy of the input image
Second, get the histogram of the image using compute_histogram() function
Third, get the optimal threshold of the image using find_optimal_threshold() function
Next, use 2 nested for-loop to go through each pixel of the new copied image
    First, calculate the average value of the pixel's value at coordinate (row,col)
    Then, compare the average value with the threshold value
    Assign image pixel to white if average value is less than threshold, and black if greater than threshold


**********************
cell_counting.py
**********************

#############################
def blob_coloring():

First, declare a dictionary filled with zeros with the size of total pixel of the input image
Second, declare a label = 1 to labeling
Third, use a 2 nested for-loop to go through each pixel in the image
    First, calculate the average intensity value of the pixel at coordinate (row,col) = pixel
    Second, calculate the average intensity values for pixel above and on the left of current coordinate = leftPixel and upPixel
    Next, comparing current pixel with pixel on the left and pixel above

    1.  if (pixel > 0 and leftPixel == 0 and upPixel == 0):
            assign current pixel with a label and update label to a new one => label += 1

    2.  if (pixel > 0 and leftPixel == 0 and upPixel > 0):
            assign current pixel == pixel above

    3.  if (pixel > 0 and leftPixel > 0 and upPixel > 0):

            if (regions[row - 1, col] == 0 and regions[row, col - 1] == 0):
                assign current pixel with a new label
                assign left and above pixel with same label
                update label to a new one

            else:
                assign current pixel == pixel above

    4.  if (regions[row, col - 1] == regions[row - 1, col]):
            assign left pixel = above pixel


#############################
def compute_statistics():

First, create dictionaries: stats - to store stats info, tempStats - to store temporary info, and locationHist - to store coordinate
Second, use a nested for-loop to compute the statistics area and location

    Use 3 lists: totalX - to store all the col/x value that has same region number
                 totalY - to store all the row/y value that has same region number
                 area - to store area value for each region

    Going through the loop, get all the x and y value of the same region into totalX and totalY
    Every time we add x and y into the lists, we increase the value in area list by 1
    After got all the x and y of the same region number, find the average for each - this will be the centroid location of the region
    Then, add the location into the locationList dictionary
    Continue doing for all the region number
After finished going through the nested for-loop, use another for-loop to add all the stats info into the tempStats dictionary
Finally, use another for-loop to go through all the item in the tempStats and pick the one that has area value greater or equal to 15 and copy it to stats dictionary


#############################
def mark_regions_image():

First, get the max key of region dictionary to get the size for the new image
Second, create a blank image using the size found above
Third, use a for-loop to pull all the region number from stats dictionary and put them in a listReg list
Next, use a nested for-loop to go through all the pixel in the new image
    Use the (row,col) coordinate of each pixel to compare region value from region dictionary and listReg dictionary
    If current coordinate found in region dictionary is found in listReg list, then make the current coordinate pixel of the new img white
    Otherwise, ignore - black

Finally, use a for-loop to go through all the item in the stats dictionary
    First, get all the value in the stats dictionary: region, area, and coordinate
    Then, draw * and region and area at the coordinate into the new image


