<script setup>

import DriverTable from "@/components/DriverTable.vue";
import DriverForm from "@/components/DriverForm.vue";
</script>

<template>
  <header>

  </header>

  <main>
    <div>
      <Suspense>
        <DriverTable/>
      </Suspense>
    </div>
  </main>
</template>

<style scoped>
</style>
