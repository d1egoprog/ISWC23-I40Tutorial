FROM python:3.10-slim

# Building Attributes
ARG BUILD_DATE
ARG VERSION
ARG COMPONENT_NAME
ENV COMPONENT ${COMPONENT_NAME}

RUN apt-get update && apt-get install -y git

LABEL maintainer="Diego, Rincon-Yanez (d1egoprog)(RID7RNG)"
LABEL description="Docker Image for ISWC 2023 Tutorial on Industry 4.0"
LABEL org.opencontainers.image.name=$COMPONENT_NAME
LABEL org.opencontainers.image.title=$COMPONENT_NAME
LABEL org.opencontainers.image.created=$BUILD_DATE
LABEL org.opencontainers.image.version=$VERSION
LABEL org.opencontainers.image.vendor="BOSCH AI Research AIR3" 

RUN python -m pip install --no-cache --upgrade setuptools pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /opt/${COMPONENT}
COPY __main__.py __main__.py

ENTRYPOINT python __main__.py -o $OUTPUT_KG $INPUT_MAPPING $ONTOLOGY