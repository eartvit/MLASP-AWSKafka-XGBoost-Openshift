FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000

# Define environment variable
ENV MODEL_NAME TestXGB
ENV SERVICE_TYPE MODEL

CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE
