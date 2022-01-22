<template>
  <v-container class="px-0 py-0" style="max-height: 100%">
    <v-row align="center"
            justify="center">
      <v-col :cols="6" style="padding-top:2rem">
        <v-expansion-panels>
          <v-expansion-panel
            v-for="(_data, idx) of data"
            :key="idx"
          >
            <v-expansion-panel-header  
              :style="_data.isDone ? { 
                textDecoration: 'line-through!important',
                backgroundColor: 'grey',
              } : { textDecoration: 'none!important' }" 
            >
              <div>{{ _data.title }}</div>
              <div>{{ _data.deadline }}</div>
              <v-btn
                small
                class="item-action ml-2 mr-5"
                color="error"
                @click.native.stop="deleteTask(_data.id)"
                >Usuń</v-btn
              >
              <v-btn
                small
                class="item-action ml-2 mr-5"
                color="success"
                @click.native.stop="doneTask(_data.id)"
                >Gotowe zadanie</v-btn
              >
              <v-btn
                small
                class="item-action ml-2 mr-5"
                color="warning"
                @click.native.stop="edit(_data.id)"
                >Edytuj</v-btn
              >
              <template #actions>
                <v-btn small text :id="`more-item-${idx}`">
                  <v-icon class="mr-3"> mdi-chevron-down </v-icon>
                  Więcej
                </v-btn>
              </template>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row>
                <v-col :cols="12">
                  <v-list dense class="pa-0">
                    <v-list-item>
                      <v-list-item-content class="py-1">
                        <v-list-item-title>Opis</v-list-item-title>
                        <v-list-item-subtitle>{{
                          _data.description
                        }}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content class="py-1">
                        <v-list-item-title>Data utworzenia</v-list-item-title>
                        <v-list-item-subtitle>{{
                            _data.created_at
                        }}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-col>
              </v-row>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>
  </v-container>
</template>




<script>
    import { AUTH_API } from '../../authorization/AuthAPI'

    export default {
        data: () => ({
            data: []
        }),
        created(){
            AUTH_API.get('/api/v1/addtodo/')
            .then(res=>{
                this.data = res.data
            })
            .catch(err=>{
                console.log(err)
            })
        },

        methods:{
            deleteTask(id){
                AUTH_API.delete('/api/v1/addtodo/'+ '?id=' + id)
                .then(res=>{
                    alert('usunięto wybrane zadanie')
                    window.location.reload(true);
                })
                .catch(err=>{
                  alert(err)
                    console.log(err.data)
                })
            },
            doneTask(id){
                AUTH_API.put('/api/v1/addtodo/'+ '?id=' + id)
                .then(res=>{
                    console.log(res.data)
                    window.location.reload(true);
                })
                .catch(err=>{
                    console.log(err.data)
                })
            },
            edit(id){
              this.$router.push({ path: '/edit/?id=' + id })
              
            }
        }
    }
    
</script>