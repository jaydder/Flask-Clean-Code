FROM python:3.8-alpine
EXPOSE 5000
WORKDIR app
COPY * /app
RUN pip install -r requirements.txt
CMD ["app.py" ]