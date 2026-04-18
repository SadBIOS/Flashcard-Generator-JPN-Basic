init_python_root = C:\path\to\your\python\executable
cache = __pycache__
venv_name = venv
script_name = kana_flashcard_gen

default: $(venv_name)\Scripts\python.exe
	$(venv_name)\Scripts\python.exe -m $(script_name)

env:
	$(init_python_root)\python.exe -m venv $(venv_name)
	powershell -Command "if (Test-Path $(venv_name)) {New-Item -ItemType Directory -Path $(venv_name)\Packages}"
	powershell -Command "if (Test-Path $(venv_name)\Packages) {New-Item -ItemType Directory -Path $(venv_name)\Packages\Pillow}"
	$(venv_name)\Scripts\python.exe -m pip --disable-pip-version-check --no-cache-dir download pillow --dest "$(venv_name)\Packages\Pillow"
	$(venv_name)\Scripts\python.exe -m pip install --disable-pip-version-check --no-index --find-links "$(venv_name)\Packages\Pillow" pillow 

clean:
	powershell -Command "if (Test-Path $(venv_name)) {Remove-Item -Recurse -Force -Verbose $(venv_name)}"
	powershell -Command "if (Test-Path $(cache)) {Remove-Item -Recurse -Force -Verbose $(cache)}"
	powershell -Command "if (Test-Path sans_serif_hiragana) {Remove-Item -Recurse -Force -Verbose sans_serif_hiragana}"
	powershell -Command "if (Test-Path serif_hiragana) {Remove-Item -Recurse -Force -Verbose serif_hiragana}"
	powershell -Command "if (Test-Path sans_serif_katakana) {Remove-Item -Recurse -Force -Verbose sans_serif_katakana}"
	powershell -Command "if (Test-Path serif_katakana) {Remove-Item -Recurse -Force -Verbose serif_katakana}"
	powershell -Command "if (Test-Path hiragana_combined) {Remove-Item -Recurse -Force -Verbose hiragana_combined}"
	powershell -Command "if (Test-Path katakana_combined) {Remove-Item -Recurse -Force -Verbose katakana_combined}"