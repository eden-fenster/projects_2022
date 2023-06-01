# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /con_2

ENV FLASK_APP=con_2/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY con_2/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000


COPY con_2/*.py /con_2/con_2/


CMD ["flask", "run", "-p", "8000"]