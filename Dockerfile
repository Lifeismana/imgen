#not using slim image because pillow require some libs that are not in slim image
#TODO use slim version and install lib required by pillow
FROM python:3.8 AS latest


RUN set -eux; \
    wget https://github.com/matomo-org/travis-scripts/blob/master/fonts/Verdana.ttf -O assets/crab/Verdana.ttf;\
    apt-get update; \
    apt-get install -y --no-install-recommends \
        graphicsmagick \
        fonts-symbola \ 
        libmagickwand-dev ; \
    # CrabRave needs this policy removed
    sed -i '/@\*/d' /etc/ImageMagick-6/policy.xml; \
    rm -rf /var/lib/apt/lists/* ;

WORKDIR /imgen
COPY . .

RUN set -eux; \
pip3 install -r /imgen/requirements.txt ;\
pip3 install -r /imgen/optional_requirements.txt;


#TODO expose custom port
EXPOSE 65535

CMD [ "gunicorn","-c","gunicorn.conf.py","server:app"]