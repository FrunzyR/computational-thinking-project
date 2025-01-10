<script setup>
import {ref, watch} from "vue";

const emit = defineEmits(['needRefresh'])
const props = defineProps({
  circuit: Object
})

const round = ref("")
const circuit = ref("")
const fastest_lap = ref("")
const length_km = ref("")

watch(() => props.circuit, () => {
  round.value = props.circuit.round
  circuit.value = props.circuit.circuit
  fastest_lap.value = props.circuit.fastest_lap
  length_km.value = props.circuit.length_km
})

async function updateCircuit() {
  const body = {
    round: round.value,
    circuit: circuit.value,
    fastest_lap: fastest_lap.value,
    length_km: length_km.value,
  }
  const result = await fetch('/api/circuit', {
    method: 'PUT',
    body: JSON.stringify(body),
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    }
  })
  emit('needRefresh')
}

async function addCircuit() {
  const body = {
    round: round.value,
    circuit: circuit.value,
    fastest_lap: fastest_lap.value,
    length_km: length_km.value,
  }
  const result = await fetch('/api/circuit', {
    method: 'POST',
    body: JSON.stringify(body),
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    }
  })
  emit('needRefresh')

}


</script>

<template>
  <Card>
    <template #header>
      <h1>Circuit Form</h1>
    </template>
    <template #content>
      <form class="flex flex-column">
        <label>Round</label>
        <InputText type="number" v-model="round"/>
        <label>Circuit</label>
        <InputText type="text" v-model="circuit"/>
        <label>Fastest lap</label>
        <InputText type="text" v-model="fastest_lap"/>
        <label>Length</label>
        <InputText type="number" v-model="length_km"/>
      </form>
    </template>
    <template #footer>
      <div class="flex gap-3">
        <Button type="button" @click="addCircuit">Add</Button>
        <Button type="button" @click="updateCircuit">Update</Button>
      </div>
    </template>
  </Card>

</template>

<style scoped>

</style>