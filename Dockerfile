FROM python:latest

RUN apt-get update \
    && apt-get install -y \
    grep \
    ncat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install psutil

WORKDIR /xml

COPY . .

RUN chmod 777 *.sh

ENTRYPOINT ["./start_nc.sh"]
