def lfsr16bit(start_state=0xACE1):
    lfsr = start_state
    bit = 0
    period = 0
    run = True
    while run:
        bit = (lfsr >> 0) ^ (lfsr >> 2) ^ (lfsr >> 3) ^ (lfsr >> 5) & 0xFFFF
        lfsr = (lfsr >> 1) | (bit << 15) & 0xFFFF
        period += 1
        print(period, hex(lfsr), hex(bit))
        run = lfsr != start_state
    return period


print(lfsr16bit())
