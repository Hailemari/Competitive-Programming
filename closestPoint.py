#find the closest point(s) to the origin(0, 0) in a grid system
def kClosest(points, k):
    
    points.sort(key = lambda k: k[0]**2 + k[1]**2)
    return points[:k]