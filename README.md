# edrilling test task

This is test task which described in file interviewassignment.md

But at the same time I tryid to create little meta-frimework for my future
tasks where it will be nessecary to deploy some model or somthing logic to
separate endpoint.
If new logic take some time, please add Redis and Celety tasks

Before using in a server, please add specific env files with sensitive 
information to .gitignore
How it works:
1. In .env you can define host and port of this endpoint
2. In docker-compose.yml choose which settings set you will use before building
    .env_dev OR
    .env_prod OR
    .env_test
3. Also in docker-compose.yml you can chose how many workers will be run
    --workers=2 (2 in this example)
4. After that in project folder do:
    docker-compose build
    docker-compose up
5. Now you can test you API in host_name/docs

For next projects.
1. Define endpoints in folder app/api/api_v1/endpoints here just call 
    related logic and process answer
2. Add routs in app/api/api_v1/api.py
3. Add objects which is neccesary for API to this folder app/schemas
4. Add main logic related to endpoints to app/tasks

