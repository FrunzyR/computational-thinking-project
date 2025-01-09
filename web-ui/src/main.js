import './assets/main.css'

import {createApp} from 'vue'
import App from './App.vue'
import DriverTable from "@/components/DriverTable.vue";
import CircuitsView from "@/components/CircuitsView.vue";
import {createMemoryHistory, createRouter, createWebHashHistory} from "vue-router";
import PrimeVue from 'primevue/config';
import {AutoComplete, Button, CascadeSelect, Column, DataTable, InputText, Select} from "primevue";
import Aura from '@primevue/themes/aura';
import SimulationsView from "@/components/SimulationsView.vue";
import Chart from "primevue/chart";

const routes = [
    {path: '/', component: DriverTable},
    {path: '/circuits', component: CircuitsView},
    {path: '/results', component: SimulationsView},
]

const router = createRouter({
    history: createWebHashHistory(),
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
    .component('Chart', Chart)
    .component('Select', Select)
    .mount('#app')
