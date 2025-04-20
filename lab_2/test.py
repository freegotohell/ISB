import math


def frequency_bit_test(data: str) -> float:
    stat = (data.count("1") - data.count("0")) / math.sqrt(len(data))
    p_value = math.erfc(abs(stat) / math.sqrt(2))
    return p_value

