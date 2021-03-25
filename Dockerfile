FROM python:3
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 8000
WORKDIR /mysite
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ] 