VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
MAIN_FILE = src/main.py

.PHONY: requirements clean install reinstall run lint format

# Rules
$(VENV):
	@if [ ! -d "$(VENV)" ]; then \
		echo "Generation of .venv"; \
		python3 -m venv $(VENV); \
	fi

# Commands
requirements:
	$(PIP) freeze > requirements.txt
	@echo "File requirements.txt generated"

clean:
	rm -rf $(VENV)

install: $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Dependencies installed"

reinstall: clean install

run:
	@$(PYTHON) $(MAIN_FILE)

lint:
	@$(PIP) install ruff
	@$(VENV)/bin/ruff check src/

format:
	@$(PIP) install ruff
	@$(VENV)/bin/ruff format src/

