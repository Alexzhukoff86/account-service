FROM python:3.8
WORKDIR /account_service
COPY /account-service .
ENV PYTHONPATH /account_service
RUN pip install --upgrade pip
RUN pip install "git+https://github.com/Alexzhukoff86/book-shared"

EXPOSE 50051
ENTRYPOINT ["python", "account_service/run.py"]