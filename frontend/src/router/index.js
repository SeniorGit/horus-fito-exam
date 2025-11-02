import { createRouter, createWebHistory } from 'vue-router'
import LoginUser from '../views/LoginUser.vue'
import { useAuthStore } from '@/store/auth'
import DashboardUser from '../views/DashboardUser.vue'
import RegisterUser from '../views/RegisterUser.vue'
import UpdateUser from '../views/UpdateUser.vue'

const routes = [
    {
      path: '/',
      name: 'login',
      component: LoginUser,
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterUser
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardUser,
      meta: { requiresAuth: true }
    },
    {
      path: '/update/:id',
      name: 'update',
      component: UpdateUser,
      meta: { requiresAuth: true }
    },
  ]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to,from,next)=>{
  const authstore = useAuthStore()

  if(to.meta.requiresAuth && !authstore.token){
    next('/')
  }else{
    next()
  }
})

export default router
