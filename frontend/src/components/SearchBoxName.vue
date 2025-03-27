<template>
  <div class="search-box">
    <input
      class="search-input"
      type="text"
      placeholder="Digite o nome da empresa..."
      v-model="inputValue"
      @input="handleInput"
    />
  </div>
</template>

<script>
export default {
  name: "SearchBoxName",
  emits: ["search"],
  data() {
    return {
      inputValue: "",
    };
  },
  methods: {
    handleInput() {
      this.$emit("search", this.inputValue);
    },
  },
};
</script>
