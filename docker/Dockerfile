# build from repo-root
ARG IMAGE_ENV="dev"

FROM python:3.10-alpine AS base
ARG PACKAGE_DEVELOPMENT_MODE

LABEL version=0.0
MAINTAINER Maximilian Langknecht

WORKDIR /app

COPY setup.py .
COPY src/pantry_supply_tracker src/pantry_supply_tracker

FROM base as package-dev
RUN pip install --upgrade pip && pip install ${PACKAGE_DEVELOPMENT_MODE} .

FROM base as package-test
RUN pip install --upgrade pip && pip install ${PACKAGE_DEVELOPMENT_MODE} .[test]

FROM package-${IMAGE_ENV} AS final
