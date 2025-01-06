<script setup>
import {ref} from "vue";
import DriverForm from "@/components/DriverForm.vue";

const drivers = ref([])
const searchKey = ref("")

getAllDrivers();

async function getAllDrivers() {
  const result = await fetch('/api/driver')
  drivers.value = await result.json()
}

async function searchDrivers() {
  const result = await fetch('/api/driver/search?key=' + searchKey.value)
  drivers.value = await result.json()
}

const lower = ref("")
const upper = ref("")

async function filterDriverBySkill() {
  const result = await fetch(`/api/driver/filter?lower=${lower.value}&upper=${upper.value}`)
  drivers.value = await result.json()
}

async function removeDriver(number){
  await fetch('/api/driver?number=' + number, {method: 'DELETE'})
  await getAllDrivers()
}

const loadedDriver = ref(null);

function loadDriver(driver){
  loadedDriver.value = driver;
}

</script>

<template>
  <div class="searchBar">
    <input type="text" v-model="searchKey">
    <button @click="searchDrivers">Search</button>
  </div>
  <table>
    <tbody>
    <tr>
      <th>Number</th>
      <th>Name</th>
      <th>Team</th>
      <th>Skill</th>
      <th></th>
    </tr>
    <tr v-for="driver of drivers">
      <td>{{ driver.number }}</td>
      <td>{{ driver.name }}</td>
      <td>{{ driver.team }}</td>
      <td>{{ driver.skill_level }}</td>
      <td>
        <button @click="() => removeDriver(driver.number)">x</button>
        <button @click="() => loadDriver(driver)">Load</button>
      </td>
    </tr>
    </tbody>
  </table>
  <div class="filterBar">
    <label>Lower Value <input type="number" v-model="lower"></label>
    <br>
    <label>Upper Value <input type="number" v-model="upper"></label>
    <button @click="filterDriverBySkill">Filter</button>
  </div>

  <DriverForm @need-refresh="getAllDrivers" :driver="loadedDriver"/>


</template>

<style scoped>
</style>