.PHONY: run
run:
	./main.py

.PHONY: test
test:
	pytest test_*.py

ifndef VERBOSE
.SILENT:
endif
