<script setup>

import DriverTable from "@/components/DriverTable.vue";
import DriverForm from "@/components/DriverForm.vue";
</script>

<template>
  <header>
    <nav class="navbar">
      <RouterLink to="/">Drivers</RouterLink>
      <RouterLink to="/circuits">Circuits</RouterLink>
    </nav>
  </header>

  <main>
    <div>
      <Suspense>
        <RouterView />
      </Suspense>
    </div>
  </main>
</template>

<style scoped>
.navbar{
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  margin-bottom: 100px;
}
</style>
