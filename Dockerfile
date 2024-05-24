FROM python:3.11.5

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

CMD python3 run.py