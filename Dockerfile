FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r ./Jenkins/python/requirements.txt
CMD ["python3", "app.py"]
