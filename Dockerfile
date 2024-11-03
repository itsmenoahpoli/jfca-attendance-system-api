FROM python:3.12

WORKDIR /app

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

CMD ["fastapi", "dev", "app/main.py", "--host", "0.0.0.0"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]