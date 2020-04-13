# pull official base image
FROM python:3.7.0-alpine

WORKDIR /usr/src/app

RUN ls -la
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies

#COPY ./requirements.txt /usr/src/app/requirements.txt
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"


# copy project
COPY . .
RUN ls -la
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
#ENV DB_HOST=postgres
RUN ls -la

CMD [ "./docker-entrypoint.sh" ]
#CMD [ "wsgi.py" ]