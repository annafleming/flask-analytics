FROM python:3.4.5
RUN mkdir /opt/flask-analytics
WORKDIR /opt/flask-analytics
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .
EXPOSE 5000
ENV FLASK_APP=manage.py
CMD ["python", "manage.py", "runserver"]