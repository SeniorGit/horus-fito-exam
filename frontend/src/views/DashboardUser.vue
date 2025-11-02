<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import { useAuthStore } from '@/store/auth'
import UsersTable from '@/components/UserTable.vue'

const router = useRouter()
const usersTableRef = ref()
const authStore = useAuthStore()

const handleLogout = () => {
  authStore.logout()
  router.push('/')
}

const handleEditUser = (user) => {
  router.push(`/update/${user.id}`)
}
</script>

<template>
  <div class="dashboard">
    <div class="dashboard-header">
      <h1>Dashboard Admin</h1>

      <button @click="handleLogout" class="btn-logout">Logout</button>
    </div>

    <UsersTable 
      ref="usersTableRef"
      :show-actions="true"
      @edit-user="handleEditUser"
    />
  </div>
</template>

<style scoped>
.dashboard {
  padding: 20px;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding-bottom: 15px;
}

.btn-logout {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
}

.btn-logout {
  background-color: #ff5722;
  color: white;
}

.btn-logout:hover {
  background-color: #e64a19;
}
</style>