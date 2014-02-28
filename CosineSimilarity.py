import math
from itertools import izip

def dotProduct(v1, v2):
    return sum(map(lambda x: x[0] * x[1], izip(v1, v2)))

def cosineMeasure(v1, v2):
    prod = dotProduct(v1, v2)
    len1 = math.sqrt(dotProduct(v1, v1))
    len2 = math.sqrt(dotProduct(v2, v2))
    return prod / (len1 * len2)

