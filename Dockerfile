FROM ubuntu:24.04

WORKDIR /work

RUN apt update -y \
    && apt install -y curl cmake python3 python3-dev python3-pip \
    && rm -rf /var/lib/apt/lists

# https://github.com/astral-sh/rye/discussions/239#discussioncomment-6032595
COPY requirements.lock ./
RUN sed '/^-e file:\.$/d' requirements.lock > requirements.txt
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY Makefile ./
COPY scripts/ scripts/
COPY tests/ tests/

CMD ["/bin/bash"]
