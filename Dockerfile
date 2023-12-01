FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip install -r ./Jenkins/python/requirements.txt
RUN pip3 install pylint
RUN pylint ./Jenkins/python/app.py || echo "Linting completed with warnings"
CMD ["python3", "./Jenkins/python/app.py"]
