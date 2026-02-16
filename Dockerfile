FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml ./
COPY webapp/ ./webapp/
RUN pip install --upgrade pip && pip install .
EXPOSE 5000
CMD ["flask", "--app", "webapp.app", "run", "--host=0.0.0.0"]