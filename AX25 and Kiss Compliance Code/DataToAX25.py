import binascii

def encode_ax25_frame(data: bytes, dest_callsign: str, source_callsign: str) -> bytes:
    """
    Encodes a data payload into an AX.25 frame.

    Args:
        data (bytes): The data payload to be transmitted.
        dest_callsign (str): Destination callsign (6 characters).
        source_callsign (str): Source callsign (6 characters).

    Returns:
        bytes: The AX.25 frame.
    """
    # Start flag (0x7E)
    ax25_frame = b'\x7E'

    # Destination address (7 bytes)
    dest_address = f"{dest_callsign}"
    dest_address_bytes = bytes(dest_address, 'ascii')
    shifted_dest_address = bytes([byte << 1 for byte in dest_address_bytes])
    ax25_frame += shifted_dest_address
    ax25_frame += b'\x40'
    ax25_frame += b'\x61'

    # Source address (7 bytes)
    source_address = f"{source_callsign}"
    source_address_bytes = bytes(source_address, 'ascii')
    shifted_source_address = bytes([byte << 1 for byte in source_address_bytes])
    ax25_frame += shifted_source_address
    ax25_frame += b'\x40'
    ax25_frame += b'\x62'

    # Control field (0x03 for UI frames)
    ax25_frame += b'\x03'

    # Protocol ID (0xF0 for no layer 3 protocol)
    ax25_frame += b'\xF0'

    # Data payload
    ax25_frame += data

    # FCS (Frame Check Sequence) - Calculate CRC16 and append
    crc = calculate_crc16(ax25_frame)
    ax25_frame += crc.to_bytes(2, 'big')

    # End flag (0x7E)
    ax25_frame += b'\x7E'

    return ax25_frame

def calculate_crc16(data: bytes) -> int:
    """
    Calculates the CRC-16 (CCITT) checksum for the given data.

    Args:
        data (bytes): Data to compute the checksum for.

    Returns:
        int: CRC-16 value.
    """
    Init = 0x1D0F
    return binascii.crc_hqx(data, Init)

def decode_ax25_frame(frame):
    if len(frame) < 14:
        print("Invalid AX.25 frame")
        return

    # AX.25 frame structure:
    # Flag (1 byte) | Destination (7 bytes) | Source (7 bytes) | Control (1 byte) | Protocol ID (1 byte) | Data | FCS (2 bytes) | Flag (1 byte)

    flag1 = frame[:1]
    destination = frame[1:8]
    source = frame[8:15]
    control = frame[15:16]
    protocol_id = frame[16]
    data = frame[17:-3]  # Data field
    fcs = frame[-3:-1]  # Frame Check Sequence
    flag2 = frame[-1:]

    # Convert bytes to ASCII for destination and source addresses
    destination_address = ''.join(chr(byte >> 1) for byte in destination)
    source_address = ''.join(chr(byte >> 1) for byte in source)

    # Print decoded information
    print("Flag1:", flag1.hex())
    print("Destination Address:", destination_address)
    print("Source Address:", source_address)
    print("Control:", control.hex())
    print("Protocol ID:", hex(protocol_id))
    print("Data:", data.hex())
    print("FCS:", fcs.hex())
    print("Flag2:", flag2.hex())

# Example usage
data_payload = b"Hello, world!"
dest_callsign = "K4KDJ"
source_callsign = "K4KDJ"
ax25_frame = encode_ax25_frame(data_payload, dest_callsign, source_callsign)
print("AX.25 Frame:", ax25_frame.hex())
decode_ax25_frame(ax25_frame)