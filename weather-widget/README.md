# Weather Widget - Prueba Técnica Frontend

## Descripción

Este proyecto es una base sólida para un widget del clima, desarrollado con Vue 3 y Vite. El objetivo principal es demostrar buenas prácticas de arquitectura, claridad en el código y escalabilidad, más allá de la cantidad de funcionalidades implementadas.

---

## Enfoque y Decisiones Técnicas

- **Abstracción y Componentización:**  
  El widget del clima está encapsulado en un componente reutilizable (`WeatherWidget.vue`), lo que facilita su mantenimiento y extensión.
- **Escalabilidad:**  
  La estructura del proyecto permite agregar fácilmente nuevos componentes, servicios o vistas. El router está preparado para futuras rutas.
- **Buenas prácticas:**  
  Uso de variables de entorno para las claves de API, separación de estilos, y código claro y comentado.
- **Stack Moderno:**  
  Vue 3 + Vite para un desarrollo rápido, eficiente y compatible con las mejores prácticas actuales.
- **Estilo Moderno:**  
  Inspirado en los widgets de Apple, con fuente del sistema y diseño limpio.

---

## Estructura del Proyecto

```
frontend/weather-widget/
├── src/
│   ├── components/
│   │   └── WeatherWidget.vue
│   ├── router/
│   │   └── index.js
│   ├── App.vue
│   ├── main.js
│   └── style.css
├── public/
├── package.json
└── vite.config.js
```

---

## Requisitos Previos

- Node.js (v16 o superior recomendado)
- npm

---

## Instalación y Ejecución

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/vicstxx/prueba-tecnica.git
   cd frontend/weather-widget
   ```

2. **Instala las dependencias**
   ```bash
   npm install
   ```

3. **Configura las variables de entorno**
   Crea un archivo `.env` en la raíz del proyecto con tus claves de API:
   ```
   VITE_API_KEY=tu_clave_de_openweathermap
   VITE_WEATHERAPI_KEY=tu_clave_de_weatherapi
   ```

4. **Ejecuta el servidor de desarrollo**
   ```bash
   npm run dev
   ```
   Abre la URL que te indique la terminal (por defecto http://localhost:5173).

---

## ¿Por qué esta arquitectura es escalable?

- **Componentes desacoplados:** Puedes agregar más widgets o vistas fácilmente.
- **Preparado para rutas:** El router está listo para futuras vistas.
- **Fácil de migrar a TypeScript:** La estructura es compatible.
- **Estilos y fuentes globales:** Permite mantener una identidad visual consistente y fácil de modificar.

---
