<div align="center">
<pre>
██████╗░██████╗░███████╗  ███╗░░░███╗░█████╗░██████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔════╝  ████╗░████║██╔══██╗██╔══██╗██║░██╔╝
██████╔╝██║░░██║█████╗░░  ██╔████╔██║███████║██████╔╝█████═╝░
██╔═══╝░██║░░██║██╔══╝░░  ██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗░
██║░░░░░██████╔╝██║░░░░░  ██║░╚═╝░██║██║░░██║██║░░██║██║░╚██╗
╚═╝░░░░░╚═════╝░╚═╝░░░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
-------------------------------------------------------------
 A tool for PDF manipulation made in python3
</pre>

[![LICENSE: GPLv3](https://img.shields.io/badge/LICENSE-GPLv3-blue)](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text)
  
</div>

## Installation

### Source code
Clone the repo on the local machine.

### Binary
Go to [Releases](https://github.com/PingalPie/PDF-Mark/releases/),
get the installer or the binary as per your use case.

## Usage
There are multiple ways to use this program.

### GUI
Graphical user interface for nerds.

``` sh
python3.11 gui.py
```

### Web
Web interface if you want to self-host.

``` sh
python3.11 web.py
```

### CLI (Command Line Interface)
Command line interface if you want speed and portability and knows how to use terminal.

``` sh
python3.11 cli.py
```

## Dependencies
- Python3.11
- PyPDF
- PILLOW
- TKinter ( for gui framework )
- Flask ( for web framework )
- Click ( for cli framework )
- pycryptodome ( for encrypting/decrypting pdf files )

## Files/Folders used
### main.py
Empty file

### pdf.py
Contains all pdf manipulative functions.

### gui.py
GUI or Graphical User Interface implementation

### cli.py
CLI or Command Line Interface implementation

### web.py
Web implementation

### templates - folder
HTML files required for web framework.

### static - folder
Data files required for web framework.
