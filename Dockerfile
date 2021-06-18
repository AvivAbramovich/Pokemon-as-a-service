FROM python:3.8-alpine

WORKDIR /code
EXPOSE 5000

ENV ES_HOST ''
ENV ES_PORT 9200
ENV FLASK_APP=paas.app

ADD paas/requirements.txt .
RUN pip install -r requirements.txt

ADD paas paas

CMD ["python3", "-m", "flask", "run", "--host", "0.0.0.0"]