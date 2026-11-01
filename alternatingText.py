import pyperclip

text = pyperclip.paste()
alt_text = ''
make_upper = False

for char in text:
    if make_upper:
        alt_text += char.upper()
    else:
        alt_text += char.lower()

    make_upper = not make_upper
    
pyperclip.copy(alt_text)
print(alt_text)