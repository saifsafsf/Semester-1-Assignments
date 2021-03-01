import math     # To use sqrt function
def points_distance(point1, point2, point3, point4):
    '''points_distance(a, b, c, d)
        Returns distance between two coordinate points.'''  # Documentation
    horz_dist = (point2 - point1)**2
    vert_dist = (point4 - point3)**2
    length = math.sqrt(horz_dist + vert_dist)   # To be returned value
    return length
X1 = float(input('Enter X1: '))     # Taking Inputs
Y1 = float(input('Enter Y1: '))
X2 = float(input('Enter X2: '))
Y2 = float(input('Enter Y2: '))
distance = points_distance(X1, X2, Y1, Y2)  # Caliing Function
print(f'Distance between ({X1}, {Y1}) & ({X2}, {Y2}) is {distance:.5}')
