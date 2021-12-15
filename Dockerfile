FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Amsterdam

RUN apt-get update && \
    apt-get install -y python3.9 python3-pip python3.9-dev
# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT [ "python3" ]
CMD [ "realtimescraper/app.py" ]