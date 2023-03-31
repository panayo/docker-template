FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /app
COPY Pipfile* /app/
RUN pipenv install

COPY . /app/

EXPOSE 8501

CMD [ "./start.sh" ]
