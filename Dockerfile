FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r ./Jenkins/python/requirements.txt
RUN pip3 install pylint
RUN pylint ./app.py || echo "Linting completed with warnings"
CMD ["python3", "app.py"]
