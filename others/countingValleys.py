def countingValleys(n, paths):
    height = valley = 0

    for path in paths:
        if path == 'U':
            height += 1
        else:
            height -= 1
        
        if path == 'U' and height == 0:
            valley += 1
    
    return valley