<template>
  <div class="search-box">
    <input
      class="search-input"
      type="text"
      :placeholder="placeholder"
      v-model="displayValue"
      @input="handleInput"
      ref="inputRef"
      maxlength="18"
    />
  </div>
</template>

<script>
export default {
  name: "SearchBox",
  props: {
    placeholder: {
      type: String,
      default: "00.000.000/0000-00",
    },
    modelValue: {
      type: String,
      default: "",
    },
  },
  emits: ["update:modelValue", "search"],
  data() {
    return {
      displayValue: "",
    };
  },
  methods: {
    cleanCNPJ(cnpj) {
      return cnpj.replace(/\D/g, "");
    },

    formatCNPJ(cnpj) {
      const cleaned = this.cleanCNPJ(cnpj);
      if (cleaned.length <= 2) return cleaned;
      if (cleaned.length <= 5)
        return `${cleaned.slice(0, 2)}.${cleaned.slice(2)}`;
      if (cleaned.length <= 8)
        return `${cleaned.slice(0, 2)}.${cleaned.slice(2, 5)}.${cleaned.slice(
          5
        )}`;
      if (cleaned.length <= 12)
        return `${cleaned.slice(0, 2)}.${cleaned.slice(2, 5)}.${cleaned.slice(
          5,
          8
        )}/${cleaned.slice(8)}`;
      return `${cleaned.slice(0, 2)}.${cleaned.slice(2, 5)}.${cleaned.slice(
        5,
        8
      )}/${cleaned.slice(8, 12)}-${cleaned.slice(12, 14)}`;
    },

    handleInput() {
      const cleaned = this.cleanCNPJ(this.displayValue);
      const limitedValue = cleaned.slice(0, 14);

      this.$emit("update:modelValue", limitedValue);
      this.$emit("search", limitedValue);

      this.displayValue = this.formatCNPJ(limitedValue);

      this.$nextTick(() => {
        this.$refs.inputRef.setSelectionRange(
          this.displayValue.length,
          this.displayValue.length
        );
      });
    },
  },
  watch: {
    modelValue(newVal) {
      if (this.cleanCNPJ(this.displayValue) !== newVal) {
        this.displayValue = this.formatCNPJ(newVal);
      }
    },
  },
  mounted() {
    this.displayValue = this.formatCNPJ(this.modelValue);
  },
};
</script>
