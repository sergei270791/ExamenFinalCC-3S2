FROM jenkins/agent
USER root
RUN apt-get update && \
apt-get install -y python && \
apt-get install -y ruby-full
USER jenkins
