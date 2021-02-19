BIN=venv/bin/

install:
	$(BIN)pip install -r requirements.txt

run:
	$(BIN)python main.py
