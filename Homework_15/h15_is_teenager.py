# 15_is_teenager.py

def is_teenager(age):
    if type(age) != int:
        raise ValueError('Age must be in numbers')
    elif age >= 12 and age <= 17:
        return True
    elif age <= 12 or age >= 17:
        return False

print(is_teenager(90))