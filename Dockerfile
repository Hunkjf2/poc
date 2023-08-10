FROM python:3.11.4-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential=12.9 libpq-dev=15.3-0+deb12u1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

FROM python:3.11.4-slim as runner


RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    libpq-dev=15.3-0+deb12u1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m python

RUN mkdir /usr/app && chown python:python /usr/app
WORKDIR /usr/app
COPY --from=builder /usr/app/venv ./venv
COPY projeto/ .
USER python

ENV PATH="/usr/app/venv/bin:$PATH"

CMD ["/bin/bash", "-c", "python manage.py runserver 0.0.0.0:8000"]