FROM python:2.7
RUN apt-get -y update

ADD . /opt/pi_director/
WORKDIR /opt/pi_director
RUN pip install .
CMD gunicorn --paste /opt/pi_director/production.ini -b :6543 -w 4
