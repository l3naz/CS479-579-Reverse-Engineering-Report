all: shellcode.S shellcode_tester.c
	gcc -m32 shellcode_tester.c -o shellcode_test -z execstack -no-pie
	as --32 shellcode.S -o shellcode.o
	ld -m elf_i386 shellcode.o -o shellcode --oformat=binary
	rm shellcode.o
	python3 x_shellcode.py

.PHONY:	info

info:
	python3 shellcode_info.py shellcode.S
