<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { authApi } from '@/services/api'  

const router = useRouter()

const form = ref({
  nama: '',
  email: '', 
  username: '',
  password: ''
})

const errors = ref({})
const loading = ref(false)

const validateForm = () => {
  errors.value = {}

  if (!form.value.nama.trim()) {
    errors.value.nama = 'Nama dibutuhkan'
  }

  if (!form.value.email.trim()) {
    errors.value.email = 'Email dibutuhkan'
  } else if (!isValidEmail(form.value.email)) {
    errors.value.email = 'Email tidak valid'
  }

  if (!form.value.username.trim()) {
    errors.value.username = 'Username dibutuhkan'
  }

  if (!form.value.password) {
    errors.value.password = 'Password dibutuhkan'
  } else if (form.value.password.length < 6) {
    errors.value.password = 'Password minimal 6 karakter'
  }

  return Object.keys(errors.value).length === 0
}

const isValidEmail = (email) => {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
}

const handleSubmit = async () => {
  if (!validateForm()) return
  
  loading.value = true
  
  try {
    const response = await authApi.register(
      form.value.nama,
      form.value.username,  
      form.value.email,
      form.value.password
    )
    
    const data = response.data
    
    if (data.success) {
      alert(data.message || 'Registrasi berhasil! Silakan login.')
      router.push('/')  
    } else {
      errors.value.submit = data.message || 'Registrasi gagal'
    }
    
  } catch (error) {
    errors.value.submit = error.response?.data?.message || error.message || 'Registrasi gagal'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="register-container">
    <div class="register-card">
      <h2 class="title">REGISTER</h2>
      
      <form @submit.prevent="handleSubmit" class="register-form">
        <div class="form-row">
          <label class="inline-label">Nama:</label>
          <input 
            type="text" 
            v-model="form.nama" 
            required
            :disabled="loading"
            :class="{ 'input-error': errors.nama }"
            class="inline-input"
          >
        </div>
        <span v-if="errors.nama" class="error-text">{{ errors.nama }}</span>

        <div class="form-row">
          <label class="inline-label">Email:</label>
          <input 
            type="email" 
            v-model="form.email" 
            required
            :disabled="loading"
            :class="{ 'input-error': errors.email }"
            class="inline-input"
          >
        </div>
        <span v-if="errors.email" class="error-text">{{ errors.email }}</span>

        <div class="form-row">
          <label class="inline-label">Username:</label>
          <input 
            type="text" 
            v-model="form.username" 
            required
            :disabled="loading"
            :class="{ 'input-error': errors.username }"
            class="inline-input"
          >
        </div>
        <span v-if="errors.username" class="error-text">{{ errors.username }}</span>

        <div class="form-row">
          <label class="inline-label">Password:</label>
          <input 
            type="password" 
            v-model="form.password" 
            required
            :disabled="loading"
            :class="{ 'input-error': errors.password }"
            class="inline-input"
          >
        </div>
        <span v-if="errors.password" class="error-text">{{ errors.password }}</span>

        <div v-if="errors.submit" class="submit-error">
          {{ errors.submit }}
        </div>

        <button 
          type="submit" 
          :disabled="loading"
          class="register-btn"
        >
          {{ loading ? 'Loading...' : 'Register' }}
        </button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.register-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f5f5;
  padding: 20px;
}

.register-card {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 400px;
}

.title {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
  font-size: 24px;
  font-weight: bold;
}

.register-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
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
  min-width: 80px;
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

.input-error {
  border-color: #f44336 !important;
}

.error-text {
  color: #f44336;
  font-size: 14px;
  margin-top: -10px;
  margin-bottom: 5px;
}

.submit-error {
  color: #f44336;
  text-align: center;
  font-size: 14px;
  padding: 10px;
  background: #ffebee;
  border-radius: 4px;
  margin-top: 10px;
}

.register-btn {
  background: #4CAF50;
  color: white;
  border: none;
  padding: 12px;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.3s;
  margin-top: 10px;
}

.register-btn:hover:not(:disabled) {
  background: #45a049;
}

.register-btn:disabled {
  background: #cccccc;
  cursor: not-allowed;
}

@media (max-width: 480px) {
  .register-card {
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
}
</style>