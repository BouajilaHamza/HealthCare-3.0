FROM python:3.11.0a1-alpine3.14


WORKDIR /


COPY . .
COPY requirements.txt requirements.txt

RUN pip install -U -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main", "app", "8000","--reload"]