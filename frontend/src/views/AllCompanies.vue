<template>
  <div class="container">
    <router-link to="/" class="btn btn-back">
      <i class="fas fa-arrow-left"></i> Voltar para Home
    </router-link>
    <div class="header">
      <h1>Todas as Empresas</h1>
      <p>Lista completa de empresas cadastradas</p>
    </div>

    <div class="card">
      <div v-if="loading" class="loader"></div>
      <div v-else-if="error" class="error">{{ error }}</div>
      <CompanyTable v-else :companies="companies" />
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import CompanyTable from "@/components/CompanyTable.vue";
import axios from "axios";

export default {
  name: "AllCompaniesView",
  components: {
    CompanyTable,
  },
  setup() {
    const companies = ref([]);
    const loading = ref(true);
    const error = ref(null);

    const fetchAllCompanies = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/companies/api/getall"
        );
        companies.value = response.data;
      } catch (err) {
        error.value = "Erro ao carregar empresas: " + err.message;
      } finally {
        loading.value = false;
      }
    };

    onMounted(fetchAllCompanies);

    return {
      companies,
      loading,
      error,
    };
  },
};
</script>
