# Variables
UV := uv 
UVX := uvx 
SYNC := $(UV) sync --locked
PYTEST := $(UV) run pytest -q --tb=short
CHECK := $(UVX) ruff linter src tests
FORMAT := $(UVX) ruff format src tests

# Default
.PHONY: help
help:
	@echo "Makefile commands:"
	@echo "  docker-run   - Run the Docker container"
	@echo "  docker-build - Build the Docker image"
	@echo "  sync         - Install dependencies"
	@echo "  install      - Install the package in editable mode with pip"
	@echo "  pipeline     - Run data seeding pipeline"
	@echo "  test         - Run tests"
	@echo "  format       - Format code"
	@echo "  clean        - Clean python artifacts"
# Build Docker image
.PHONY: docker-build
docker-build:
	docker build -t dataseeder:latest .

# Run Docker container
.PHONY: docker-run
docker-run:
	docker run --env-file .env -it dataseeder:latest

# Install dependencies
.PHONY: sync
sync:
	$(SYNC)

.PHONY: install
install: 
	python -m pip install -e .
# Run pipeline 
.PHONY: pipeline
pipeline:
	$(UV) run src/dataseeder/pipeline.py

# Run tests
.PHONY: test
test:
	$(PYTEST)

# Format code
.PHONY: format
format:
	$(FORMAT)
	
# Clean python artifacts
.PHONY: clean
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
