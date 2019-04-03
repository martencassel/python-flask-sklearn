#!/bin/sh

docker build -t generate-model:1.0 .

docker run -it --rm -v $(pwd):/usr/src/app generate-model:1.0
