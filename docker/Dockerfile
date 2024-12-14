FROM ubuntu:24.04

WORKDIR /work

RUN apt update \
    && apt install -y curl build-essential

COPY uv.lock ./
COPY pyproject.toml ./

RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && /root/.local/bin/uv sync --no-install-project

COPY Makefile ./
COPY src/ src/
COPY tests/ tests/

CMD ["/bin/bash"]
