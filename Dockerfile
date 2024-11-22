FROM ubuntu:24.04

WORKDIR /work

RUN apt update \
    && apt install -y curl

COPY uv.lock ./
COPY pyproject.toml ./

RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && /root/.local/bin/uv sync

COPY Makefile ./
COPY scripts/ scripts/
COPY tests/ tests/

CMD ["/bin/bash"]
