FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r ./Jenkins/python/requirements.txt
RUN pip3 install pylint
RUN pwd
RUN ls
RUN pylint /app/Jenkins/python/app.py || echo "Linting completed with warnings"
CMD ["python3", "./Jenkins/python/app.py"]
