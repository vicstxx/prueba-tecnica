import { createRouter, createWebHistory } from 'vue-router';
import WeatherWidget from '../components/WeatherWidget.vue';

const routes = [
  { path: '/weather', name: 'Weather', component: WeatherWidget },
  { path: '/', redirect: '/weather' },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;