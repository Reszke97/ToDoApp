FROM python:3.9
WORKDIR /backend
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["/bin/sh"]
CMD ["runMigrations.sh"]