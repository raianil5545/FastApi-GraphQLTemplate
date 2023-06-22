FROM python:3
ENV PYTHONUNBUFFERED=1
# Install PostgreSQL client and development headers
RUN apt-get update \
    && apt-get install -y postgresql-client libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install build dependencies
RUN apt-get update \
    && apt-get install -y build-essential libssl-dev libffi-dev python3-dev

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 8000