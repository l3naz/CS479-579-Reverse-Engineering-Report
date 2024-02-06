.section .text
.globl _start
_start:
    xorl %eax, %eax            # Clear %eax register
    mov $59, %eax              # syscall number for execve (59 in 64-bit)
    lea shell_path(%rip), %rdi # address of "/bin/sh" (using RIP-relative addressing)
    xorl %esi, %esi            # null for command-line arguments
    xorl %edx, %edx            # null for environment variables
    syscall                    # Invoke execve syscall

    xorl %edi, %edi            # Clear %edi register (exit status)
    mov $60, %eax              # syscall number for exit (60 in 64-bit)
    syscall                    # Invoke exit syscall

.section .data
shell_path: .asciz "/bin/sh"
