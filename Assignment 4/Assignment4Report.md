# Assigment 4 Report

## Easycrackme1

### Solution

- The main function prompts the user to input a password and compares it to the hardcoded password FIRST_PASSWORD which is picklecucumberl337.
- It prints a message based on whether the input matches the hardcoded password.
- The getinput function reads input from stdin, calculates the length, null-terminates the string, and updates the length parameter.

### Keygen
echo "picklecucumberl337" | ./easy_crackme_1

## Easycrackme2

### Solution 

- The main function prompts the user to input a password and compares it to the hardcoded password FIRST_PASSWORD which is "artificialtree".
- It prints a message based on whether the input matches the hardcoded password.
- The getinput function reads input from stdin, calculates the length, null-terminates the string, and updates the length parameter.

### Keygen
echo "artificialtree" | ./easy_crackme_2

## Easycrackme3

### Solution
- The main function initializes variables, prompts for password, and compares against hardcoded passwords FIRST_PASSWORD1 and FIRST_PASSWORD2.
- It checks if the input matches either password individually or the concatenated password.
- Based on comparison and length, it determines if the password is correct, adjusting length as needed.
- Provides feedback to user based on validation result.
- Frees memory and checks stack canary to avoid issues.
- Returns boolean indicating whether validation succeeded.
- Password: "strawberrykiwi"

### Keygen 
echo "strawberrykiwi" | ./easy_crackme_3

## Control_flow_1
### Solution
- To solve, must reach win function based on function call graph.
- Route is Main → rock → paper → scissor → lizard → spock → win
- To reach the rock function from main function, the length of  the key has to be greater or equal to 16.
- To reach paper function from rock function, the 3rd index which is the 4th character of the key has to be “2”.
- To reach scissor function from paper function, we have to ensure (uVar1 & 1) != 0 which means (uVar1 & 1) == 1. To achieve that uVar1 has to equal to 1 which means 1L << ((byte)((int)param_1[7] - 0x25U) & 0x3f) has to equal to 1. So ((byte)((int)param_1[7] - 0x25U) & 0x3f) has to equal to 0. That means ((byte)((int)param_1[7] - 0x25U) has to equal to 0. To achieve that (int)param_1[7] equals to 0x25U which is “%”. So to reach scissor function, the 8th character of the key will have to be “%”.
- To reach lizard function from scissor function, iVar1 which is the first character of the key has to equal to 0x41 which is “A”. So first character of the key is “A”.
- To reach spock function from lizard function, the second character has to equal to 0x36 which is “6”.
- And to reach the win function, param_1 + 0xf which means the 16th character has to equal to 0x2a which is “*”.
### Key rules
- Length >= 16
- 4th char is "2"
- 8th char is "%"
- 1st char is "A"
- 2nd char is "6"
- 16th char is "*"

### Keygen1.py
```
import random
import string

def generate_key():
  key = ['A', '6']

  while len(key) < 16: 
    key.append(random.choice(string.ascii_letters + string.digits))

  key[3] = '2'
  key[7] = '%' 
  key[15] = '*'
  
  return ''.join(key)

print("Generated key:", generate_key())
```
## Control_flow_2
### Solution
-  I found that to solve the problem, we have to reach win function
-  Route is Main → rock → paper → scissor → lizard → spock → win
-  To reach rock from main function, the input key will have to have at least 16 characters.
- To reach paper function from rock function, key + 6 which is the 7th character has to be “Y”.
- To reach scissor function from paper function, same as control_flow_1, we have to make sure uVar1 = 0 so that uVar2 = 1 then (uVar2 & 1) != 0. In order for uVar1 = 0, (int*)(char *)(param_1 + 8) - 0x23 - 0. That means (param_1 + 8) which is the 9th character has to be equal to 0x23 which is “#”.
- To reach lizard function from scissor function, param_1 + 10 has to be equal to 0x41. That means 11th character has to be “A”.
- To reach spock function from lizard function, param_1 + 0xd which is param_1 + 13, 14th character equal to 0x36 which is “6”.
- And to reach win function, param_1 + 0xb which is param_1 + 11, 12th character will have to be 0x2a which is “*”.

### Key rules
- Length >= 16
- 7th char is "Y"
- 9th char is "#"
- 11th char is "A"
- 14th char is "6"
- 12th char is "*"

### Keygen2.py
```
import random
import string

def generate_key():
  key = []
  while len(key) < 16:
    key.append(random.choice(string.ascii_letters + string.digits))

  key[6] = 'Y' 
  key[8] = '#'
  key[10] = 'A'
  key[13] = '6'
  key[11] = '*'
  
  return ''.join(key)
  
print("Generated key:", generate_key())
```



