# Survey API Backend

Este backend implementa una API RESTful para la gestión de encuestas, usando FastAPI y PostgreSQL. El entorno está preparado para ejecutarse fácilmente con Docker y docker-compose.

## Tecnologías principales
- FastAPI (Python 3.10+)
- PostgreSQL
- Docker & docker-compose

## Estructura del proyecto

```
backend/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   └── routers/
│       └── survey.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## ¿Cómo levantar el backend?

1. Asegúrate de tener Docker y docker-compose instalados.
2. Desde la carpeta `backend/`, ejecuta:
   ```bash
   docker-compose up --build
   ```
3. La API estará disponible en: http://localhost:8000/docs

---

A continuación se generará el código y la estructura completa del backend siguiendo las mejores prácticas y los requisitos de la prueba técnica. 