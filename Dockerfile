FROM python:3.7

RUN apt-get update && apt-get install -y make rsync nginx sass
RUN pip install --upgrade pip

ENV PROJECT queube

COPY docker-config/bashrc /root/.bashrc
COPY etc/nginx/sites-available/default-dev /etc/nginx/sites-available/default

WORKDIR /opt/${PROJECT}

COPY ./ /opt/${PROJECT}
RUN make dev-install
