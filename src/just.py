from pyautogui import *
	#confirm, moveTo, moveRel, click, press, write, size, hotkey, scroll, screenshot
from datetime import datetime as dt
from random import uniform, choice
from time import sleep
from sys import exit as sys_exit
from platform import system

#DEFAULT SETTING ASSUMPTIONS
OS = system()
def is_win():   return OPERATING_SYSTEM =='Windows'
def is_mac():   return OPERATING_SYSTEM=='Darwin'
def is_linux(): return OPERATING_SYSTEM=='Linux'
def is_posix(): return is_mac() or is_linux()

NOTE = 'Notepad' if is_win() else 'TextEdit' if is_mac() else 'gedit'
BROWSER = 'Chrome' if is_win() else 'Safari' if is_mac() else 'Firefox'

#MESSEAGES
OS_WARNING = "WARNING (JustDoIt): Full functionality not yet supported on this OS. May have unintended consequences."
DT_FORMAT  = "%Y.%m.%d_%H.%M.%S"
#SYMBOLS
CMD_CHARS  = ". asdfghjklqwertyuiopzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM`,()0123456789*@&_-/#~|+[]^v<>.!;:?"
CTRL_CHARS = set("asdfghjklqwertyuiopzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
MOUSE = {'*': click,  '@': moveTo,    '&': dragTo}
BUTTONS = {
	'_': "delete", '-': "backspace", '/': "enter", 
	'~': "esc",    '+': "tab",       ' ': "space",
	}
NAV_CHARS = {
	'^':'up',    'v':'down',  '<':'left',  '>':'right',
	'a':'home',  'z':'end',   'A':'pageup','V':'pagedown',
	'|':'scrollup',';':'scrolldown',
	}

#Coordinate Values for points on the screen - to be used in f-strings
W, H = size()
def str_coords(x,y): return f'{str(int(x))},{str(int(y))}'
CENTER = str_coords(W/2, H/2)
TL = str_coords(1, 1)     #"topleft"
TR = str_coords(W-1, 1)   #"topright"
TC = str_coords(W/2, 0)   #"topcenter"
ML = str_coords(0, H/2)   #"midleft"
MR = str_coords(W, H/2)   #"midright"
MC = str_coords(W/2, H/2) #"midcenter"
BL = str_coords(1, H-1)   #"bottomleft"
BR = str_coords(W-1, H-1) #"bottomright"
BC = str_coords(W/2, H)   #"bottomcenter"

# def pause(): sleep(uniform(1.5, 2))

#SCREEN NAVIGATION
def mouse_to(x,y): moveTo(x,y)
def mouse_from(x_offset, y_offset): moveRel(x_offset, y_offset)
def scrollup():   scroll(100)
def scrolldown(): scroll(-100)
#CLICKING
# click(x,y) builtin to pyAutoGUI
def lclick(x,y): click(x,y, button='left')
def rclick(x,y): click(x,y, button='right')
def dclick(x,y): click(x,y, clicks=2)

#SPECIAL
# TODO Set $ to run a command in the terminal/CMD reads line until \n character
# TODO Set () to run hotkey functionality for the characters inside (using JustDoIt symbols)
# ? OS Search
def win_key(): press('win')               #Opens Start Menu
def mac_key(): hotkey('command', 'space') #Opens Spotlight Search
# % ScreenShot
def prtsc(): screenshot().save( dt.now().strftime(DT_FORMAT)+'.png' )
# ! Alert/Confirmation
def confirm_auto(
		message='Automation paused. Continue running?',
		title='JustDoIt Automation',
		buttons=['OK', 'Cancel']):
	resp = confirm(message, title, buttons)
	if resp=='OK': return True
	else: sys_exit("[Exiting JustDoIt Automation...]")

#WRITING (TYPING)
def write(it=str):
	for i in it:
		sleep(uniform(0.03, 0.12))
		press(i)
    
#HOTKEY CONTROL
def hotk(super=str, char=str):
	if char.isupper():  hotkey(super,'shift', char, interval=0.1)
	else:
		hotkey(super, char, interval=0.1)
		if not char.islower() and char!=' ':
			print("WARNING: ctrl/cmd function was not given a letter")

#CTRL SHORTCUTS for Basic ctrl+X or ctr+shift+X Operations
def ctrl(it=str):
	if is_win():   hotk('ctrl', it)
	elif is_mac(): hotk('command', it)
	else:          hotk('ctrl', it); print(OS_WARNING)

#INTER/INTRA-WINDOW NAV
  #TODO - Determine Shorthand symbols for these
def next_tab(): hotkey('ctrl','tab', interval=0.1)
def prev_tab(): hotkey('ctrl','shift','tab', interval=0.1)
def prev_window(): hotkey('alt','tab', interval=0.1)
def last_window(): hotkey('alt','shift','tab', interval=0.1)


def do(it=str):
	pause_mode = False
	write_mode = False
	nav_mode   = False
	coord_mode = False
	#alert_mode = False
	coords    = ""
	text      = ""
	pause_val = ""
	tmpcmd    = ""

	for char in it:
		if char not in '\n\t\r':
			if char not in CMD_CHARS:
				print(f"Warning: '{char}' not a functional command character. Refer to the docs:\n{DOCS_URL}")
	sleep(0.3) #Safety buffer before starting
	for char in it:
		# Ignore Tabs, Newlines, and Returns
		if char in '\n\t\r': continue
		
			
		# Writing Mode
		if char=='`':
			if write_mode:
				write(text)
				text = ''  # Clear the text buffer
			write_mode = not write_mode
			continue
		if write_mode:
			text += char
			continue

		# Alert Mode
		if char=='!':
			confirm_auto()
			continue
    #TODO - Consider Implementing an alert mode to allow for cutom prompts/alerts (maybe using \n as terminating syntax)
		#	if alert_mode:
		#		if text: confirm_auto(message=text)
		#		else: confirm_auto()
		#		text = ''  # Clear the text buffer
		#	alert_mode = not alert_mode
		#	continue
		#if alert_mode:
		#	text += char
		#	continue

		# Pause Mode
		if pause_mode:
			if char.isdigit():
				pause_val += char
				continue
			else:
				if pause_val:
					sleep(int(pause_val))
					pause_val = ''
				else:
					sleep(1)
				pause_mode = False
		if char=='.':
			pause_mode = True
			continue

		# Coordinate Mode
		if char in '@*&':
			coord_mode = True
			tmpcmd = char
			continue
		if coord_mode:
			if char in ",0123456789":
				coords += char
				continue
			else:
				if tmpcmd == '*':
					if char=='*':
						dclick(*position())
						continue
					else:
						click(*position())
				elif coords:
					x,y = map(int, coords.split(','))
					sleep(1)
					MOUSE[tmpcmd](x,y)
				coord_mode = False
				coords = ''
				tmpcmd = ''
		
		#ADD COMMENT
		if char=='?':
			if is_win(): win_key()
			if is_mac(): mac_key()
			continue

		# Navigation Mode
		if char == '[':
			nav_mode = True
			continue
		if char == ']':
			nav_mode = False
			continue
		if nav_mode:
			if char in NAV_CHARS:
				press(NAV_CHARS[char])
				PAUSE = uniform(1.5, 2)
				continue

		# Hotkey Functionality
		elif char in CTRL_CHARS:
			ctrl(char)
			PAUSE = uniform(1.5, 2)

		# Button Presses
		elif char in BUTTONS:
			press(BUTTONS[char]) # Call the corresponding function for the button key
			# BUTTONS[char]()
		else:
			print(f"ERROR: Unknown command character '{char}'")


def give_up():
	messages = [
		"Yesterday, you said tomorrow. Don't give up!",
		"Don't let your code be bugs. Debug it!",
		"If you're tired of starting over, stop giving up!",
		"The code won't write itself. Just code it!",
		"Dreams of a clean code? Refactor it!",
		"Error? More like a challenge!"
		]
	motivational_shout = choice(messages)

	# Log the moment of weakness for reflection.
	with open("give_up_log.txt", "a") as f:
		f.write(f"[{dt.now().strftime(DT_FORMAT)}] - Thought about giving up. Shia says: '{motivational_shout}'\n")
	# Raise the RuntimeError with the motivational message.
	raise RuntimeError(motivational_shout)
