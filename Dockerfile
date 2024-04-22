FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

COPY e_lib /app/e_lib

# Install dependencies
COPY requirements.txt /app/e_lib/requirements.txt
RUN pip install --no-cache-dir -r /app/e_lib/requirements.txt

ENV DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS}

WORKDIR /app/e_lib

EXPOSE 9026

CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "loaddata", "dictionary/fixtures/*.json"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:9026"]
