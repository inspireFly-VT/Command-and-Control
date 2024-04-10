import binascii
crctest = 0x1D0F
datatest = bytes('123456789', 'UTF-8')
print(datatest)

def calc(crc, data: bytes) -> int:
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x8000:
                crc <<= 1
                crc ^= 0x1021
            else:
                crc >>= 1
    return crc

print(hex(binascii.crc_hqx(datatest, crctest)))

# placeholder = calc(crctest, datatest)
# print(hex(placeholder))