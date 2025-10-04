# Usamos Python 3.12 slim
FROM python:3.12-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos requirements e instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la carpeta app
COPY ./app ./app

# Exponemos el puerto que usará FastAPI
EXPOSE 8000

# Comando para arrancar FastAPI con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
