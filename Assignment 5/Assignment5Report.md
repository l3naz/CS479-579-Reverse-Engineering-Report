# Assignment 5 Report

## Ransomware1

### To decrypt important.docx

I see it use STRCMP to compare user input with variable FIRST_PASSWORD which I found has a value: "lumpy_cactus_fruit".
I tried to execute the ransom and enter it as a password, it successfully decrypted important.docx.

#### Fuction on ghidra with human-readble variables:
![Screenshot from 2024-03-18 14-53-27](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/f8387742-c3db-43b4-82b4-4d3890cc3ab2)

### To decrypt secret.txt

#### My decrypt.py:
```
#!/usr/bin/env python3

import sys

if (len(sys.argv) != 3):
	print("Usage:  decrypt1.py INFILE OUTFILENAME")

infile = sys.argv[1]
outfile = sys.argv[2]
key = ord('4')

with open(infile, "rb") as inf:
	with open(outfile, "wb") as ouf:

		contents = inf.read()
		
		for b in contents:
			ouf.write((b ^ key).to_bytes(1, "big"))
```

#### How it works?
The program checks if the correct number of command-line arguments (input file and output file) are provided.
It stores the input file name and output file name in the variables infile and outfile, respectively.
It sets the XOR key to the ASCII value of the character '4', which is 52 (decimal).
It opens the input file in binary read mode using open(infile, "rb").
It opens the output file in binary write mode using open(outfile, "wb").
It reads the entire contents of the input file into memory using contents = inf.read().
It loops through each byte b in the contents.
For each byte b, it XORs it with the key using b ^ key.
The result of the XOR operation is converted to a byte string using (b ^ key).to_bytes(1, "big").
The decrypted byte string is written to the output file using ouf.write(...).
So, this program simply reads an encrypted file, XORs each byte with the key '4', and writes the decrypted bytes to the output file.



#### Decrypt function on ghidra with human-redable variables
![Screenshot from 2024-03-18 15-51-10](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/521a2b91-0406-44e2-98f8-6e6d3041525d)

## Ransomware2

### Decrypt important.docx

I see it use STRCMP to compare user input with variable FIRST_PASSWORD which I found has a value: "delicious".
 execute the ransom and enter it as a password, it successfully decrypted important.docx.
 
#### Function on Ghidra with human-readable variables
![Screenshot from 2024-03-18 15-43-37](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/26d9ef75-de1e-4138-b551-d536e63b004a)

### Decrypt secret.txt

#### My decrypt.py
```
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
```

#### How it works?
The program defines a function decrypt_file that takes two arguments: the input file and the output file.
Inside the decrypt_file function, it sets the XOR key to the bytes b"1337".
It opens the input file in binary read mode using open(infile, "rb").
It reads the entire contents of the input file into memory using encrypted_data = inf.read().
It creates an empty bytearray decrypted_data to store the decrypted data.
It loops through each byte byte in the encrypted_data using enumerate(encrypted_data), which also provides the index i.
For each byte byte, it gets the corresponding byte from the XOR key using xor_key[i % len(xor_key)]. This ensures that the key is repeated if the encrypted data is longer than the key.
It XORs the byte byte with the key byte key_byte using decrypted_byte = byte ^ key_byte.
The decrypted byte decrypted_byte is appended to the decrypted_data bytearray using decrypted_data.append(decrypted_byte).
After processing all bytes, it opens the output file in binary write mode using open(outfile, "wb").
It writes the decrypted data from the decrypted_data bytearray to the output file using outf.write(decrypted_data).
The decrypt_file function is called from the if __name__ == "__main__" block, which checks if the correct number of command-line arguments (input file and output file) are provided.
So, this program reads an encrypted file, XORs each byte with the corresponding byte from the "1337" key (repeating the key if needed), and writes the decrypted bytes to the output file.

#### Decrypt functions on Ghidra with human-readable variables:
![Screenshot from 2024-03-18 22-56-11](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/171c6f2b-f954-4385-a9d2-4a4aa4189256)

![Screenshot from 2024-03-18 22-56-21](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/020f8df9-d1f7-4323-a7b8-da71291299bd)



