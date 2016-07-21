# (x3, y3)
# |
# |
# |
# (x1, y1) -------- (x2, y2)
from math import sqrt
import pyproj

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
    	return '(' + str(self.x) + ',' + str(self.y) + ')'

def distance(a, b):
	return sqrt((a.x-b.x)**2+(a.y-b.y)**2)

point_ll = Point(0, 0)
point_lr = Point(5, 0)
point_ul = Point(0, 5)


def find_circle_centers(point_ll, point_lr, point_ul, radius):
	width = distance(point_ll, point_lr)
	height = distance(point_ll, point_ul)

	x_distance_between_centers = sqrt(3) * radius
	y_distance_between_centers = 3 * radius / 2

	centers = []
	center = point_ll

	while center.y <= point_ul.y:
		point_on_y_axis = center.x
		while center.x <= point_lr.x:
			centers.append(Point(center.x, center.y))
			center.x = center.x + x_distance_between_centers
		center.x = point_on_y_axis
		center.y = center.y + y_distance_between_centers
	return centers

center_list = find_circle_centers(point_ll, point_lr, point_ul, 1)
print center_list

