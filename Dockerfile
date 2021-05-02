FROM python:3.7-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/

RUN sed -i 's/\r//' start.sh
RUN chmod +x start.sh

EXPOSE $PORT:8000

ENTRYPOINT [ "./start.sh" ]