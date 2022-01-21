<template>
  <div>
    <v-app-bar class="indigo white--text">
      <v-toolbar-title>To do app</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items 
        class="d-none d-sm-flex"
      >
        <v-btn
          class="elevation-0 indigo white--text"
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path">
          <v-icon left dark>{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-btn>
      </v-toolbar-items>
      <v-app-bar-nav-icon
        @click="drawer = true" 
        class="d-flex d-sm-none indigo white--text"
      ></v-app-bar-nav-icon>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
        >
          <v-list-item 
            v-for="item in menuItems"
            :key="item.title"
            :to="item.path"
          >
            <v-list-item-title>
              <v-icon left>{{ item.icon }}</v-icon>
              {{ item.title }}
            </v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
    import { mapState } from "vuex"
    export default {
      data(){
        return {
          drawer: false,
          tab: null,
          loaded: false,
        }
      },
      computed: {
        ...mapState({
          isAuthenticated: (state) => state.isAuthenticated,
          role: (state) => state.role
        }),
        menuItems(){
          let menuItems = []
          if(this.isAuthenticated){
            menuItems = [
              { title: 'Home', path: '/', icon: 'mdi-home' },
              { title: 'Lista zadań', path: '/todolist'},
              { title: 'Dodaj zadanie', path: '/addtask'},
              this.auth,
              // { title: 'register', path: '/register', icon: 'mdi-account-plus ' }
            ]
          }
          else{
            menuItems = [
              { title: 'Home', path: '/', icon: 'mdi-home' },
              this.auth,
              { title: 'Rejestracja', path: '/register', icon: 'mdi-account-plus ' }
            ]
          }
          return menuItems
        },
        auth(){
          return this.isAuthenticated?{ title: 'wyloguj', path: '/logout', icon: 'mdi-logout'}:{ title: 'login', path: '/login', icon: 'mdi-login'}
        },
      },

    }
</script>