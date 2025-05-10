import math
import scipy.special as sp


def frequency_bit_test(data: str) -> float:
    stat = (data.count("1") - data.count("0")) / math.sqrt(len(data))
    p_value = math.erfc(abs(stat) / math.sqrt(2))
    return p_value


def identical_consecutive_bit_test(binary_str: str) -> float:
    n = len(binary_str)
    zeta = binary_str.count("1") / n
    if not (abs(zeta - 0.5) < (2 / math.sqrt(n))):
        return 0
    v_n = 0
    for i in range(n - 1):
        if binary_str[i] != binary_str[i + 1]:
            v_n += 1
    p_value = math.erfc(abs(v_n - 2 * n * zeta * (1 - zeta)) / (2 * math.sqrt(2 * n) * zeta * (1 - zeta)))
    return p_value


def longest_sequence_in_block(binary_str: str) -> float:
    blocks = []
    for i in range(0, len(binary_str), 8):
        block = binary_str[i: i + 8]
        blocks.append(block)
    v = [0, 0, 0, 0]
    p = [0.2148, 0.3672, 0.2305, 0.1875]
    for block in blocks:
        max_run = 0
        cur_len = 0
        for j in block:
            if j == "1":
                cur_len += 1
                max_run = max(max_run, cur_len)
            else:
                cur_len = 0
        match max_run:
            case max_run if max_run <= 1: v[0] += 1
            case 2: v[1] += 1
            case 3: v[2] += 1
            case max_run if max_run >= 4: v[3] += 1
    chi2 = sum(((v[i] - 16 * p[i]) ** 2) / (16 * p[i]) for i in range(len(v)))
    p_value = sp.gammainc((3 / 2), (chi2 / 2))
    return p_value
