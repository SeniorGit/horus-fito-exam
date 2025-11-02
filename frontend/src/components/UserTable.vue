<script setup>
import { ref, onMounted, computed } from 'vue'  
import { getData } from '@/services/api'
import { useRouter } from 'vue-router'
import SearchBar from './SearchBar.vue'

const props = defineProps({
  showActions: {
    type: Boolean,
    default: true
  },
  showSearch: {
    type: Boolean,
    default: true
  }
})

const emit = defineEmits(['edit-user', 'delete-user', 'refresh'])
const router = useRouter()


const allUsers = ref([])
const error = ref('')
const success = ref('')
const searchKeyword = ref('')
const deletingId = ref(null) 


const filteredUsers = computed(() => {
  if (!searchKeyword.value) return allUsers.value
  
  const keyword = searchKeyword.value.toLowerCase()
  return allUsers.value.filter(user => 
    user.username?.toLowerCase().includes(keyword) ||
    user.email?.toLowerCase().includes(keyword) ||
    user.nama?.toLowerCase().includes(keyword)
  )
})

// Fetch get data from DB
const fetchUsers = async () => {
  const response = await getData.getallUser()
  const data = response.data
  allUsers.value = data.data.users || data.data
  emit('refresh', allUsers.value)
}

// Delete confirmation
const deleteUser = async (userId) => {
  if (!confirm('Yakin ingin menghapus user ini?')) return
  
  deletingId.value = userId
  error.value = ''
  
  const response = await getData.deleteUser(userId)
  const data = response.data
  
  if (data.success) {
    success.value = data.message || 'User berhasil dihapus!'
    allUsers.value = allUsers.value.filter(user => user.id !== userId)
    
    emit('delete-user', userId)
    
    setTimeout(() => {
      success.value = ''
    }, 3000)
    
  } else {
    error.value = data.message || 'Gagal menghapus user'
  }
  
}

// Search handle
const handleSearch = (keyword) => {
  searchKeyword.value = keyword
}

// Edit handler
const editUser = (user) => {
  if (!user || !user.id) {
    console.error('Invalid user data:', user)
    alert('Error: Data user tidak valid')
    return
  }
  router.push(`/update/${user.id}`)
}


defineExpose({
  refresh: fetchUsers,
  getUsers: () => allUsers.value
})


onMounted(() => {
  fetchUsers()
})
</script>

<template>
  <div class="table-section">
    <div class="table-header">
      <SearchBar 
        v-if="showSearch"
        placeholder="Cari username atau nama..."
        @search="handleSearch"
      />
    </div>

    <div v-if="success" class="success-message">
      {{ success }}
    </div>

    <div v-if="error" class="error-message">
      {{ error }}
    </div>

    <div class="table-container">
      <table class="users-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Nama Lengkap</th>
            <th>Email</th>
            <th v-if="showActions">Aksi</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in filteredUsers" :key="user.id">
            <td>{{ user.id }}</td>
            <td>{{ user.username }}</td>
            <td>{{ user.nama || user.full_name || '-' }}</td>
            <td>{{ user.email }}</td>
            <td v-if="showActions" class="actions">
              <button 
                @click="editUser(user)" 
                class="btn-edit"
                :disabled="deletingId === user.id"
              >
                Edit
              </button>
              <button 
                @click="deleteUser(user.id)" 
                class="btn-delete"
                :disabled="deletingId === user.id"
              >
                {{ deletingId === user.id ? 'Menghapus...' : 'Hapus' }}
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
.table-section {
  margin-top: 20px;
}

.table-header {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.success-message {
  background-color: #e8f5e8;
  color: #2e7d32;
  padding: 12px 16px;
  border-radius: 6px;
  margin-bottom: 15px;
  border-left: 4px solid #2e7d32;
}

.error-message {
  background-color: #ffebee;
  color: #c62828;
  padding: 12px 16px;
  border-radius: 6px;
  margin-bottom: 15px;
  border-left: 4px solid #c62828;
}

.users-table {
  width: 100%;
  border-collapse: collapse;
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.users-table th {
  background-color: #f8f9fa;
  padding: 12px 16px;
  text-align: left;
  font-weight: 600;
  color: #495057;
  border-bottom: 2px solid #e9ecef;
}

.users-table td {
  padding: 12px 16px;
  border-bottom: 1px solid #e9ecef;
}

.actions {
  display: flex;
  gap: 8px;
}

.btn-edit, .btn-delete {
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.8rem;
  transition: all 0.3s;
  min-width: 60px;
}

.btn-edit {
  background-color: #4CAF50;
  color: white;
}

.btn-delete {
  background-color: #f44336;
  color: white;
}

.btn-edit:hover:not(:disabled) {
  background-color: #45a049;
}

.btn-delete:hover:not(:disabled) {
  background-color: #da190b;
}

.btn-edit:disabled, .btn-delete:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.table-container {
  overflow-x: auto;
}
</style>