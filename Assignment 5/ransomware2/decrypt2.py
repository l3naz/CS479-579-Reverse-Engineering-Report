#!/usr/bin/env python3
import sys

def decrypt_file(infile, outfile):
    xor_key = b"1337"  # XOR key as bytes

    with open(infile, "rb") as inf:
        encrypted_data = inf.read()

    decrypted_data = bytearray()

    for i, byte in enumerate(encrypted_data):
        key_byte = xor_key[i % len(xor_key)]
        decrypted_byte = byte ^ key_byte
        decrypted_data.append(decrypted_byte)

    with open(outfile, "wb") as outf:
        outf.write(decrypted_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: decrypt.py INFILE OUTFILE")
        sys.exit(1)

    infile = sys.argv[1]
    outfile = sys.argv[2]

    decrypt_file(infile, outfile)
