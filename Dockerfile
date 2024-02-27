FROM python:3.12

RUN mkdir /app

COPY *.py /app/
COPY pyproject.toml /app

WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --only main

CMD ["poetry", "run", "python", "main.py"]
