FROM continuumio/miniconda3 AS build

COPY environment.yml .
RUN apt-get update -y
RUN apt-get install -y libicu-dev
RUN conda update conda
RUN conda env update -n root -f environment.yml



