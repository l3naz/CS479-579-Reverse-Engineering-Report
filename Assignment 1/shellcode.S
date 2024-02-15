.section .text
.globl _start

_start:
    # Set rax to 59 (sys_execve)
    xorq    %rax, %rax
    movb    $59, %al               # Syscall number 59 (execve)

    # Set rdi to point to '/bin/sh' string
    xorq    %rdi, %rdi
    movq    $0x68732f6e69622f, %rdi  # '/bin/sh' in little-endian

    # Set rsi to null
    xorq    %rsi, %rsi

    # Set rdx to null
    xorq    %rdx, %rdx

    # Call execve
    syscall

    # Exit
    xorq    %rax, %rax
    incq    %rax                     # syscall number 60 (exit)
    xorq    %rdi, %rdi                # status code 0
    syscall

