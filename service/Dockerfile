FROM python:3

WORKDIR /app

COPY . /app


RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r req.txt

COPY /service/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY /service/run /backend-run
RUN sed -i 's/\r$//g' /backend-run
RUN chmod +x /backend-run