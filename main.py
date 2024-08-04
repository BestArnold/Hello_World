from pathlib import Path
"""
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string =''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi")
else:
    print("Your birthday does not appear in the first million digits of pi")

print(len(pi_string))
"""
path = Path('programming.txt')
path.write_text("I love python")