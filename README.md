# Japanese Alphabet Flashcard Generator

## Setup

This project helps generate Anki-style flashcards for learning Japanese. *Please Check the Notes Section for Font Settings*


## 1. Download Python (WinPython)

Get a stable release here:  
https://github.com/winpython/winpython/releases

Example used:
- WinPython64-3.14.4.0dotb1.zip  
- Python 3.14.0 (inside WinPython package)

Extract it somewhere simple like:

```text
C:\WinPython\
````

## 2. Install Make (MinGW)

Download from WinLibs:
[https://winlibs.com/#download-release](https://winlibs.com/#download-release)

Example used:

* winlibs-x86_64-posix-seh-gcc-15.2.0-mingw-w64ucrt-14.0.0-r7.7z

After extracting, rename:

```text
mingw64\bin\mingw32-make.exe → make.exe
```

Add this folder to your PATH:

```text
mingw64\bin
```

## 3. Configure Python path

Edit the config:

```text
init_python_root = C:\path\to\your\python\executable
```

Set it to wherever WinPython is extracted (find `python.exe` inside).

Example:

```text
C:\WinPython\python-3.14.0\
```


## 4. Build

Inside the project folder, run:

```bash
make
```

## Done

Everything should build automatically after that.


> [!NOTE]
> * Please edit the font names (point directly to the .ttf file directly). I used Noto Sans JP and Noto Serif JP from Google Fonts.
> * Unfortunately, I am not Japanese (nor am I a native English speaker), but I am learning the language. Please feel free to point out any errors in the character set.
> * I couldn’t find a suitable Anki deck, and I was a bit lazy, so I decided to make my own.
* I will probably add kanji radicals **Soon™**.
* Emphasis on the word *probably*.
