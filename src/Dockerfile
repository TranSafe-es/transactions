FROM python:2.7
ADD requirements.txt /tmp/requirements.txt
RUN apt-get update && apt-get install -y \
                        python-pip
RUN pip install -U pip setuptools
RUN pip install -r /tmp/requirements.txt
ADD . /code
WORKDIR /code
EXPOSE 80
RUN ["python", "manage.py", "makemigrations"]
RUN ["python", "manage.py", "test"]
RUN ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
