# *__JustDoIt__: Simplified Automation with PyAutoGUI*

*`JustDoIt`* is for computer task automation using a compact string command syntax. This module seeks to provide a 'regex-like' mechanism for computer automation. The command string uses special characters and sequences to dictate a variety of actions, from mouse movements and clicks to keyboard inputs and other system operations.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#example-usages)
- [Symbol Reference](#symbol-reference)
- [License](#license)
<!--- [Contributing](#contributing)-->

## Features

- **Keyboard Automation**: Easily write text, perform hotkey actions, and more.
- **Mouse Automation**: Perform clicks, drags, and mouse movements with simple commands.
- **Screen Navigation**: Navigate through screens, tabs, and windows with ease.
- **Warnings / Errors**: Tries to provide feedback for unknown command characters to help troubleshoot issues.

## Installation

To use `JustDoIt`, you first need to install `pyautogui`:

```
pip install pyautogui
```

## Usage
Here's a quick rundown of the command characters you can use with `JustDoIt`.

### **Command Characters**:
- `? ` Search Key (Win Key or Command+Spacebar on Mac) 
- `! ` Alert/Confirmation (for testing and human actions)
- `% ` Screenshot (saves to current directory as `{DT_FORMAT}.png`)

### **Typing (Writing Mode)**:
- Write Mode: To write text to your screen as if with your keyboard, surround your text with the backtick (```
		`
		```) character.
- For example:
		```
		`Hello World`
		```
### **Keyboard Actions**:
- `_ ` Delete
- `- ` Backspace
- `/ ` Enter
- `~ ` Escape key
- `+ ` Tab key
- `  ` (Space) Spacebar

###  **Mouse Actions**:
The following invoke 'Coordinate Mode', where you specify the `x,y` coordinates `*500,1000` of the mouse action:
- `* ` Click
- `& ` Drag To
- `@ ` Move To

### **Navigation Commands**:
Use the `[` and `]` characters to enter and exit navigation mode. While in navigation mode:
- `^ v < > ` Arrow Keys
- `a z ` Home/End Keys
- `A V ` Pageup/Pagedown
- and more...

For a full list of commands, refer to the source code. Some of the symbols are not yet implemented, but will be in the future, and a rare few are subject to change.
<!--You can also use the `JustDoIt.help()` function to print out a list of commands.-->

## Example Usages

Here are some examples that demonstrate some basic `JustDoIt` functionality:

### Mouse Movement:
```python
from JustDoIt import just

just.do(it="""
	@10,10.@50,50.@100,100.@200,200.
	@300,300.@400,400.@600,600
	@{BC}@{TR}@{BL}@{MR}@{CENTER}
	""")
```

### Application Use:
```python
# Writes "Hello World" to a note and saves it:
just.do(it=f".?.`{NOTE}`/.`Hello World?`-----`ORLD!!!`s.`JustDoIt.txt`/.w")
```

### Browsing:
```python
# Opens YouTube vid in Fullscreen, then Closes it after confirmation:
url = 'https://youtu.be/ZXsQAXx_ao0'
just.do(it=f"@{MC}.2?`{BROWSER}`./.l`{url}`./.5**.10!w")
```

For more complex/modular sequences, you can use variables and F-strings to title/chain a multitude of commands.

## Default Variables and Settings
On import, JustDoIt will try to infer what OS, Browser, and Note-taking app you are using. If it can't, it will default to Windows, Chrome, and Notepad. Users can set these variables manually by setting the following variables to one of it's options:
```python
OPERATING_SYSTEM = 'Linux' #['Windows', 'Linux', 'Mac']
BROWSER = 'Brave' #['Chrome', 'Firefox', 'Safari', 'Edge'...]
NOTE = 'Sublime' #['Notepad', 'TextEdit', 'gedit'...]
```
- Settings options for Speed, Verbosity, and more are in the works.


<!--## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](#).-->



## Symbol Reference
The default mode is `Control Mode`, where letters/characters are interpreted as keyboard commands. For example, lower-case `c` is interpreted as `ctrl/cmd + C` (copy), and capital `T` would be interpreted as `ctrl/cmd + shift + T` (reopen last tab). Though JustDoIt can covers the most common shortcuts, it does not yet support them all. For an intensive list, check out: Wikipedia's [Table of Keyboard Shortcuts](https://en.wikipedia.org/wiki/Table_of_keyboard_shortcuts). The following tables details JustDoIt's non-alphabetic character functions.

| character | Action / Behavior |
| ------ | ----------- |
| `?` | Search Key (Win Key or Command+Spacebar on Mac) |
| `!` | Alert/Confirmation (for testing and human actions) |
| `%` | Screenshot (saves to current dir as `{DT_FORMAT}.png`) |
| `.n` | Pause operation for 'n' seconds |
| `...` | Pause operation for $2^{(n\_dots-1)}$ |


| character | Control Mode |
| ------ | ----------- |
| `a`-z | Ctrl/Cmd + A |
| `A`-Z | Ctrl/Cmd + Shift + A |
| `_` | Delete |
| `-` | Backspace |
| `/` | Enter |
| `~` | Escape key |
| `+` | Tab key |
| `'` `'` | (Space) Spacebar |


| character | Writing Mode |
| ------ | ----------- |
| `(Backtick)` | Starts/Stops Writing mode |
| `(Backslash)` | Allows for backtick in Writing mode __*(Not Yet Implemented)*__ |


| character | Coordinate Mode |
| ------ | ----------- |
| `*` | Click In-place |
| `**` | Double-click In-place |
| `*x,y` | Click at Coordinates x,y (ie `*10,500`) |
| `@x,y` | Move to Coordinates x,y (ie `@700,800`) |
| `&x,y` | Drag to Coordinates x,y (ie `&0,500`) |


| character | Navigation Mode |
| ------ | ----------- |
| `[` | Enter Navigation Mode |
| `]` | Exit Navigation Mode |
| `^` | Up Key |
| `v` | Down Key |
| `<` | Left Key |
| `>` | Right Key |
| `a` | Home Key |
| `z` | End Key |
| `A` | Pageup |
| `V` | Pagedown |




## License

This project is [MIT](LICENSE) licensed.