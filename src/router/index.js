import { createRouter, createWebHistory } from 'vue-router'
import { useLogin } from '@/utils/useLogin.js'
import { useToken } from '@/utils/useToken.js'
const { logout } = useLogin()

const HomeView = () => import('@/pages/HomeView.vue')
const LoginView = () => import('@/pages/LoginView.vue')
const TeamsView = () => import('@/pages/TeamsView.vue')
const TeamView = () => import('@/pages/TeamView.vue')
const FormView = () => import('@/pages/FormView.vue')
const FormAddView = () => import('@/pages/FormAddView.vue')
const UsersView = () => import('@/pages/UsersView.vue')
const StatusesView = () => import('@/pages/StatusesView.vue')
const TrainingView = () => import('@/pages/TrainingView.vue')
const TrainingIdView = () => import('@/pages/TrainingIdView.vue')
const dropsView = () => import('@/pages/dropsView.vue')
const ToDoListView = () => import('@/pages/ToDoListView.vue')

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/form/:id',
      name: 'form',
      component: FormView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/form-add',
      name: 'form-add',
      component: FormAddView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/teams',
      name: 'teams',
      component: TeamsView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/team/:id',
      name: 'team',
      component: TeamView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/users',
      name: 'users',
      component: UsersView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/statuses',
      name: 'statuses',
      component: StatusesView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/training',
      name: 'trainings',
      component: TrainingView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/training/:id',
      name: 'training',
      component: TrainingIdView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/drops',
      name: 'drops',
      component: dropsView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/todolist',
      name: 'todolist',
      component: ToDoListView,
      meta: {
        requiresAuth: true,
      },
    },
  ],
})
router.beforeEach((to, from, next) => {
  const { isAuth } = useLogin()
  const { tokenExpire } = useToken()
  const dateNow = Date.now()
  const requireAuth = to.meta.requiresAuth

  if (tokenExpire.value && dateNow >= tokenExpire.value) {
    next('/')
    logout().then()
  }

  if (!requireAuth && isAuth.value) {
    next('/home')
  }

  if (requireAuth && !isAuth.value) {
    next('/')
    logout().then()
  } else {
    next()
  }
})
export default router
