# 15_is_teenager.py

def is_teenager(age):
    if type(age) != int:
        raise ValueError('Age must be in numbers')
    elif 12 <= age <= 17:
        return True
    elif 17 < age < 12:
        return False