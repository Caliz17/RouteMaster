# Usamos Python 3.12 slim
FROM python:3.12-slim

# Establecemos directorio de trabajo
WORKDIR /app

# Copiamos requirements e instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código al contenedor
COPY . .

# Exponemos el puerto de Django
EXPOSE 8000

# Comando para correr Django en modo desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
