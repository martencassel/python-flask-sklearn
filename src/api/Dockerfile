FROM python:3-alpine

WORKDIR /usr/src/app

#RUN apk update && apk add gcc gfortran musl-dev freetype-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]