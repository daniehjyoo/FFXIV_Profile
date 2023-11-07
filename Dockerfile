FROM python:3.11
ARG API_KEY
ENV API_KEY=$API_KEY

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3", "./main.py" ]