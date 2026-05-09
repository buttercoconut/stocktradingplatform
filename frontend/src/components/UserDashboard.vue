<template>
  <div>
    <h2>User Dashboard</h2>
    <p>Welcome, {{ user?.name }}</p>
    <div v-if="orders.length">
      <h3>Your Orders</h3>
      <ul>
        <li v-for="order in orders" :key="order.id">
          {{ order.symbol }} - {{ order.quantity }} @ {{ order.price }} ({{ order.side }})
        </li>
      </ul>
    </div>
    <div v-else>
      <p>No orders yet.</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

interface Order {
  id: number;
  symbol: string;
  quantity: number;
  price: number;
  side: string;
}

interface User {
  id: number;
  name: string;
}

const user = ref<User | null>(null);
const orders = ref<Order[]>([]);

const fetchDashboard = async () => {
  try {
    const [userRes, ordersRes] = await Promise.all([
      axios.get('/api/user'),
      axios.get('/api/orders'),
    ]);
    user.value = userRes.data;
    orders.value = ordersRes.data;
  } catch (e) {
    console.error('Failed to load dashboard', e);
  }
};

onMounted(() => fetchDashboard());
</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}
li {
  margin-bottom: 0.5rem;
}
</style>
