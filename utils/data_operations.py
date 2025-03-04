import math

def euclidean_distance(x1, x2):
  #Euclidean distance between two points.
    distance = 0
    for i in range(len(x1)):
        distance += (x1[i] - x2[i]) ** 2
    return math.sqrt(distance)