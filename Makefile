PROJECT_NAME := mfmt
SYSTEM_NAME ?= default
IMAGE_NAME := $(PROJECT_NAME)-$(SYSTEM_NAME)-image
CONTAINER_NAME := $(PROJECT_NAME)-$(SYSTEM_NAME)-container
DOCKERFILE := docker/Dockerfile$(if $(filter default,$(SYSTEM_NAME)),,$(addprefix .,$(SYSTEM_NAME)))
PWD := $(shell pwd)

.PHONY: docker-build docker-run install-rye rye-sync rye-lint rye-fmt pytest mypy

docker-build:
	docker build -t $(IMAGE_NAME) -f $(DOCKERFILE) .

docker-run:
	docker run -it --rm --name $(CONTAINER_NAME) $(IMAGE_NAME)

uv-build:
	uv build

install-mfmt:
	uv pip install .

pytest:
	uv run pytest tests

ruff-check:
	uvx ruff check

ruff-fmt:
	uvx ruff fmt

mypy:
	uvx mypy
