FROM python:3.7.0-alpine

WORKDIR /usr/src/app

RUN ls -la
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"

# copy project, install dependencies, expose port
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000

CMD [ "./docker-entrypoint.sh" ]
