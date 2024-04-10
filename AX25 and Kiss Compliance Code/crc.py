crctest = 0x1D0F
datatest = bytes('Hello', 'UTF-8')
print(datatest)

def calculate_crc16(data: bytes) -> int:
    crc = 0x1D0F #CCITT-False is 0xFFFF, 
    poly = 0x1021  # CRC-CCITT polynomial


    for byte in data:
        crc ^= (byte << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1
            crc &= 0xFFFF  # Limit to 16 bits

    return crc

print(hex(calculate_crc16(datatest)))
