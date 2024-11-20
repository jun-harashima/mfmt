PROJECT_NAME := mfmt
IMAGE_NAME := $(PROJECT_NAME)-image
CONTAINER_NAME := $(PROJECT_NAME)-container
PWD := $(shell pwd)

.PHONY: docker-build docker-run install-rye rye-sync rye-lint rye-fmt pytest mypy

docker-build:
	docker build -t $(IMAGE_NAME) -f Dockerfile .

docker-run:
	docker run -it --rm -v $(PWD):/work --name $(CONTAINER_NAME) $(IMAGE_NAME)

install-rye:
	curl -sSf https://rye.astral.sh/get | RYE_NO_AUTO_INSTALL=1 RYE_INSTALL_OPTION="--yes" bash
	# Do not source $HOME/.rye/env (add only rye to the PATH, do not add python3 to the PATH)
	# to use the Python from the base image. We use rye only for package management.
	ln -s $$HOME/.rye/shims/rye /usr/local/bin

rye-sync:
	rye sync

rye-lint:
	rye lint

rye-fmt:
	rye fmt

pytest:
	env PYTHONPATH="." rye run pytest -vv

mypy:
	rye run mypy
