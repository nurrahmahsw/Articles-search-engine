"""
author rochanaph
September 21 2017
"""
import math
def euclidean(vector1, vector2):
    """
    fungsi untuk menghitung jarak antara 2 vektor dengan rumus euclidean ddistance
    :param vector1: vektor 1
    :param vector2: vektor
    :return:
    """
    dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
    dist = math.sqrt(sum(dist))
    return dist

def cosine(vector1, vector2):
    """
    :param vector1:
    :param vector2:
    :return:
    """

    dot  = sum([a*b for a,b in zip(vector1, vector2)])
    mag1 = math.sqrt(sum([a**2 for a in vector1]))
    mag2 = math.sqrt(sum([a**2 for a in vector2]))
    return dot/(mag1*mag2)



p = [1,1,1,1,2,0,0]
q = [0,0,1,1,1,1,1]

# print euclidean(p,q)
# print cosine(p,q)

def manhattan_distance(vector1,vector2):
    return sum(abs(a-b) for a,b in zip(vector1,vector2))

def jaccard_similarity(vector1,vector2):
    intersection_cardinality = len(set.intersection(*[set(vector1),set(vector2)]))
    union_cardinality = len(set.union(*[set(vector1),set(vector2)]))
    return intersection_cardinality/float(union_cardinality)

    # Input: 2 objects
    # Output: Pearson Correlation Score
def pearson_correlation(object1, object2):
    values = range(len(object1))

    # Summation over all attributes for both objects
    sum_object1 = sum([float(object1[i]) for i in values])
    sum_object2 = sum([float(object2[i]) for i in values])

    # Sum the squares
    square_sum1 = sum([pow(object1[i], 2) for i in values])
    square_sum2 = sum([pow(object2[i], 2) for i in values])

    # Add up the products
    product = sum([object1[i] * object2[i] for i in values])

    # Calculate Pearson Correlation score
    numerator = product - (sum_object1 * sum_object2 / len(object1))
    denominator = ((square_sum1 - pow(sum_object1, 2) / len(object1)) * (square_sum2 -
                                                                         pow(sum_object2, 2) / len(object1))) ** 0.5

    # Can"t have division by 0
    if denominator == 0:
        return 0

    result = numerator / denominator
    return result
