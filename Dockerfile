# ---- Base python ----
FROM python:3.11.1-alpine AS base


# ---- Dependencies ----
FROM base AS build

RUN apk add gcc g++ postgresql-dev linux-headers libffi-dev musl-dev cargo python3-dev make

COPY falcon_api_boilerplate /svc/kicks
COPY setup.py /svc/setup.py
COPY requirements.txt /svc/requirements.txt

WORKDIR /svc
RUN pip install -U pip
RUN pip install wheel && pip wheel . --wheel-dir=./wheels

FROM base
COPY --from=build /svc /svc


WORKDIR /svc
RUN pip install --no-index --find-links=./wheels -r requirements.txt
RUN pip install --no-index --find-links=./wheels .

COPY gunicorn_conf.py gunicorn_conf.py

EXPOSE 8000

CMD [ "gunicorn", "--config", "gunicorn_conf.py", "kicks:api"]