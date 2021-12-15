FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Amsterdam

RUN apt-get update && \
    apt-get install -y python3.9 python3-pip python3.9-dev && \
    apt install -y git
# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip3 install --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint
COPY . .
ENTRYPOINT [ "python3" ]
CMD [ "realtimescraper/app.py" ]