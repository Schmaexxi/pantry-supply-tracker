ARG IMAGE_ENV="dev"
ARG PACKAGE_DEVELOPMENT_MODE
FROM python:3.10-alpine AS base

LABEL version=0.0
MAINTAINER Maximilian Langknecht

WORKDIR /app

COPY setup.py .
COPY pantry_supply_tracker pantry_supply_tracker

FROM base as package-dev
RUN pip install --upgrade pip && pip install ${PACKAGE_DEVELOPMENT_MODE} .

FROM base as package-test
RUN pip install --upgrade pip && pip install ${PACKAGE_DEVELOPMENT_MODE} .[test]

FROM package-${IMAGE_ENV} AS final
