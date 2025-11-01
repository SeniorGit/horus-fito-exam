import { defineStore } from "pinia";

export const useAuthStore = defineStore('auth',{
    state: () => ({
        user: null,
        token: null
    }),

    actions: {
        login(userData, userToken){
            this.user = userData
            this.token = userToken
            localStorage.setItem('token', userToken)
        },

        logOut(){
            this.user = null
            this.token = null
            localStorage.removeItem('token')
        }
    }
})