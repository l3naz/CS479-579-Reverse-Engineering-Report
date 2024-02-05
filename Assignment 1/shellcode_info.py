# shellcode_info.py

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 shellcode_info.py <shellcode_file>")
        sys.exit(1)

    shellcode_file_path = sys.argv[1]

    try:
        with open(shellcode_file_path, 'rb') as file:
            shellcode_bytes = file.read()

        size = len(shellcode_bytes)

        print(f"My shellcode is {size} bytes long.")
        print("Here they are: --", end=" ")

        for byte in shellcode_bytes:
            print(f"{byte:02X}", end=" ")

        print("\nASCII representation:", shellcode_bytes.decode('utf-8', 'replace'))

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
