FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy
WORKDIR app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install allure-pytest
CMD ["pytest", "tests/test_cheq.py"]
