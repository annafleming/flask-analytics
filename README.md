# Flask data analytics app

- To build the image run `docker build -t flask-analytics .` from the project directory
- Run the container with `docker run -id -p 5000:5000 -v /local/path/to/flask-analytics:/opt/flask-analytics --name flask-analytics-app flask-analytics`
- Stop the container using `docker stop flask-analytics-app`
- Restart the server with `docker start flask-analytics-app`
- You can log in to the server using `docker exec -it flask-analytics-app bash`