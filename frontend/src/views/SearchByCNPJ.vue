<template>
  <div class="container">
    <router-link to="/" class="btn btn-back">
      <i class="fas fa-arrow-left"></i> Voltar para Home
    </router-link>
    <div class="header">
      <h1>Busca por CNPJ</h1>
      <p>Digite o CNPJ da empresa (apenas números)</p>
    </div>

    <div class="card">
      <SearchBox
        placeholder="Digite o CNPJ da empresa... (apenas números)"
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
import SearchBox from "@/components/SearchBox.vue";
import CompanyTable from "@/components/CompanyTable.vue";
import axios from "axios";

export default {
  name: "SearchByCNPJView",
  components: {
    SearchBox,
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
          "http://127.0.0.1:8000/companies/api/getbycnpj",
          {
            params: { cnpj: term },
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
