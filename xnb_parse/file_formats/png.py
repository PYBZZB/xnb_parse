"""
PNG encoder
"""

import struct
import zlib


class PyPngWriter(object):
    # The PNG signature.
    # http://www.w3.org/TR/PNG/#5PNG-file-signature
    _SIGNATURE = struct.pack('8B', 137, 80, 78, 71, 13, 10, 26, 10)

    def __init__(self, width=None, height=None):
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be greater than zero")

        # http://www.w3.org/TR/PNG/#7Integers-and-byte-order
        if width > 2 ** 32 - 1 or height > 2 ** 32 - 1:
            raise ValueError("width and height cannot exceed 2**32-1")

        self.width = width
        self.height = height
        self.chunk_limit = 2 ** 20

        self.color_type = 6
        self.planes = 4
        self.stride = self.width * self.planes

    def write_bytearray(self, outfile, rows, alpha='yes'):
        if alpha not in ('yes', 'no', 'only'):
            raise ValueError("Invalid alpha parameter: '%s'", alpha)

        # http://www.w3.org/TR/PNG/#5PNG-file-signature
        outfile.write(PyPngWriter._SIGNATURE)

        # http://www.w3.org/TR/PNG/#11IHDR
        PyPngWriter._write_chunk(outfile, 'IHDR', struct.pack("!2I5B", self.width, self.height, 8, self.color_type, 0,
                                                              0, 0))

        # http://www.w3.org/TR/PNG/#11IDAT
        compressor = zlib.compressobj()

        full_row_ff = [0xff] * self.width
        data = bytearray()
        for row in rows:
            data.append(0)
            if alpha == 'no':
                row[3::4] = full_row_ff
            elif alpha == 'only':
                row[0::4] = full_row_ff
                row[1::4] = full_row_ff
                row[2::4] = full_row_ff
            data.extend(row)
            if len(data) > self.chunk_limit:
                compressed = compressor.compress(str(data))
                if len(compressed):
                    PyPngWriter._write_chunk(outfile, 'IDAT', compressed)
                data = bytearray()
        if len(data):
            compressed = compressor.compress(str(data))
        else:
            compressed = bytearray()
        flushed = compressor.flush()
        if len(compressed) or len(flushed):
            PyPngWriter._write_chunk(outfile, 'IDAT', str(compressed + flushed))

        # http://www.w3.org/TR/PNG/#11IEND
        PyPngWriter._write_chunk(outfile, 'IEND')

    @staticmethod
    def _write_chunk(outfile, tag, data=''):
        # http://www.w3.org/TR/PNG/#5Chunk-layout
        outfile.write(struct.pack("!I", len(data)))
        outfile.write(tag)
        outfile.write(data)
        checksum = zlib.crc32(tag)
        checksum = zlib.crc32(data, checksum)
        checksum &= 2 ** 32 - 1
        outfile.write(struct.pack("!I", checksum))


def write_png(filename, width, height, rows, alpha='yes'):
    out_png = PyPngWriter(width=width, height=height)
    with open(filename, 'wb') as out_handle:
        out_png.write_bytearray(out_handle, rows, alpha)