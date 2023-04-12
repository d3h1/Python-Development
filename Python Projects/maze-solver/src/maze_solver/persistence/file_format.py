import array
import struct
from dataclasses import dataclass
from typing import BinaryIO

MAGIC_NUMBER: bytes = b'MAZE'

@dataclass(frozen=True)
class FileHeader:
    format_version: int
    width: int
    height: int

    # Reads number of bytes equal to length of magic number
    @classmethod
    def read(cls, file: BinaryIO) -> 'FileHeader':
        assert (
            file.read(len(MAGIC_NUMBER)) == MAGIC__NUMBER
        ), 'Unknown file type'
        # !Reads a single unassigned byte and assigns the result to a local variable with the file format version
        format_version, = struct.unpack("B", file.read(1))
        width, height = struct.unpack("<2I", file.read(2 * 4))
        return cls(format_version, width, height)
    
    # Writing files using B
    def write(self, file: BinaryIO) -> None:
        file.write(MAGIC_NUMBER)
        file.write(struct.pack("B", self.format_version))
        file.write(struct.pack("<2I", self.width, self.height))

@dataclass(frozen=True)
class FileBody:
    square_values: array.array
    
    @classmethod
    def read(cls, header: FileHeader, file: BinaryIO) -> "FileBody":
        return cls(
            array.array("B", file.read(header.width * header.height))
        )
    
    # Using numbers stored in the array to create borders and roles
    def write(self, file: BinaryIO) -> None:
        file.write(self.square_values.tobytes())