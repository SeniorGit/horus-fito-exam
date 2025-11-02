<script setup>
import { ref, watch, defineProps, defineEmits } from 'vue'

const props = defineProps({
  placeholder: {
    type: String,
    default: 'Cari..'
  }
})

const emit = defineEmits(['search', 'refresh'])
const searchKeyword = ref('')
let searchTimeout = null

watch(searchKeyword, (newVal) => {
  clearTimeout(searchTimeout)
  if (newVal.length === 0 || newVal.length >= 1) {
    searchTimeout = setTimeout(() => {
      emit('search', newVal)
    }, 500)
  }
})

const handleSearch = () => {
  clearTimeout(searchTimeout)
  emit('search', searchKeyword.value)
}

</script>

<template>
  <div class="search-section">
    <div class="search-box">
      <input 
        v-model="searchKeyword" 
        @keyup.enter="handleSearch"
        :placeholder="placeholder"
        type="search"
      >
      <button 
        @click="handleSearch" 
        class="btn-search"
      >
        Search
      </button>
    </div>
  </div>
</template>

<style scoped>
.search-section {
  display: flex;
  gap: 15px;
  align-items: flex-start;
}

.search-box {
  display: flex;
  gap: 8px;
  align-items: center;
}

.search-box input {
  padding: 10px 12px;
  border: 2px solid #e1e5e9;
  border-radius: 6px;
  min-width: 300px;
  font-size: 14px;
  transition: border-color 0.3s;
}

.btn-search {
  padding: 10px 16px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s;
  white-space: nowrap;
}

.btn-search {
  background-color: #4CAF50;
  color: white;
}

.btn-search:hover:not(:disabled) {
  background-color: #45a049;
}

.btn-search:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>