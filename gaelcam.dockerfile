
FROM python:3.8-slim


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir numpy matplotlib seaborn roboflow ultralytics


COPY train.py /app/


CMD ["python", "train.py"]
