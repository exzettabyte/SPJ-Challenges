FROM python:alpine3.7

WORKDIR /var/www

COPY ./app /var/www
COPY flag /flag
RUN pip install Flask==1.1.2
RUN adduser -D -g '' www
USER www
ENTRYPOINT ["python"]
CMD ["app.py"]
