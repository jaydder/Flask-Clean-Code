FROM python:3.8-alpine
EXPOSE 5000
WORKDIR app
COPY * /app
RUN apk update && apk upgrade
RUN apk add --no-cache sqlitebrowser~=3.12.2-r3
RUN pip install -r requirements.txt
CMD ["app.py" ]