# Assignment 7

## Prove that the loader is using DLL injection
The function loads several functions dynamically using LoadLibraryA and GetProcAddress. This dynamic loading of libraries and functions is a common technique used in DLL injection to gain access to functions required for injection and execution within a target process.
The function contains calls such as OpenProcess, VirtualAllocEx, WriteProcessMemory, and CreateRemoteThread. These are indicative of manipulating processes and memory in a remote process space, which is typical in DLL injection.

![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/f8cd7372-f195-4d64-b0f0-23ce506b035a)

## Injected Process
It seems that FUN_00401000 is looking to identify the process "explorer.exe" to possibly inject code into it. The process gets selected by:
1. Taking as input an identifier (likely Process ID).
2. Opening the process and querying its information.
3. Checking if the main module's name of this process is "explorer.exe" or not.
   
![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/ce523273-69f0-429e-8e2d-c698a2fdb9bc)

## Entry point of DLL injection


## How often Malware act


## What does malware do every loops
