from Config import Config
import math
import numpy as np


class Ai:

    def __init__(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        self.xpos = kwargs['pos'][0]
        self.ypos = kwargs['pos'][1]
        self.xapple = kwargs['apple'][0]
        self.yapple = kwargs['apple'][1]
        self.size = kwargs['size']
        self.north = [self.get_intersect([self.xpos, self.ypos], [
            self.xpos, self.ypos+1], [30, Config["game"]["bumper_size"]], [50, Config["game"]["bumper_size"]])]
        self.east = [self.get_intersect([self.xpos, self.ypos], [
            self.xpos+1, self.ypos], [Config["game"]["width"]-Config["game"]["bumper_size"], 30], [Config["game"]["width"]-Config["game"]["bumper_size"], 50])]
        self.south = [self.get_intersect([self.xpos, self.ypos], [
            self.xpos, self.ypos-1], [30, Config["game"]["height"]-Config["game"]["bumper_size"]], [50, Config["game"]["height"]-Config["game"]["bumper_size"]])]
        self.west = [self.get_intersect([self.xpos, self.ypos], [
            self.xpos-1, self.ypos], [Config["game"]["bumper_size"], 30], [Config["game"]["bumper_size"], 50])]

    def action(self):
        # print(self.west)
        return "none"

    def get_intersect(self, a1, a2, b1, b2):
        """
        Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
        a1: [x, y] a point on the first line
        a2: [x, y] another point on the first line
        b1: [x, y] a point on the second line
        b2: [x, y] another point on the second line
        """
        s = np.vstack([a1, a2, b1, b2])        # s for stacked
        h = np.hstack((s, np.ones((4, 1))))  # h for homogeneous
        l1 = np.cross(h[0], h[1])           # get first line
        l2 = np.cross(h[2], h[3])           # get second line
        x, y, z = np.cross(l1, l2)          # point of intersection
        if z == 0:                          # lines are parallel
            return (float('inf'), float('inf'))
        return (x/z, y/z)
