FROM python:3-onbuild

WORKDIR /root

RUN apt-get update && apt-get -y install netcat

COPY requirements.txt ./
COPY trip.py ./
COPY run.sh ./
COPY config.yaml ./
RUN chmod +x run.sh

RUN pip install --user -r requirements.txt

CMD ["./run.sh"]
