# CS479/579 Reverse Engineering at NMSU

## Summary
This repository holds reports on reverse engineering malware samples from "Practical Malware Analysis."

## System Setup

### Step 1: Download and Install VirtualBox
Download VirtualBox from [here](https://www.virtualbox.org/) and follow the installation instructions.

### Step 2: Download Windows 11 OS ISO
Download the Windows 11 ISO from an official source.

### Step 3: Install Windows 11 on VirtualBox
Open VirtualBox, create a new VM, and install Windows 11 using the downloaded ISO. Ensure proper configuration for your virtual machine.

### Step 4: Install IDE & C/C++ Compiler
Install your preferred Integrated Development Environment (IDE) and a C/C++ compiler for programming tasks.

### Step 5: Install IDA Education
Download and install IDA Education from the provided link.

### Step 6: Network Isolation
1. In the network settings of the VM, create a new "VirtualBox Host-only Ethernet Adapter."
2. Change the IPv4 to "10.0.0.1" (ensure it is different from the physical host IP address).
3. Set the subnet mask to 255.255.255.0.
4. Change the network settings of the VM to "host-only" and choose the adapter that you created earlier

### Step 7: Create Snapshot
Create a snapshot of your VM to easily revert to a known state if needed.

### Step 8: Disable Windows Defender
1. Select Start and type "Windows Security" to search for the app.
2. Open the Windows Security app, go to Virus & threat protection.
3. Under Virus & threat protection settings, select Manage settings.
4. Switch Real-time protection to Off.

### Step 8a: Permanently Disable Windows Defender
1. Select Start and type "Run"
2. In Run prompt type "gpedit.msc" then click "OK"
3. Click "Computer Configuration" -> "Administrative Templates" -> "Windows Components"
4. On right side, scroll down and click "Windows Defender Antivirus" -> "Real-Time Protection"
5. Double click on "Turn off real-time protection"
6. Select "Enable" then "Apply", "OK"

### Step 9: Install Flare VM
Follow the installation instructions provided [here](https://github.com/mandiant/flare-vm) to install Flare VM.


