import pyperclip
text =pyperclip.paste()
#todo

lines = text.split('\n')
for i in range(len(lines)):
    lines[i]= '*' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)