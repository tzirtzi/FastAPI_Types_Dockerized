FROM python:3.8-slim

LABEL maintainer="Tzirtzilakis George <tzirtzi@gmail.com>"

RUN pip install --no-cache-dir "uvicorn[standard]" gunicorn \
	&& pip install --no-cache-dir fastapi

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./gunicorn_conf.py /gunicorn_conf.py

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 80

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]