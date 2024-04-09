# Homework 6 Report

## Crackme5 solution
To solve this crackme, we need to enter the proper Serial Number. To do that, I need to first load the crackme into Ghidra, analyze the overall program flow.
Then I analyzed some of the subroutines function to understand the meaning of them and the Serial Number rule. Then Finally create a keygen.

### My solution is
```
import string
import random

class NoChoices(Exception):
    pass

def random_serial():
    def random_crit(crit, valid_chars):
        candidates = list(filter(crit, valid_chars))  # Convert filter object to list
        if len(candidates) == 0:
            raise NoChoices("Can't satisfy {}".format(repr(crit)))
        return random.choice(candidates)

    ## Rock
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    minus = '-'
    valid_chars = [ord(o) for o in lowercase + uppercase + digits + minus]
    serial = [random.choice(valid_chars) for i in range(19)]

    ## Paper
    serial[8] = random_crit(lambda x: (x^serial[10]) <= 9, valid_chars)
    serial[5] = random_crit(lambda x: (x^serial[13]) <= 9, valid_chars)
    t1 = (serial[8] ^ serial[10]) + 48
    serial[3] = t1
    serial[15] = t1 
    t2 = (serial[5] ^ serial[13]) + 48
    serial[0] = t2 
    serial[18] = t2 

    ## Scissors
    serial[1] = random_crit(lambda x: x + serial[2] > 170, valid_chars)
    serial[16] = random_crit(lambda x: x + serial[17] > 170 and 
            serial[1] + serial[2] != x + serial[17],
            valid_chars)

    ## Cracker
    serial[4], serial[9], serial[14] = 45,45,45 

    return "".join([chr(c) for c in serial])

def create_serial():
    while True:
        try:
            return random_serial()
        except NoChoices:
            pass

print(create_serial())
```

### How I did it using Ghidra
Analyzing all the subroutines function like "Rock", "Paper", "Scissors", "Cracker" the rule of the Serial Key is
The serial key must be 19 characters long. 
The serial key must contain hyphens ('-') at positions 5, 10, and 15.
Position 1 is determined by performing an XOR operation between characters at positions 14 and 6, then adding 48 to the result.
Position 4 is determined by performing an XOR operation between characters at positions 11 and 9, then adding 48 to the result.
Position 16 is determined by performing an XOR operation between characters at positions 11 and 9, then adding 48 to the result.
Position 19 is determined by performing an XOR operation between characters at positions 14 and 6, then adding 48 to the result.

![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/7b2176c6-26e7-4cb2-9289-d7a6abf66a86)
![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/3916ce6d-f381-45f9-b546-ffc1d9a2090b)
![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/9c0b11bc-3c62-4a50-94c5-cc043322062c)
![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/51f73f48-a053-4c0d-a18f-403a8359acb9)
![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/85f5e1a9-9422-4374-816b-8345de5921da)
![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/04668268-ee7c-49e4-99be-38a3315c4e33)

## Crackme1 solution
To solve this crackme, we need to enter a correct username and serial pairs. To do that, I needed to understand the logic the program uses to validate serial numbers. Then create a keygen so that 
the keygen script generates a username and a correct corresponding 'serial number'.

### My solution is
```
import string
import random

def generate_username(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def transform_username(username):
    transformed = ''
    transformed_ascii = []
    for i, char in enumerate(username):
        if i % 2 == 0:
            transformed += char.lower()
            transformed_ascii.append(ord(char.lower()))
        else:
            transformed += char.upper()
            transformed_ascii.append(ord(char.upper()))
    return transformed, transformed_ascii

def generate_serial(transformed_ascii):
    transformed_string = ''.join(str(x) for x in transformed_ascii)
    return transformed_string[(len(transformed_ascii)-8)*2:(len(transformed_ascii)-8)*2 +8]

def main():
    username_length = random.randint(8, 12)
    username = generate_username(username_length)
    transformed_username, transformed_ascii = transform_username(username)
      
    serial = generate_serial(transformed_ascii)

    print("Generated Username:", username)
    print("Transformed Username:", transformed_username)
    print("Generated Serial:", serial)

if __name__ == "__main__":
    main()

```


### How I did it using Ghidra
After analyzing the main function this is what I found
It prompts the user to enter a username, which must be between 8 and 12 characters long. If the username does not meet this requirement, it will keep asking the user to enter a valid username.
After accepting a valid username, it prompts the user to enter a serial number.
It then creates a new string by alternating the case of each character in the username (uppercase for odd positions, lowercase for even positions).
The program then extracts a substring from the entered serial number. The length of this substring is determined by the length of the username minus 8, multiplied by 2.
It converts this substring to an integer value and compares it with the entered serial number. If they match, it prints "s/n OK!", otherwise, it prints "s/n WRONG!".

![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/e15b0087-b76f-4b91-8b02-149621c42b8b)

![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/1a7208b3-e6da-4fe2-8ead-2fa55f78ff5e)

![image](https://github.com/l3naz/CS479-579-Reverse-Engineering-Report/assets/122416778/c1a75d1b-81d6-480d-8206-7f28546770ed)








