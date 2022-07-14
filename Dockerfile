FROM python:3.8.0-buster
WORKDIR /app
COPY . /app
RUN pip install flask
CMD ["python" ," Mainscore.py"]


