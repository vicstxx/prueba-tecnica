# Prueba Técnica - Frontend y Backend

Este repositorio contiene la implementación completa de la prueba técnica, dividida en dos partes independientes:

## 📁 Estructura del Proyecto

```
prueba-tecnica/
├── weather-widget/     # Frontend - Widget del Clima (Vue 3)
└── backend/           # Backend - API de Encuestas (FastAPI + PostgreSQL)
```

---

## 🎯 Frontend - Weather Widget

### Descripción
Widget del clima desarrollado con Vue 3 y Vite, que permite consultar el clima de cualquier ciudad usando APIs públicas.

### Tecnologías
- Vue 3 (Composition API)
- Vite
- Axios
- APIs: OpenWeatherMap + WeatherAPI (fallback)

### Cómo ejecutar

1. **Navegar al directorio del frontend:**
   ```bash
   cd weather-widget
   ```

2. **Instalar dependencias:**
   ```bash
   npm install
   ```

3. **Configurar variables de entorno:**
   Crear archivo `.env` en la raíz del proyecto:
   ```
   VITE_API_KEY=tu_clave_de_openweathermap
   VITE_WEATHERAPI_KEY=tu_clave_de_weatherapi
   ```

4. **Ejecutar el servidor de desarrollo:**
   ```bash
   npm run dev
   ```

5. **Abrir en el navegador:**
   ```
   http://localhost:5173
   ```

### Funcionalidades
- Consulta del clima por ciudad
- Fallback automático entre APIs
- Diseño moderno inspirado en widgets de Apple
- Fuente del sistema nativa

---

## 🔧 Backend - Survey API

### Descripción
API RESTful para gestión de encuestas, desarrollada con FastAPI y PostgreSQL.

### Tecnologías
- FastAPI (Python 3.10+)
- PostgreSQL
- SQLAlchemy
- Docker & Docker Compose

### Cómo ejecutar

1. **Navegar al directorio del backend:**
   ```bash
   cd backend
   ```

2. **Ejecutar con Docker (recomendado):**
   ```bash
   docker-compose up --build
   ```

3. **Acceder a la documentación:**
   ```
   http://localhost:8000/docs
   ```

### Endpoints disponibles

- `POST /surveys` - Crear una nueva encuesta
- `POST /surveys/{survey_id}/questions` - Agregar pregunta a una encuesta
- `POST /questions/{question_id}/options` - Agregar opción a una pregunta

### Tipos de preguntas soportados
- `text` - Pregunta de texto abierto
- `single_choice` - Pregunta de opción única
- `multiple_choice` - Pregunta de opción múltiple

---

## 🚀 Ejecución Completa

### Opción 1: Ejecutar ambos proyectos por separado

1. **Terminal 1 - Frontend:**
   ```bash
   cd weather-widget
   npm install
   npm run dev
   ```

2. **Terminal 2 - Backend:**
   ```bash
   cd backend
   docker-compose up --build
   ```

### Opción 2: Usar scripts (si están disponibles)

```bash
# Frontend
npm run dev:frontend

# Backend
npm run dev:backend
```

---

## 📋 Requisitos Previos

### Para el Frontend:
- Node.js (v16 o superior)
- npm

### Para el Backend:
- Docker y Docker Compose
- O Python 3.10+ y PostgreSQL (para ejecución local)

---

## 🔑 Configuración de APIs

### Frontend (Weather Widget)
Obtener claves gratuitas de:
- [OpenWeatherMap](https://openweathermap.org/api)
- [WeatherAPI](https://www.weatherapi.com/)

### Backend (Survey API)
No requiere claves externas, usa base de datos local.

---