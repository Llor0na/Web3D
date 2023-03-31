import struct

def read_c_string(file):
    """Read a null-terminated string from a file"""
    string = bytearray()
    while True:
        char = file.read(1)
        if char == b'\0':
            break
        string += char
    return string.decode()

def get_file_size(file):
    """Get the size of a file in bytes"""
    current_position = file.tell()
    file.seek(0, 2)
    size = file.tell()
    file.seek(current_position, 0)
    return size

try:
    with open("scene.mview", 'rb') as file:
        end = get_file_size(file)
        while file.tell() < end:
            name = read_c_string(file)
            mime = read_c_string(file)
            compressed, size, raw_size = struct.unpack("III", file.read(3*4))
            print("Name: {}\nMIME type: {}\nCompressed: {}\nSize: {}\nRaw size: {}".format(name, mime, bool(compressed & 1), hex(size), hex(raw_size)))
            if file.tell() + size >= end:
                break
            file.seek(size, 1)
except FileNotFoundError:
    print("The file 'scene.mview' could not be found.")
except Exception as e:
    print("An error occurred: {}".format(e))
