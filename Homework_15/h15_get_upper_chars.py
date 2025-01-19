# h15_get_upper_chars.py

def get_upper_chars(text: str):
    uppers = ''
    for i in text:
        x = i.capitalize()
        if i == x:
            uppers += i
    if uppers:
        return uppers
    else:
        return False

print(get_upper_chars('loremipsum'))

# def get_upper_chars(text: str):
#     uppers = ''
#     for i in text:
#         x = i.capitalize()
#         if i == x:
#             uppers += i
#     return True