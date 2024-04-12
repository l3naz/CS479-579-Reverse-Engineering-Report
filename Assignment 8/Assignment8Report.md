# Assignment 8

## OSINT
NjRAT is a Remote Access Trojan(RAT) which was created in June 2013. It is a kind of malicious software which can remotely access computers or devices. This device onto individuals attention due to its user-friendliness and a multiple functionalities which offer distant control over the victim’s computer. Consequently, cybercriminals can manage the infected systems by distance. The main distribution of it is associated with the Middle East, although the Syrian Electronic Army is thought to be its early distributer as well. Since the time it debuted, this drug has been observed spreading to different parts of the world as it has grown in its locality and across other countries. NjRAT is commonly spread through phishing, infection through a program or file, and even links shared on social media. It has been recognized as the main attack vector in many cases of computer data theft, system manipulation, and denial-of-service attacks.

Cite:
1. https://www.cyber.nj.gov/threat-landscape/malware/trojans/njrat
2. https://www.cynet.com/attack-techniques-hands-on/njrat-report-bladabindi/

## RegShot

After using RegShot to comparing before and after Malware executing, I can see that it add and changes multiple registry keys. The longer I let it executing, the more keys are added and modified. But what stands out to me are
`HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run\ecc7c8c51c0850c1ec247c7fd3602f20: ""C:\Users\User\AppData\Local\Temp\windows.exe" .."` and `HKU\S-1-5-21-2381349442-1145859609-3592442688-1000\Software\Microsoft\Windows\CurrentVersion\Run\ecc7c8c51c0850c1ec247c7fd3602f20: ""C:\Users\User\AppData\Local\Temp\windows.exe" .."`

![regshot2](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/08b9b751-2044-408a-ad10-2da253d7380f)

![regshot1](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/7260bdf9-56eb-44f5-840e-819e89230a9f)


I think that mean it's adding a key in the Run section of the registry. The Run section is often used for programs that are set to start when the operating system boots up. The key ecc7c8c51c0850c1ec247c7fd3602f20 that the malware has added will run the windows.exe file, which is located in the temp folder. And this is how NjRAT achieve persistence - by ensuring it's run each time the system is booted up.

![regshot3](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/49f3d47d-2947-4d34-a624-8d94f6b33f13)

Moreover, I identified that there are additional files in my C:/ drive, NJQ8.exe and njRAT.exe, was created by NjRAT

![regshot4](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/97692ab2-8b8a-4e65-a944-1433e26a5729)


## FakeNet

I open FakeNet, then NjRAT and let it run for 5 minutes. Deploying FakeNet revealed NjRAT attempting to connect to zaaptoo.zapto.org. A thorough examination identified zapto.org, a dynamic DNS service possibly housing the attacker, associated with IP 158.247.7.206. Though zapto.org maintains a variety of sub-domains, it may be an abuse of a legitimate domain by the NjRAT perpetrator. Tracking these unusual requests alongside other symptoms is crucial for diagnosing potential compromise and focusing on abnormal network behavior.

![FakeNet1](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/dc080810-9d90-48f5-93f5-432bdd29234c)
