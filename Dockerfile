#not using slim image because pillow require some libs that are not in slim image
#TODO use slim version and install lib required by pillow
FROM python:3.8 AS latest


RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        graphicsmagick ; \
        libmagickwand-dev ; \
    rm -rf /var/lib/apt/lists/* ;

WORKDIR /imgen
COPY . .

RUN set -eux; \
pip3 install -r /imgen/requirements.txt ;\
pip3 install -r /imgen/optional_requirements.txt;


#TODO expose custom port
EXPOSE 65535

CMD [ "gunicorn","-c","gunicorn.conf.py","server:app"]