PROJECT_NAME := mfmt
IMAGE_NAME := $(PROJECT_NAME)-image
CONTAINER_NAME := $(PROJECT_NAME)-container
PWD := $(shell pwd)

.PHONY: docker-build docker-run install-rye rye-sync rye-lint rye-fmt pytest mypy

docker-build:
	docker build -t $(IMAGE_NAME) -f Dockerfile .

docker-run:
	docker run -it --rm -v $(PWD):/work --name $(CONTAINER_NAME) $(IMAGE_NAME)

uv-build:
	uv build

install-mfmt:
	uv pip install .
