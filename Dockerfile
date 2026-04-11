FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml ./
COPY webapp/ ./webapp/
RUN pip install --upgrade pip && pip install .
EXPOSE 5000
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:5000", "webapp.app:app"]