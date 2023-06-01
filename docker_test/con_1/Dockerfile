# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /con_1

ENV FLASK_APP=con_1/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY con_1/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 3000


COPY con_1/*.py /con_1/con_1/


CMD ["flask", "run", "-p", "3000"]