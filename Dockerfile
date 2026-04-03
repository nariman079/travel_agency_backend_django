FROM python:3.12
ENV PYTHONUNBUFFERED=1
RUN pip install poetry
WORKDIR /code/
COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false && poetry install --no-root
COPY . /code/