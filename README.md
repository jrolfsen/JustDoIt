# **JustDoIt**: Simplified Automation with PyAutoGUI

`JustDoIt` is for computer task automation using a compact string command syntax. This module seeks to provide a 'regex-like' mechanism for computer automation. The command string uses special characters and sequences to dictate a variety of actions, from mouse movements and clicks to keyboard inputs and other system operations.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command Characters](#command-characters)
  - [Example Usages](#example-usages)
<!--- [Contributing](#contributing)-->
- [License](#license)

## Features

- **Keyboard Automation**: Easily write text, perform hotkey actions, and more.
- **Mouse Automation**: Perform clicks, drags, and mouse movements with simple commands.
- **Screen Navigation**: Navigate through screens, tabs, and windows with ease.
- **Error Reporting**: Provides feedback for unknown command characters to help troubleshoot issues.

## Installation

To use `JustDoIt`, you first need to install `pyautogui`:

```
pip install pyautogui
```

## Usage

### Command Characters

Here's a quick rundown of the command characters you can use with `JustDoIt`:

- **Keyboard Actions**:
  - Special Buttons:
    - `?`: Windows Key (or Command Spacebar on Mac)
    - `_`: Delete
    - `-`: Backspace
    - `/`: Enter
    - `~`: Escape key
    - `+`: Tab key
    - ` ` (Space): Spacebar

- **Typing**:
  - Write Mode: Surround your text with the `\`` character. For example: `\`Hello World\``

- **Mouse Actions**:
  - The following invoke 'Coordinate Mode', where you specify the coordinates `*888,888`` of the mouse action:
	- `*`: Click
	- `&`: Drag
	- `@`: Move To

- **Navigation Commands**:
  - Use the `[` and `]` characters to enter and exit navigation mode.
  - While in navigation mode:
    - `^`: Up
    - `v`: Down
    - `<`: Left
    - `>`: Right
    - and more...

For a full list of commands, refer to the source code. Some of the symbols are not yet implemented, but will be in the future, and a rare few are subject to change.
<!--You can also use the `JustDoIt.help()` function to print out a list of commands.-->

### Example Usages

Here's a basic example of how you can use `JustDoIt`:

```python
from JustDoIt import just

# Move mouse to coordinates around the screen:
just.do(it".@10,10.@50,50.@100,100.@200,200.@300,300.@400,400.@600,600@{BC}@{TR}@{BL}@{MR}@{CENTER}")

# Writes "Hello World" to a note and saves it:
just.do(it=f".?.`{NOTE}`/.`Hello World?`-----`ORLD!!!`s.`JustDoIt.txt`/.w")

# Opens YouTube vid in Fullscreen, then closes it after confirmation:
url = 'https://youtu.be/ZXsQAXx_ao0'
do(it=f"@{MC}.2?`{BROWSER}`./.l`{url}`./.5**.10!w")

```

For more complex sequences, you can string together multiple commands.

<!--## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](#).-->

## License

This project is [MIT](LICENSE) licensed.

---

You might want to fill in the placeholders, such as the issues page link, or modify the content as per your preferences and project specifics.
