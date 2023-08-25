FROM python:3.8-slim

COPY . /voxy
WORKDIR /voxy

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/voxy:/voxy/app"

##############################################
RUN apt-get update 
RUN apt-get install build-essential gcc g++ musl-dev unixodbc-dev -y
RUN apt-get install libc-dev libxslt-dev libxml2-dev libffi-dev -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
##############################################


EXPOSE 7070

CMD ["uvicorn", "--workers", "1", "--host", "0.0.0.0", "--port", "7070", "main:app"]
