import { defineStore } from "pinia"
import { authApi } from '@/services/api'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null,
  }),

  actions: {
    async login(username, password) {
      try {
        const response = await authApi.login(username, password)
        const data = response.data
        
        if (data.success) {
          const userData = data.data.user
          const tokenData = data.data.access_token 
          
          this.user = userData
          this.token = tokenData
          localStorage.setItem('token', tokenData)
          
          return { success: true, user: userData }
        } else {
          return { success: false, message: data.message }
        }
        
      } catch (error) {
        console.error('Login error:', error)
        
        if (error.response?.status === 401) {
          return { 
            success: false, 
            message: error.response.data?.message || 'Invalid credentials' 
          }
        }
        
        return { 
          success: false, 
          message: error.message || 'Login failed' 
        }
      }
    },

    logout() {
      this.user = null
      this.token = null
      localStorage.removeItem('token')
    }, 
  }
})