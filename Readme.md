# Maybe you need to refresh GCloud credentials first

gcloud auth login

# Build this project: 

docker build -f python3.8-alpine3.10.dockerfile -t marbbl:FastAPI_types_example .
-- Notice that for production you may need to change log level to error 
-- or at least warning in 'gunicorn_conf.py'. 

# Run the image: 

docker run -p 8000:80 marbbl:FastAPI_types_example
-- feel free to run to whatever port externally, to change the internal port 80  
-- change the 'gunicorn_conf.py' AND the EXPOSE command in .dockerfile 

# Open your browser

Open your browser at http://127.0.0.1:8000

There is a swagger-powered api documentation in http://127.0.0.1:8000/docs

And also an Alternative API documentation with ReDoc http://127.0.0.1:8000/redoc

# More info (from the creator of Fast API and maintener of base Docker images)

https://fastapi.tiangolo.com/
