FROM python:3.8-alpine

WORKDIR /code
EXPOSE 5000

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD *.py .

CMD ['python3', '-m', 'flask', 'run', '--host', '0.0.0.0']