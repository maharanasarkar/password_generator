# Random Password Generator

This is a simple Python script that generates a random password by combining lowercase letters, uppercase letters, numbers, and special characters.

## Usage

To generate a random password, simply run the `GeneratePassword()` function from the provided script.

```python
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
sp_char = "!@#$%^&*()<>?:;"

def GeneratePassword():
    string = lower + upper + number + sp_char
    length = 25
    password = "".join(random.sample(string, length))
    print(password)

GeneratePassword()
```

## Customization
If you want to customize the length of the generated password or the character sets used, you can modify the length variable and the lower, upper, number, and sp_char strings accordingly.

```
# Example: Customize password length
length = 16
```
