import math
import numpy as np


def _merge(array, left_index, right_index, middle):
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # We use the comparison_function instead of a simple comparison operator
        if left_copy[left_copy_index] < right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def _merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    _merge_sort(array, left_index, middle)
    _merge_sort(array, middle + 1, right_index)
    _merge(array, left_index, right_index, middle)

def calculate_percentile(array, percentile):
    '''
        Returns the percentile of given array

        :param list array:
            Specifies poolValues
        :param float percentile:
            Specifies input percentiles
    '''
    if len(array) < 100:
        # Sort array
        _merge_sort(array, 0, len(array)-1)

        # Find the percentile
        percentile_rank = percentile / 100 * (len(array)-1)
        index = math.floor(percentile_rank)
        weight = percentile_rank - index

        percentile_value = array[index] * (1 - weight) + array[index + 1] * weight
    else:
        percentile_value = np.percentile(array, percentile)

    return percentile_value
