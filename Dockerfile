FROM python:3.10.9-slim-buster
COPY . /app
WORKDIR /app
EXPOSE 5000
ENV NAME Drug_Class
RUN pip install -r requirements.txt
CMD ["python","drug.py"]