FROM python:3.9

WORKDIR /src/validator

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./password_validator.py"]