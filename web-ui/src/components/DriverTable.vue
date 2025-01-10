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

async function removeDriver(number) {
  await fetch('/api/driver?number=' + number, {method: 'DELETE'})
  await getAllDrivers()
}

const loadedDriver = ref(null);

function loadDriver(driver) {
  loadedDriver.value = driver;
}

async function sortDrivers() {
  const result = await fetch('/api/driver/sort', {method: 'GET'})
  drivers.value = await result.json()
}

</script>

<template>
  <div class="container">
    <div>

      <div class="searchBar flex flex-row justify-content-between">
        <InputText type="text" v-model="searchKey"/>
        <Button @click="searchDrivers">Search</Button>
        <Button @click="sortDrivers">Sort</Button>
      </div>

      <table>
        <tbody>
        <tr>
          <th>Number</th>
          <th>Name</th>
          <th>Team</th>
          <th>Skill</th>
          <th>Delete</th>
          <th>Modify</th>
        </tr>
        <tr v-for="driver of drivers">
          <td>{{ driver.number }}</td>
          <td>{{ driver.name }}</td>
          <td>{{ driver.team }}</td>
          <td>{{ driver.skill_level }}</td>
          <td>
            <Button @click="() => removeDriver(driver.number)" label="x" severity="danger"/>
          </td>
          <td>
            <Button @click="() => loadDriver(driver)" severity="secondary">Load</Button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>

    <div>
      <Card>
        <template #title>
          <h1>Filter</h1>
        </template>
        <template #content>
          <label>Lower Value
            <InputText type="number" v-model="lower"/>
          </label>
          <br>
          <label>Upper Value
            <InputText type="number" v-model="upper"/>
          </label>
        </template>
        <template #footer>
          <Button @click="filterDriverBySkill">Filter</Button>
        </template>
      </Card>

      <DriverForm @need-refresh="getAllDrivers" :driver="loadedDriver"/>
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

.searchBar {
  margin-bottom: 10%;
}
</style>