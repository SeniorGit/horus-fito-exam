import axios from "axios";

const API_URL = 'http://localhost:5000'

const api = axios.create({
  baseURL: API_URL,  
  timeout: 5000      
})

export const authApi = {
    register(nama, username, email, password){
        return api.post('/api/users/register', {
            nama, 
            username,
            email, 
            password
        })
    },

    async login(username, password) {
        const response = await api.post('/api/users/login', { 
        username, 
        password 
        })
        return response
    },

    getDashboard(){
        return api.get('/api/protected/me')
    }
}

export const getData = {
    getallUser(){
        return api.get('/api/users/getdata')
    },

    update(id, userData){
        return api.put(`/api/users/update/${id}`, userData)
    },

    getUserById(id) {
        return api.get(`/api/users/${id}`)
    },

    deleteUser(id){
        return api.delete(`/api/users/delete/${id}`)
    },

    serachUser(searchKeyword) {
        return api.get('/api/users', { 
        params: { search: searchKeyword }
        })
    },
}
export default api