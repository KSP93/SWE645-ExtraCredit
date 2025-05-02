
FROM python:3.12-slim

WORKDIR /code

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       libssl-dev \
       libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt /code/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /code/requirements.txt

COPY app /code/app

ENV PYTHONPATH=/code

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
