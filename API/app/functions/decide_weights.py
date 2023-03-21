import math
import numpy as np


def appropiate_weight(w1, w2, x1, x2, theta, gate):
    # hacemos la primer ronda de cálculos
    y_pred = calculate_predictions(w1, w2, x1, x2, theta)
    # establecemos la y esperada
    if gate == 'and':
        y_waited = [-1, -1, -1, 1]
    elif gate == 'or':
        y_waited = [-1, 1, 1, 1]
    elif gate == 'nand':
        y_waited = [1, 1, 1, -1]
    elif gate == 'nor':
        y_waited = [-1, 1, 1, -1]
    # comparamos que y_waited == y_pred
    for i in range(len(y_waited)):  # y_waited eras
        for i in range(len(y_waited)):  # y_waited veces
            res = False
            while not res:
                res = compare_lists(y_pred, y_waited)


def calculate_predictions(w1, w2, x1, x2, theta):
    y_pred = []
    for i in range(size(x1)):
        y_acum = (w1*x1[i]) + (w2*x2[i]) - theta
        if y_acum >= 1:
            y_pred.append(1)
        else:
            y_pred.append(-1)
    return y_pred


def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True
