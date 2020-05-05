FROM python:3.6

COPY . /usr/src/app

RUN pip install -r requirment.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]