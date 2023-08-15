# This tool is used to manipulate pdfs

# Dependecies
- python
- pypdf
- pillow
- tkinter (optional if you use only web framework)
- flask   (optional if you use only gui framework)
- pycryptodome (if you want to encrypt pdfs)

tkinter or flask is required to run

# Usage
There are two different ways to use this program

## GUI application
This is just the gui implementation of the functions which are in pdf.py

```bash
python3 gui.py
```

## Web application
This is just the web implementation of the functions which are in pdf.py

```bash
python3 web.py
```
After running the web.py go to localhost:5000 in your browser.

## CLI application
This is just the cli implementation of the functions which are in pdf.py

```bash
python3 cli.py
```

# Files/Folders
## main.py
There is nothing in there.
## pdf.py
Every function to manipulate pdfs lives there. 
## gui.py
That is the gui implementation.
## cli.py
That is the cli implementation.
## web.py
That is the web implementation.
## templates - Folder
There resides all the html files required for web framework
## static - Folder
There resides all the data files required for web framework
