import Vue from 'vue'
import VueRouter from 'vue-router'

import Register from '../components/authentication/Register.vue'
import Login from '../components/authentication/Login.vue'
import Logout from '../components/authentication/Logout.vue'
import Home from '../components/home/Home.vue'
import AddTodo from '../components/todo/addtodo.vue'
import ToDoList from '../components/todo/todolist.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },

  {
    path: '/logout',
    name: 'Logout',
    component: Logout
  },

  {
    path: '/login',
    name: 'Login',
    component: Login
  },

  {
    path: '/register',
    name: 'Register',
    component: Register,
  },

  {
    path: '/addtask',
    name: 'Addtask',
    component: AddTodo,
  },

  {
    path: '/todolist',
    name: 'ToDoList',
    component: ToDoList,
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router