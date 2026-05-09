<template>
  <div>
    <h2>{{ symbol }} Stock Chart</h2>
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';
import Chart from 'chart.js/auto';

const props = defineProps({
  symbol: { type: String, required: true },
  data: { type: Array as () => Array<{ time: string; price: number }>, required: true },
});

const chartCanvas = ref<HTMLCanvasElement | null>(null);
let chartInstance: Chart | null = null;

const renderChart = () => {
  if (!chartCanvas.value) return;
  const ctx = chartCanvas.value.getContext('2d');
  if (!ctx) return;

  const labels = props.data.map(d => d.time);
  const prices = props.data.map(d => d.price);

  if (chartInstance) chartInstance.destroy();
  chartInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels,
      datasets: [{
        label: `${props.symbol} Price`,
        data: prices,
        borderColor: 'rgba(75,192,192,1)',
        fill: false,
      }],
    },
    options: {
      responsive: true,
      scales: {
        x: { display: true, title: { display: true, text: 'Time' } },
        y: { display: true, title: { display: true, text: 'Price' } },
      },
    },
  });
};

onMounted(() => renderChart());
watch(() => props.data, () => renderChart(), { deep: true });
</script>

<style scoped>
canvas {
  max-width: 100%;
}
</style>
