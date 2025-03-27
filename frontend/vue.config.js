const { defineConfig } = require("@vue/cli-service");
module.exports = {
  chainWebpack: (config) => {
    config.plugin("html").tap((args) => {
      args[0].title = "Consulta de Empresas | IntuitiveCare"; // Altere aqui
      return args;
    });
  },
};
