#!/bin/sh

docker build -t predictor:1.0 .

docker run -d -p 8093:8093 predictor:1.0 