COLOR_CYAN := \033[36m
COLOR_RESET := \033[0m

SRCS := $(shell git ls-files '*.py')

.DEFAULT_GOAL := help

.PHONY: all
all: test ## Run tests

.PHONY: help
help: ## Show this help message
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make [options] $(COLOR_CYAN)[target] ...$(COLOR_RESET)\n\n"} \
	/^[a-zA-Z_-]+:.*##/ {printf "  $(COLOR_CYAN)%-20s$(COLOR_RESET) %s\n", $$1, $$2}' \
		$(MAKEFILE_LIST)

.PHONY: test
test: ## Run tests
	uv run pytest test_*.py

.PHONY: format
format: ## Format Python sources in place
	uv run ruff format $(SRCS)

.PHONY: format-check
format-check: ## Fail if Python sources require formatting
	uv run ruff format --check $(SRCS) \
		|| (echo "Some files require formatting. Run 'make format' to fix." && exit 1)

.PHONY: clean
clean: ## Remove generated caches
	find . \( -path ./.git -o -path ./.venv -o -path ./venv \) -prune \
		-o -type d -name __pycache__ -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache
	rm -f .coverage .coverage.*

ifneq ($(VERBOSE),1)
.SILENT:
endif
