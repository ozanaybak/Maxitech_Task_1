# maxitech_1

First of all, it is necessary to make sure that fastapi, uvicorn and docker are already installed and running smoothly. I had to deal with it a lot because I had problems with paths on my computer. Secondly, I kept the Dockerfile and requirements.txt files in the same location with the code I wrote in the main.py file. I first integrated the code I wrote in the main.py file with fastapi. I combined Docker and Fastapi together with the dockerfile and requirements.txt I added later. I started a container in Docker and created an image." http://localhost:8000" I was able to see the outputs from this address.


In the terminal, I entered the following commands in order to start docker, create an image and combine it with fastapi:

1-)docker build -t my-fastapi-app .
2-)docker images
3-)docker run -d -p 8000:8000 my-fastapi-app



As the second part of the project, I tried to capture the information about 848 companies in total, which are not visible on the first page but can only be accessed with the search button on the site, and display them in a json file and FastApi. For this, first, after converting the cURL code to Python on the search button on the site, I sent many queries in a loop and reached the companies suggested in the search button and found their ids. I have stored these ids in a list. Secondly, I tried to print the information of all ids and therefore all companies to the .json file, respectively, in accordance with the desired parameters, by giving the id information in this list to the id parameter in a loop, through the python code of the cURL of the GraphQL file, where I had access to the detailed information of the companies.
