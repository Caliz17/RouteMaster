# Imagen base
FROM python:3.12-slim

# Node.js para Tailwind
RUN apt-get update && apt-get install -y curl gnupg
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y nodejs build-essential

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements y package.json
COPY requirements.txt .
COPY package.json package-lock.json ./

# Instalar Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Instalar Node dependencies
RUN npm install

# Copiar todo el código del frontend
COPY . .

# Exponer puerto Django
EXPOSE 8000

# Comando por defecto para correr frontend
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
