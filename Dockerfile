FROM python:3.7

RUN apt-get update && apt-get install -y make rsync
RUN pip install --upgrade pip

ENV PROJECT queube

COPY docker-config/bashrc /root/.bashrc

WORKDIR /opt/${PROJECT}

COPY ./ /opt/${PROJECT}
RUN make dev-install
