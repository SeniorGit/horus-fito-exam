<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getData } from '@/services/api'
import { useAuthStore } from '@/store/auth'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()

// from data
const form = ref({
  nama: '',
  email: '', 
  username: ''
})

const loading = ref(false)
const error = ref('')
const success = ref('')

const loadUserData = async () => {
  const userId = route.params.id
  
  if (!userId) {
    error.value = 'User ID tidak valid'
    return
  }

  loading.value = true
  try {
    const response = await getData.getUserById(userId)
    const data = response.data
    
    if (data.success) {
      form.value = {
        nama: data.data.nama || data.data.full_name || '',
        email: data.data.email || '',
        username: data.data.username || ''
      }
    } else {
      error.value = data.message || 'Gagal memuat data user'
    }
  } catch (err) {
    error.value = err.response?.data?.message || 'Terjadi kesalahan'
  } finally {
    loading.value = false
  }
}

const validateForm = () => {
  error.value = ''
  
  if (!form.value.nama.trim()) {
    error.value = 'Nama lengkap harus diisi'
    return false
  }
  
  if (!form.value.email.trim()) {
    error.value = 'Email harus diisi'
    return false
  }
  
  if (!form.value.username.trim()) {
    error.value = 'Username harus diisi'
    return false
  }
  
  return true
}

const handleUpdate = async () => {
  if (!validateForm()) return
  
  loading.value = true
  success.value = ''
  error.value = ''
  
  try {
    const userId = route.params.id
    const response = await getData.update(userId, form.value)
    const data = response.data

    if (data.success) {
      success.value = data.message || 'Data user berhasil diupdate!'
      if (authStore.user?.id === parseInt(userId)) {
        authStore.user = { ...authStore.user, ...form.value }
      }
      
      setTimeout(() => {
        router.push('/dashboard')
      }, 2000)
    } else {
      error.value = data.message || 'Gagal mengupdate user'
    }
  } catch (err) {
    error.value = err.response?.data?.message || 'Terjadi kesalahan saat update'
  } finally {
    loading.value = false
  }
}

const handleBack = () => {
  router.push('/dashboard')
}

onMounted(() => {
  loadUserData()
})
</script>

<template>
  <div class="update-container">
    <div class="update-card">
      <h2 class="title">UPDATE USER</h2>
      
      <div v-if="success" class="success-message">
        {{ success }}
      </div>

      <div v-if="error" class="error-message">
        {{ error }}
      </div>

      <form @submit.prevent="handleUpdate" class="update-form">
        <div class="form-row">
          <label class="inline-label">Nama Lengkap:</label>
          <input 
            type="text" 
            v-model="form.nama"
            required
            :disabled="loading"
            class="inline-input"
          >
        </div>

        <div class="form-row">
          <label class="inline-label">Email:</label>
          <input 
            type="email" 
            v-model="form.email"
            required
            :disabled="loading"
            class="inline-input"
          >
        </div>

        <div class="form-row">
          <label class="inline-label">Username:</label>
          <input 
            type="text" 
            v-model="form.username"
            required
            :disabled="loading"
            class="inline-input"
          >
        </div>

        <div class="button-group">
          <button 
            type="submit" 
            :disabled="loading"
            class="update-btn"
          >
            {{ loading ? 'Updating...' : 'Update' }}
          </button>
          <button 
            type="button" 
            @click="handleBack"
            :disabled="loading"
            class="back-btn"
          >
            Kembali
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.update-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f5f5;
  padding: 20px;
}

.update-card {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 450px;
}

.title {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
  font-size: 24px;
  font-weight: bold;
}

.update-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.inline-label {
  font-weight: 500;
  color: #333;
  font-size: 16px;
  min-width: 120px; 
}

.inline-input {
  flex: 1;
  padding: 10px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  box-sizing: border-box;
}

.inline-input:focus {
  outline: none;
  border-color: #4CAF50;
}

.inline-input:disabled {
  background-color: #f5f5f5;
  cursor: not-allowed;
}

.button-group {
  display: flex;
  gap: 15px;
  margin-top: 20px;
}

.button-group button {
  flex: 1;
}

.update-btn {
  background: #4CAF50;
  color: white;
  border: none;
  padding: 12px;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.3s;
}

.update-btn:hover:not(:disabled) {
  background: #45a049;
}

.update-btn:disabled {
  background: #cccccc;
  cursor: not-allowed;
}

.back-btn {
  background: transparent;
  color: #666;
  border: 1px solid #ddd;
  padding: 12px;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s;
}

.back-btn:hover {
  background: #f5f5f5;
}

.success-message {
  background-color: #e8f5e8;
  color: #2e7d32;
  padding: 12px 16px;
  border-radius: 6px;
  margin-bottom: 20px;
  border-left: 4px solid #2e7d32;
}

.error-message {
  background-color: #ffebee;
  color: #c62828;
  padding: 12px 16px;
  border-radius: 6px;
  margin-bottom: 20px;
  border-left: 4px solid #c62828;
}


@media (max-width: 480px) {
  .update-card {
    padding: 30px 20px;
  }
  
  .form-row {
    flex-direction: column;
    align-items: stretch;
    gap: 5px;
  }
  
  .inline-label {
    min-width: auto;
  }
  
  .button-group {
    flex-direction: column;
    gap: 10px;
  }
}
</style>