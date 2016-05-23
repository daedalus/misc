get_bin = lambda x, n: format(x, 'b').zfill(n)

rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))
 
max_bits = 16  # For fun, try 2, 17 or other arbitrary (positive!) values
 
value = 0b0000001000000000
i = 1
max_bits = 16
print get_bin(value,max_bits)
print get_bin(rol(value, i, max_bits),max_bits)
print get_bin(ror(value, i, max_bits),max_bits)

