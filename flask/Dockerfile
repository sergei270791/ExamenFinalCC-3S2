FROM ubuntu:22.04
RUN apt-get update && \
apt-get install -y python3 && \
apt-get install -y python3-pip && \
pip install Flask

COPY hola.py .
ENTRYPOINT ["python3","hola.py"]




