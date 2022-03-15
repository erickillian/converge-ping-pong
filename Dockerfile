FROM python:3.7.12

WORKDIR /code

ADD . /code

RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic
