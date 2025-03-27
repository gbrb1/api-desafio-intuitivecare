<template>
  <div class="table-container">
    <table v-if="companies.length > 0" class="company-table">
      <thead>
        <tr>
          <th>Razão Social</th>
          <th>CNPJ</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="company in companies" :key="company.cnpj">
          <td>{{ company.nome_fantasia }}</td>
          <td>{{ formatCNPJ(company.cnpj) }}</td>
        </tr>
      </tbody>
    </table>
    <div v-else class="no-results" align="center">
      <i class="fas fa-search-minus"></i>
      <p>Nenhuma empresa encontrada</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "CompanyTable",
  props: {
    companies: {
      type: Array,
      required: true,
    },
  },
  methods: {
    formatCNPJ(cnpj) {
      return cnpj.replace(
        /^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})$/,
        "$1.$2.$3/$4-$5"
      );
    },
  },
};
</script>
