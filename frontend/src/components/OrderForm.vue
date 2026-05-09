<template>
  <div>
    <h2>{{ symbol }} Order Form</h2>
    <form @submit.prevent="submitOrder">
      <label>
        Symbol:
        <input v-model="symbol" required />
      </label>
      <label>
        Quantity:
        <input type="number" v-model.number="quantity" min="1" required />
      </label>
      <label>
        Price:
        <input type="number" v-model.number="price" step="0.01" required />
      </label>
      <label>
        Side:
        <select v-model="side">
          <option value="buy">Buy</option>
          <option value="sell">Sell</option>
        </select>
      </label>
      <button type="submit">Place Order</button>
    </form>
    <p v-if="status">Status: {{ status }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const symbol = ref('AAPL');
const quantity = ref(10);
const price = ref(150.0);
const side = ref('buy');
const status = ref('');

const submitOrder = async () => {
  try {
    const response = await axios.post('/api/order', {
      symbol: symbol.value,
      quantity: quantity.value,
      price: price.value,
      side: side.value,
    });
    status.value = response.data.message;
  } catch (e) {
    status.value = 'Error placing order';
  }
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
label {
  display: flex;
  flex-direction: column;
}
button {
  margin-top: 0.5rem;
}
</style>
