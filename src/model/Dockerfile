FROM python:3.6-alpine


RUN apk update && \
	apk add --no-cache \
    # bash \
    libstdc++ \
    libgomp \
    build-base \
    cmake \
    gfortran \
    libpng && \
    ln -s locale.h /usr/include/xlocale.h && \
    apk add --no-cache --virtual .build-deps \
    lapack-dev \
    musl-dev \
    python3-dev \
    jpeg-dev \
    freetype-dev \
    libffi-dev \
    openssl-dev \
    g++ && \
    pip install --no-cache-dir \
    numpy==1.14.2 \
    scipy==1.0.1 \
    scikit-learn==0.19.1 \
    pandas==0.22.0 \
    matplotlib==2.2.2 \
    py-multibase==0.1.2 \
    wheel \
    lightgbm

# apk add openssl-dev==1.1.1b-r1

WORKDIR /usr/src/app

#RUN apk update && apk add gcc gfortran musl-dev freetype-dev

COPY . .

CMD [ "python", "model.py" ]
