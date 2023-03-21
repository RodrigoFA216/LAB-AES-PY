import math


def neuron_activ(w1, w2, x1, x2, theta, gate):
    data = [[x1[0], x2[0]], [x1[1], x2[1]], [x1[2], x2[2]], [x1[3], x2[3]]]
    results = []
    expected = []
    if gate == 'and':
        expected = [-1, -1, -1, 1]
    elif gate == 'or':
        expected = [-1, 1, 1, 1]
    elif gate == 'nand':
        expected = [1, 1, 1, -1]
    elif gate == 'nor':
        expected = [-1, 1, 1, -1]
    for element in data:
        X1 = float(element[0])
        X2 = float(element[1])
        z = (w1 * X1) + (w2 * X2) - theta
        y = 1 / (1+math.exp(-z))
        if (y >= 1):
            results.append(1)
        else:
            results.append(-1)
    res = compare_lists(expected, results)
    if res:
        return {"result": True, "values": results}
    else:
        return {"result": False, "values": None}


def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True
