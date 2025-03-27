<template>
  <div class="container">
    <div class="header">
      <h1>Consulta de Empresas</h1>
      <p>Selecione o tipo de consulta que deseja realizar</p>
    </div>

    <div class="card home-card">
      <div class="button-group">
        <router-link to="/search-by-name" class="btn btn-primary">
          <i class="fas fa-search"></i> Buscar por Nome
        </router-link>
        <router-link to="/search-by-cnpj" class="btn btn-primary">
          <i class="fas fa-id-card"></i> Buscar por CNPJ
        </router-link>
        <router-link to="/all-companies" class="btn btn-primary">
          <i class="fas fa-list"></i> Todas as Empresas
        </router-link>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "HomeView",
};
</script>
