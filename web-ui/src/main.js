import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import DriverTable from "@/components/DriverTable.vue";
import CircuitsView from "@/components/CircuitsView.vue";
import {createMemoryHistory, createRouter} from "vue-router";
import PrimeVue from 'primevue/config';
import {Button, Column, DataTable, InputText} from "primevue";
import Aura from '@primevue/themes/aura';

const routes = [
  { path: '/', component: DriverTable },
  { path: '/circuits', component: CircuitsView },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

createApp(App)
    .use(router)
    .use(PrimeVue, {
      theme: {
        preset: Aura,
    }
    })
    .component('Button', Button)
    .component('InputText', InputText)
    .component('DataTable', DataTable)
    .component('Column', Column)
    .mount('#app')
