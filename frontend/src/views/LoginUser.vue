<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/store/auth'

const authStore = useAuthStore()
const router = useRouter()
const username = ref('')    
const password = ref('')  
const loading = ref(false)  

const handleLogin = async () => {
    loading.value = true
    const result = await authStore.login(username.value, password.value)
    if (result && result.success) {
        router.push('/dashboard')
    } else {
        alert(result?.message || 'Login failed')
    }
    loading.value = false
}

const goToRegister = () => {
    router.push('/register')
}
</script>

<template>
    <div class="login-container">
        <div class="login-card">
            <h2 class="title">LOGIN</h2>
            
            <form @submit.prevent="handleLogin" class="login-form">
                <div class="form-row">
                    <label class="inline-label">Username:</label>
                    <input 
                        type="text" 
                        v-model="username" 
                        required
                        :disabled="loading"
                        class="inline-input"
                    >
                </div>

                <div class="form-row">
                    <label class="inline-label">Password:</label>
                    <input 
                        type="password" 
                        v-model="password" 
                        required
                        :disabled="loading"
                        class="inline-input"
                    >
                </div>

                <div class="button-group">
                    <button 
                        type="submit" 
                        :disabled="loading || !username || !password"
                        class="login-btn"
                    >
                        {{ loading ? 'Loading...' : 'Login' }}
                    </button>

                    <button 
                        type="button" 
                        @click="goToRegister"
                        class="register-btn"
                    >
                        Register
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<style scoped>
.login-container {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #f5f5f5;
    padding: 20px;
}

.login-card {
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

.login-form {
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

.button-group {
    display: flex;
    gap: 15px;
    margin-top: 20px;
}

.button-group button {
    flex: 1;
}

.login-btn {
    background: #4CAF50;
    color: white;
    border: none;
    padding: 12px;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
    transition: background 0.3s;
}

.login-btn:hover:not(:disabled) {
    background: #45a049;
}

.login-btn:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

.register-btn {
    background: transparent;
    color: #4CAF50;
    border: 1px solid #4CAF50;
    padding: 12px;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
    transition: all 0.3s;
}

.register-btn:hover {
    background: #4CAF50;
    color: white;
}

@media (max-width: 480px) {
    .login-card {
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