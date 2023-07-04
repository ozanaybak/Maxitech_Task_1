# maxitech_1

First of all, it is necessary to make sure that fastapi, uvicorn and docker are already installed and running smoothly. I had to deal with it a lot because I had problems with paths on my computer. Secondly, I kept the Dockerfile and requirements.txt files in the same location with the code I wrote in the main.py file. I first integrated the code I wrote in the main.py file with fastapi. I combined Docker and Fastapi together with the dockerfile and requirements.txt I added later. I started a container in Docker and created an image." http://localhost:8000" I was able to see the outputs from this address.


In the terminal, I entered the following commands in order to start docker, create an image and combine it with fastapi:

1-)docker build -t my-fastapi-app .
2-)docker images
3-)docker run -d -p 8000:8000 my-fastapi-app
