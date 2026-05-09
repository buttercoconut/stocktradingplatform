<!-- App.vue -->
<template>
  <div>
    <nav>
      <router-link to="/dashboard">Dashboard</router-link> |
      <router-link to="/chart">Chart</router-link> |
      <router-link to="/order">Order</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script setup lang="ts">
// No script needed for this simple layout
</script>
