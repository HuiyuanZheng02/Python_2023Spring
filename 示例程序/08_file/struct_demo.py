import struct

def pack1():
    i, f, b, s = 1234567, 3.14, True, 'python程序设计'
    s2 = s.encode()
    s2_len = len(s2)
    packed_buffer = struct.pack(f'if?h{s2_len}s', i, f, b, s2_len, s2)
    return packed_buffer

def pack2():
    # 下面给出了pack_into的版本，注意由于short要求出现在2的倍数的地址边界， if?h相当于if?xh
    i, f, b, s = 1234567, 3.14, True, 'python程序设计'
    s2 = s.encode()
    s2_len = len(s2)
    buffer = bytearray(struct.calcsize('if?h') + s2_len)
    struct.pack_into('if?x', buffer, 0, i, f, b)
    struct.pack_into(f'h{s2_len}s', buffer, struct.calcsize('if?x'), s2_len, s2)
    return buffer

def unpack(buffer):
    offset = struct.calcsize('if?h')
    values = struct.unpack('if?h', buffer[:offset])
    print(*values)

    s = struct.unpack_from(f'{values[-1]}s', buffer, offset)
    print(s[0].decode())


if __name__ == '__main__':
    buffer = pack1()
    print(buffer)
    unpack(buffer)

    print()
    buffer = pack2()
    print(buffer)
    unpack(buffer)
