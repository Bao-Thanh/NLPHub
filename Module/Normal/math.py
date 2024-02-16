import numpy as np
import math

def calculator(numbers, sign):
    
    nums = np.array(numbers, dtype=float)
    
    def add():
        return np.sum(nums)

    def subtract():
        return np.subtract.reduce(nums)

    def multiply():
        return np.multiply.reduce(nums)

    def divide():
        return np.divide.reduce(nums)

    def find_max():
        return max(nums)

    def find_min():
        return min(nums)

    def calculate_total():
        return len(nums)

    def calculate_average():
        return np.average(nums)

    def calculate_median():
        return np.median(nums)

    def calculate_pow():
        return math.pow(nums[0], nums[1])

    def calculate_log():
        return math.log(nums[1], nums[0])

    def calculate_base():
        decimal_number = int(str(int(nums[0])), int(nums[1]))
        result = np.base_repr(decimal_number, base=int(nums[2]))
        return result

    def calculate_rad():
        return nums[0] % nums[1]

    def calculate_percentage():
        return (nums[0] * 100) // nums[1]

    def calculate_sqrt():
        return math.sqrt(nums[0])

    def calculate_round():
        return round(nums[0], int(nums[1]))

    def calculate_abs():
        return abs(nums[0])

    def find_big():
        return nums[0] if (nums[0] > nums[1]) else nums[1]

    def find_small():
        return nums[0] if (nums[0] < nums[1]) else nums[1]

    def compare_less():
        return [x for x in nums if x < nums[0]]

    def compare_less_equal():
        return [x for x in nums if x <= nums[0]]

    def compare_greater():
        return [x for x in nums if x > nums[0]]

    def compare_greater_equal():
        return [x for x in nums if x >= nums[0]]

    def compare_equal():
        return [x for x in nums if x == nums[0]]

    switch_dict = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "max": find_max,
        "min": find_min,
        "total": calculate_total,
        "average": calculate_average,
        "median": calculate_median,
        "pow": calculate_pow,
        "log": calculate_log,
        "base": calculate_base,
        "rad": calculate_rad,
        "%": calculate_percentage,
        "sqrt": calculate_sqrt,
        "round": calculate_round,
        "abs": calculate_abs,
        "big": find_big,
        "small": find_small,
        "<": compare_less,
        "<=": compare_less_equal,
        ">": compare_greater,
        ">=": compare_greater_equal,
        "=": compare_equal
    }

    return switch_dict.get(sign, lambda: "Invalid sign")()
