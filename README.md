# Pokemon as a Service

## Usage

### docker

#### build

```docker
docker build . -t pokemon-as-a-service
```

#### run
```docker
docker run -d -p 5000:5000 -e ES_HOST=db pokemon-as-a-service
```

### docker-compose

run all services (app, elasticsearch instance and kibana)
```docker
docker compose up -d
```

### cli
* Running the module
```shell
python -m paas.app
```

* Using `flask run` (and set flask parameters as you preferred)
```shell
export FLASK_APP=paas.app
flask run
```

## Options

* `ES_HOST` - the ElasticSearch host machine
* `ES_PORT` - the ElasticSearch port (default: `9200`)

## Test

* install pytest
    ```shell
  pip install pytest
    ```
* (Optional) set api base (default: `http://localhost:5000/api/`)
  ```shell
  export PAAS_API_BASE=http://your-endpoint/api
    ```
* run tests
  ```shell
  pytest -s
  ```