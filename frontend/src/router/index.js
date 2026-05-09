<!-- router/index.js -->
import { createRouter, createWebHistory } from 'vue-router';
import UserDashboard from '../components/UserDashboard.vue';
import StockChart from '../components/StockChart.vue';
import OrderForm from '../components/OrderForm.vue';

const routes = [
  { path: '/dashboard', component: UserDashboard },
  { path: '/chart', component: StockChart, props: { symbol: 'AAPL', data: [] } },
  { path: '/order', component: OrderForm },
  { path: '/', redirect: '/dashboard' },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
