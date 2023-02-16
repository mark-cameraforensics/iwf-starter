## What is this?
A python app with an http api which accepts an image as base64, does some work, then returns a json response. It can be built and run with Docker.

## Run
Run via Docker Compose

`docker compose up`

## Test the API with a sample image

`curl -X POST -H 'Content-Type: application/json' -d @test-request.json http://localhost:5000`