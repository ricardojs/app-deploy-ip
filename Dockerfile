FROM ubuntu:latest
MAINTAINER Ricardo Silveira "ricardo.js@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python python-pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
EXPOSE 5000
