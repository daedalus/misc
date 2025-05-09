from copy import copy
import zlib
import sys

sys.set_int_max_str_digits(10000)

def readfile(filename):
  with open(filename,"rb") as fp:
    return fp.read()
   

from copy import copy

def encode_m1(data):
    """Returns indices of negative values in data."""
    return [i for i, x in enumerate(data) if x < 0]

def apply_m1_delta(delta, m1):
    """Applies sign inversion at specified indices."""
    delta2 = copy(delta)
    for i in m1:
        delta2[i] *= -1
    return delta2

def delta_encode(data):
    """Returns absolute deltas and the m1 sign index."""
    if not data:
        return [], []
    deltas = [data[0]]
    for i in range(1, len(data)):
        deltas.append(data[i] - data[i - 1])
    m1 = encode_m1(deltas)
    abs_deltas = [abs(x) for x in deltas]
    return abs_deltas, m1

def delta_decode(abs_deltas, m1):
    """Decodes absolute deltas with sign correction."""
    if not abs_deltas:
        return []
    corrected = apply_m1_delta(abs_deltas, m1)
    data = [corrected[0]]
    for i in range(1, len(corrected)):
        data.append(data[-1] + corrected[i])
    return data

from copy import copy

def encode_m1(data):
    """Returns indices of negative values in data."""
    return [i for i, x in enumerate(data) if x < 0]

def apply_m1_delta(delta, m1):
    """Applies sign inversion at specified indices."""
    delta2 = copy(delta)
    for i in m1:
        delta2[i] *= -1
    return delta2

def to_integer(digits, base):
    """Encodes a list of digits into a single integer in given base."""
    result = 0
    for d in digits:
        result = result * base + d
    return result

def from_integer(value, base, length):
    """Decodes a base-encoded integer back into a list of digits of given length."""
    digits = []
    for _ in range(length):
        digits.append(value % base)
        value //= base
    return list(reversed(digits))

def delta_encode_to_integers(data):
    """Encodes data into abs_deltas and m1 as integers."""
    if not data:
        return 0, 0, 1, 1, 0  # dummy values
    deltas = [data[0]]
    for i in range(1, len(data)):
        deltas.append(data[i] - data[i - 1])
    m1 = encode_m1(deltas)
    abs_deltas = [abs(x) for x in deltas]

    base_delta = max(abs_deltas) + 1
    base_m1 = (max(m1) + 1) if m1 else 1

    encoded_delta = to_integer(abs_deltas, base_delta)
    encoded_m1 = to_integer(m1, base_m1) if m1 else 0

    return encoded_delta, encoded_m1, base_delta, base_m1, len(data)

def delta_decode_from_integers(encoded_delta, encoded_m1, base_delta, base_m1, length):
    """Decodes data from encoded integers."""
    abs_deltas = from_integer(encoded_delta, base_delta, length)
    m1 = from_integer(encoded_m1, base_m1, len([i for i in abs_deltas if i != 0])) if encoded_m1 else []
    corrected = apply_m1_delta(abs_deltas, m1)
    data = [corrected[0]]
    for i in range(1, len(corrected)):
        data.append(data[-1] + corrected[i])
    return data



data = readfile(sys.argv[1])

encoded_delta, encoded_m1, base_d, base_m1, length = delta_encode_to_integers(data)
decoded = delta_decode_from_integers(encoded_delta, encoded_m1, base_d, base_m1, length)

def int_to_bytes(n):
    length = (n.bit_length() + 7) // 8 or 1
    return n.to_bytes(length, 'big')

def bytes_to_int(b):
    return int.from_bytes(b, 'big')

def write_encoded_to_file(filename, encoded_delta, encoded_m1):
    delta_bytes = int_to_bytes(encoded_delta)
    m1_bytes = int_to_bytes(encoded_m1)

    with open(filename, 'wb') as f:
        # Write lengths first so you can parse later
        f.write(len(delta_bytes).to_bytes(2, 'big'))  # 2 bytes = max 65535
        f.write(len(m1_bytes).to_bytes(2, 'big'))
        f.write(delta_bytes)
        f.write(m1_bytes)




write_encoded_to_file("delta.bin",encoded_delta,encoded_m1)

