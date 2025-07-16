<script setup>
import WeatherWidget from './components/WeatherWidget.vue'
</script>

<template>
  <div class="app-bg">
    <h1>Prueba Tecnica Frontend</h1>
    <div class="widget-center">
      <WeatherWidget />
    </div>
  </div>
</template>

<style scoped>
.app-bg {
  min-height: 100vh;
  background: #f5f7fa;
  padding-top: 40px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}
.widget-center {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  min-height: 60vh;
}
h1 {
  margin-bottom: 2rem;
  color: #333;
  text-align: center;
}
</style>
