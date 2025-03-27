<template>
  <div class="container">
    <router-link to="/" class="btn btn-back">
      <i class="fas fa-arrow-left"></i> Voltar para Home
    </router-link>
    <div class="header">
      <h1>Busca por Nome</h1>
      <p>Digite parte do nome fantasia da empresa</p>
    </div>

    <div class="card">
      <SearchBoxName
        placeholder="Digite o nome da empresa..."
        v-model="searchTerm"
        @search="searchCompanies"
      />

      <div v-if="loading" class="loader"></div>
      <div v-else-if="error" class="error">{{ error }}</div>
      <CompanyTable v-else :companies="companies" />
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import SearchBoxName from "@/components/SearchBoxName.vue";
import CompanyTable from "@/components/CompanyTable.vue";
import axios from "axios";

export default {
  name: "SearchByNameView",
  components: {
    SearchBoxName,
    CompanyTable,
  },
  setup() {
    const searchTerm = ref("");
    const companies = ref([]);
    const loading = ref(false);
    const error = ref(null);

    const searchCompanies = async (term) => {
      if (!term) {
        companies.value = [];
        return;
      }

      try {
        loading.value = true;
        error.value = null;
        const response = await axios.get(
          "http://127.0.0.1:8000/companies/api/search",
          {
            params: { name: term },
          }
        );
        companies.value = response.data;
      } catch (err) {
        error.value = "Erro ao buscar empresas: " + err.message;
      } finally {
        loading.value = false;
      }
    };

    return {
      searchTerm,
      companies,
      loading,
      error,
      searchCompanies,
    };
  },
};
</script>
