FROM python:3.9

COPY requirements.txt .
COPY . .
RUN pip3 install poetry 
RUN poetry install

EXPOSE 5000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
