<template>
  <div class="container">
    <h1>Widget del Clima</h1>
    <input
      v-model="city"
      placeholder="Ingresa el nombre de la ciudad"
      @keyup.enter="fetchWeather"
    />
    <button @click="fetchWeather">Consultar clima</button>
    <div v-if="weather" class="weather-info">
      <h2>{{ weather.name }}</h2>
      <p class="temp">Temperatura: {{ weather.main.temp }}°C</p>
      <p class="msg">{{ getWeatherMessage(weather.main.temp) }}</p>
    </div>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const city = ref('')
const weather = ref(null)
const error = ref('')

const getWeatherMessage = (temp) => {
  if (temp < 10) return "Hace frío 🧥"
  if (temp <= 25) return "Clima templado 🌤"
  return "Hace calor ☀️"
}

const fetchWeather = async () => {
  if (!city.value) {
    error.value = 'Por favor ingresa el nombre de una ciudad'
    return
  }

  error.value = ''
  weather.value = null

  try {
    const response = await axios.get(
      `https://api.openweathermap.org/data/2.5/weather?q=${city.value}&appid=${
        import.meta.env.VITE_API_KEY
      }&units=metric`
    )
    weather.value = response.data
  } catch (err) {
    try {
      const response = await axios.get(
        `http://api.weatherapi.com/v1/current.json?key=${
          import.meta.env.VITE_WEATHERAPI_KEY
        }&q=${city.value}`
      )
      weather.value = {
        name: response.data.location.name,
        main: { temp: response.data.current.temp_c }
      }
    } catch (fallbackErr) {
      error.value = 'No se pudo obtener el clima. Intenta de nuevo.'
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

.container {
  max-width: 350px;
  margin: 32px auto;
  padding: 28px 24px 24px 24px;
  text-align: center;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.7);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
  backdrop-filter: blur(12px);
  border: 1.5px solid rgba(255, 255, 255, 0.3);
  font-family: 'Inter', Arial, sans-serif;
  transition: box-shadow 0.3s;
}
.container:hover {
  box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.22);
}
h1 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #222;
  margin-bottom: 1.2rem;
  letter-spacing: 0.02em;
}
input {
  padding: 10px 14px;
  margin: 10px 0 18px 0;
  width: 80%;
  border: none;
  border-radius: 12px;
  background: rgba(240, 240, 240, 0.9);
  font-size: 1rem;
  color: #222;
  outline: none;
  box-shadow: 0 1px 4px 0 rgba(31, 38, 135, 0.06);
  transition: background 0.2s;
}
input:focus {
  background: #fff;
}
button {
  padding: 10px 24px;
  background: linear-gradient(90deg, #4f8cff 0%, #38e0ff 100%);
  color: #fff;
  font-weight: 600;
  font-size: 1rem;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  margin-bottom: 10px;
  box-shadow: 0 2px 8px 0 rgba(31, 38, 135, 0.10);
  transition: background 0.2s, box-shadow 0.2s;
}
button:hover {
  background: linear-gradient(90deg, #38e0ff 0%, #4f8cff 100%);
  box-shadow: 0 4px 16px 0 rgba(31, 38, 135, 0.16);
}
.weather-info {
  margin-top: 18px;
  padding: 18px 0 8px 0;
  border-radius: 16px;
  background: rgba(255,255,255,0.55);
  box-shadow: 0 2px 8px 0 rgba(31, 38, 135, 0.08);
}
.weather-info h2 {
  font-size: 1.2rem;
  font-weight: 600;
  color: #222;
  margin-bottom: 0.5rem;
}
.temp {
  font-size: 2.2rem;
  font-weight: 600;
  color: #007aff;
  margin: 0.2rem 0 0.5rem 0;
}
.msg {
  font-size: 1.1rem;
  color: #333;
  margin-bottom: 0.5rem;
}
.error {
  color: #ff3b30;
  margin-top: 12px;
  font-weight: 600;
  font-size: 1rem;
  letter-spacing: 0.01em;
}
</style>