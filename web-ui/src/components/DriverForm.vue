<script setup>
import {ref, watch} from "vue";

const emit = defineEmits(['needRefresh'])
const props = defineProps({
  driver: Object
})

const number = ref("")
const name = ref("")
const team = ref("")
const skill = ref("")

watch(() => props.driver, () => {
  number.value = props.driver.number
  name.value = props.driver.name
  team.value = props.driver.team
  skill.value = props.driver.skill_level
})

async function updateDriver() {
  const body = {
    name: name.value,
    team: team.value,
    number: number.value,
    skill_level: skill.value,
  }
  const result = await fetch('/api/driver', {
    method: 'PUT',
    body: JSON.stringify(body),
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    }
  })

  emit('needRefresh')
}

async function addDriver() {
  const body = {
    name: name.value,
    team: team.value,
    number: number.value,
    skill_level: skill.value,
  }
  const result = await fetch('/api/driver', {
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
  <form>
    <label>Number</label>
    <br>
    <InputText type="text" v-model="number"/>
    <br>

    <label>Name</label>
    <br>
    <InputText type="text" v-model="name"/>
    <br>

    <label>Team</label>
    <br>
    <InputText type="text" v-model="team"/>
    <br>

    <label>Skill Level</label>
    <br>
    <InputText type="number" v-model="skill"/>
    <br>
  </form>
  <Button type="button" @click="addDriver">Add</Button>
  <Button type="button" @click="updateDriver">Update</Button>
</template>

<style scoped>

</style>