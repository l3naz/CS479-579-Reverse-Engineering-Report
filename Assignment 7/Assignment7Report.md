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
![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/6e2ac8eb-2efd-498a-a0ca-253b849e4de9)



## How often Malware act
The Malware acts every 60 seconds
![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/f8baf25c-3c57-4141-bb19-63cc0f90e319)


## What does malware do every loops
The Malware will create a Thread executing sprintf that print "_Practical_Malware_Analysis_1" "_Practical_Malware_Analysis_2" and move on
![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/7fd1c1c8-40d1-49eb-81ed-7c2f6ea5eb0a)
