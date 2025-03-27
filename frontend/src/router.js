import { createRouter, createWebHistory } from "vue-router";
import HomeView from "./views/Home.vue";
import SearchByNameView from "./views/SearchByName.vue";
import SearchByCNPJView from "./views/SearchByCNPJ.vue";
import AllCompaniesView from "./views/AllCompanies.vue";

const routes = [
  { path: "/", name: "Home", component: HomeView },
  {
    path: "/search-by-name",
    name: "SearchByName",
    component: SearchByNameView,
  },
  {
    path: "/search-by-cnpj",
    name: "SearchByCNPJ",
    component: SearchByCNPJView,
  },
  { path: "/all-companies", name: "AllCompanies", component: AllCompaniesView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
