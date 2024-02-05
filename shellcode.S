.text
    .global _start
_start:
    xorl %eax, %eax
    movb $11, %al           # syscall number for execve
    leal shell_path, %ebx   # address of "/bin/sh"
    xorl %ecx, %ecx         # null for command-line arguments
    xorl %edx, %edx         # null for environment variables
    int $0x80

    xorl %eax, %eax
    inc %eax                # syscall number for exit
    int $0x80

.section .data
    shell_path: .asciz "/bin/sh"
