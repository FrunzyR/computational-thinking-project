<script setup>
import {ref} from "vue";
import CircuitForm from "@/components/CircuitForm.vue";

const circuits = ref([])
const searchKey = ref("")
const lower = ref("")
const upper = ref("")

async function getAllCircuits() {
  const result = await fetch('api/circuit')
  circuits.value = await result.json()
}

getAllCircuits()

async function searchCircuit() {
  const result = await fetch('api/circuit/search?key=' + searchKey.value)
  circuits.value = await result.json()
}

async function filterByKm() {
  const result = await fetch(`/api/circuit/filter?lower=${lower.value}&upper=${upper.value}`)
  circuits.value = await result.json()
}

async function sortCircuits() {
  const result = await fetch('/api/circuit/sort', {method: 'GET'})
  circuits.value = await result.json()
}

async function removeCircuit(round) {
  await fetch('/api/circuit?round=' + round, {method: 'DELETE'})
  await getAllCircuits()
}

const loadedCircuit = ref(null);

async function loadCircuit(circuit) {
  loadedCircuit.value = circuit;
}

</script>

<template>
  <div class="container">
    <div>
      <div class="searchBar">
        <InputText type="text" v-model="searchKey"/>
        <Button @click="searchCircuit">Search Circuit</Button>
        <Button @click="sortCircuits">Sort by time</Button>
      </div>
      <table>
        <tbody>
        <tr>
          <th>Round</th>
          <th>Circuit</th>
          <th>Fastest lap</th>
          <th>Length</th>
          <th></th>
        </tr>
        <tr v-for="circuit in circuits">
          <td>{{ circuit.round }}</td>
          <td>{{ circuit.circuit }}</td>
          <td>{{ circuit.fastest_lap }}</td>
          <td>{{ circuit.length_km }}</td>
          <td>
            <Button @click="() => removeCircuit(circuit.round)" label="X" severity="danger"/>
          </td>
          <td>
            <Button @click="() =>loadCircuit(circuit)">Load</Button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
    <div>
      <div class="filterBar">
        <label>Lower length<InputText type="number" v-model="lower"/> </label>
        <label>Upper length<InputText type="number" v-model="upper"/> </label>
        <Button @click="filterByKm">Filter</Button>
        <CircuitForm @need-refresh="getAllCircuits" :circuit="loadedCircuit"/>
      </div>
    </div>
  </div>

</template>

<style scoped>
.container {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: space-between;
}
</style>