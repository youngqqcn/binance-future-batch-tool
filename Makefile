
.PHONY: build
build:
	pyside6-uic form.ui -o ui_form.py

run: build
	python3 widget.py


