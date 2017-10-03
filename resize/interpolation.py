class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        #Write your code for linear interpolation here

        # Assume that pt1, pt2, and unknown are lists. Each contains a coordinate (x,y) and a intensity value
        # Assume that intensity of unknown is 0 at the moment, we will update it after computing
        # pt1 = [x,y,intensity]
        # pt2= [x,y,intensity]
        # unknown = [x,y,intensity]

        # Formula to use to calculate the intensity
        # part1 = [ [(pt2(x) - unknown(x)) / (unknown(x) - pt1(x))] * (pt1(intensity) ]
        # part2 = [ [(unknown(x) - pt1(x)) / (pt2(x) - pt1(x)] * (pt2(intensity)) ]
        # unknown(intensity) = part1 + part2

        # Get all the values from inputs
        x1, y1, int1 = pt1
        x2, y2, int2 = pt2
        x, y, intUnknown = unknown

        print(x1, y1, int1)
        print(x2, y2, int2)
        print(x, y, intUnknown)

        if (y1 == y2):
            part1 = float((x2 - x) / (x2 - x1) * (int1))
            part2 = float((x - x1) / (x2 - x1) * (int2))
            intUnknown = part1 + part2
        elif (x1 == x2):
            part1 = float((y2 - y) / (y2 - y1) * (int1))
            part2 = float((y - y1) / (y2 - y1) * (int2))
            intUnknown = part1 + part2

        # print("Intensity: %s" %intUnknown)
        # unknown[2] = intUnknown

        return intUnknown

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task
        # Assume that pt1, pt2, and unknown are lists. Each contains a coordinate (x,y) and a intensity value
        # Assume that intensity of unknown is 0 at the moment, we will update it after computing
        # pt1 = [x,y,intensity]
        # pt2= [x,y,intensity]
        # unknown = [x,y,intensity]

        # First get the location of the interpolation point between pt1 and pt2, pt3 and pt4, and pt1 and pt4
        x1, y1, int1 = pt1
        x2, y2, int2 = pt2
        x3, y3, int3 = pt3
        x4, y4, int4 = pt4
        x, y, intUnknown = unknown

        # Get the x and y coordinate of the point between 2 pts
        x_12 = x
        y_12 = y1
        intUnknown12 = 0

        # Create a new list to store the location and pass it to linear interpolation function to compute the intensity
        unknown_12 = [x_12, y_12, intUnknown12]

        # Get the x and y coordinate of the point between 2 pts
        x_34 = x
        y_34 = y3
        intUnknown34 = 0

        # Create a new list to store the location and pass it to linear interpolation function to compute the intensity
        unknown_34 = [x_34, y_34, intUnknown34]

        # Compute the intensity of unknown between each pt, and update it in each list
        unknown_12[2] = self.linear_interpolation(pt1, pt2, unknown_12)
        unknown_34[2] = self.linear_interpolation(pt3, pt4, unknown_34)

        print(unknown_12)
        print(unknown_34)

        # Compute the intensity of the unknown point
        unknown[2] = self.linear_interpolation(unknown_12, unknown_34, unknown)

        # print("Intensity: %s" %(unknown[2]))


        return unknown[2]
