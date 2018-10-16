#exercise from Kaggle's Python tutorial

def diamond(height):
    """Return a string resembling a diamond of specified height (measured in lines).
    height must be an even integer.
    """
    result = ''
    l, r = '/', '\\'
    for i in range(1,height + 1):
        if (i <= height/2):
            line = (i * l) + (i * r)
            result += line.center(height, ' ') + '\n'
        else:
            line = (height + 1 - i) * r + (height + 1 - i) * l
            result += line.center(height, ' ') + '\n'
    return result[:-1]

print(diamond(4))