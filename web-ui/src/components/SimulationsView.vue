<script setup>
import {onMounted, ref} from "vue";

const viewResult = ref("")
const chartData = ref()
const chartOptions = ref()

const selectedCircuit = ref()
const circuits = ref()

async function getAllCircuits() {
  const result = await fetch('/api/circuit')
  circuits.value = await result.json()
  selectedCircuit.value = circuits.value[0]
}

onMounted(async () => {
  await getAllCircuits();
  await getSimulationResult()

  chartData.value = setChartData();
  chartOptions.value = setChartOptions();

  console.log(viewResult.value)
  console.log(chartData.value)
});

const setChartData = () => {
  const documentStyle = getComputedStyle(document.documentElement);
  return {
    labels: viewResult.value.drivers_names,
    datasets: [
      {
        label: 'Avarage Lap Time',
        backgroundColor: documentStyle.getPropertyValue('--p-cyan-500'),
        borderColor: documentStyle.getPropertyValue('--p-cyan-500'),
        data: viewResult.value.results
      },
    ]
  };
};
const setChartOptions = () => {
  const documentStyle = getComputedStyle(document.documentElement);
  const textColor = documentStyle.getPropertyValue('--p-text-color');
  const textColorSecondary = documentStyle.getPropertyValue('--p-text-muted-color');
  const surfaceBorder = documentStyle.getPropertyValue('--p-content-border-color');

  return {
    plugins: {
      legend: {
        labels: {
          color: textColor
        }
      }
    },
    scales: {
      x: {
        ticks: {
          color: textColorSecondary,
        },
        grid: {
          display: false,
          drawBorder: false
        }
      },
      y: {
        beginAtZero: false,
        ticks: {
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder,
          drawBorder: false
        }
      }
    }
  };
}

async function getSimulationResult() {
  const result = await fetch('/api/result_simulate?round=' + selectedCircuit.value.round)
  viewResult.value = await result.json();

  chartData.value = setChartData();
  chartOptions.value = setChartOptions();
}

</script>

<template>
  <div v-if="circuits">
    <h1>Lap Timing Data for each Driver </h1>
    <br>
    <div>
      <Select v-model="selectedCircuit" :options="circuits" option-label="circuit" @change="getSimulationResult"/>
    </div>
    <br>
    <div class="card">
      <Chart type="bar" :data="chartData" :options="chartOptions"/>
    </div>
  </div>
</template>

<style scoped>
.card {
  height: 800px;
}
</style>