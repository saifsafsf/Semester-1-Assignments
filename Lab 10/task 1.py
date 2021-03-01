import math                                     # Importing modules

def points_distance(point1, point2):
    '''Returns distance between two coordinate points.'''  # Documentation
    horz_dist = (point1[0] - point2[0])**2
    vert_dist = (point1[1] - point2[1])**2
    length = math.sqrt(horz_dist + vert_dist)   # To be returned value
    return length

points = int(input('Enter number of points: ')) # Taking input
list_points = []
print()

for i in range(1, points+1):
      point = eval(input(f'Enter point {i}: ')) # Coordinates for each point
      list_points.append(point)
      
total_dist = 0

for j in range(points-1):
      dist = points_distance(list_points[j], list_points[j+1])    # Usinf function
      total_dist += dist
      
print(f'\nThe total distance between these points: {total_dist:.3f} units.')
