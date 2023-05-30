FROM python:3.8.16
WORKDIR /account_service
COPY . .
ENV PYTHONPATH /account_service
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 50051
#ENTRYPOINT ["python", "account_service/run.py"]