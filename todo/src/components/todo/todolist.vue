<template>
  <v-container class="px-0 py-0" style="max-height: 100%">
    <v-row align="center"
            justify="center">
      <v-col 
        style="padding-top:2rem"
        cols="12"
        sm="9"
        md="8"
        lg="7"
      >
        <v-card style="cursor: pointer; text-align:left" id="doneList" v-if="isDone">
          <v-alert
              type="success"
          >
              Status Zadania: Rozwiązane
          </v-alert>
        </v-card>
        <v-card style="cursor: pointer; text-align:left" id="notDoneList" v-if="!isDone">
          <v-alert
              type="warning"
          >
              Status Zadania: Nie Rozwiązane
          </v-alert>
       </v-card>
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
              <div><b>Tytuł: </b>{{ _data.title }}</div>
              <div><b>Deadline: </b>{{ _data.deadline }}</div>
              <v-btn
                style="max-width:50px"
                small
                class="item-action ml-2 mr-5"
                color="error"
                @click.native.stop="deleteTask(_data.id)"
                ><v-icon>{{'mdi-trash-can-outline'}}</v-icon></v-btn
              >
              <v-btn
                small
                style="max-width:50px"
                class="item-action ml-2 mr-5"
                color="success"
                @click.native.stop="doneTask(_data.id)"
                ><v-icon>{{'mdi-note-check'}}</v-icon></v-btn
              >
              <v-btn
                small
                style="max-width:50px"
                class="item-action ml-2 mr-5"
                color="warning"
                @click.native.stop="edit(_data.id)"
                ><v-icon>{{'mdi-clipboard-edit'}}</v-icon></v-btn
              >
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row>
                <v-col :cols="12">
                  <v-list dense class="pa-0">
                    <v-list-item>
                      <v-list-item-content class="py-1">
                        <v-list-item-title><b>Opis</b></v-list-item-title>
                        <v-list-item-subtitle>{{
                          _data.description
                        }}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content class="py-1">
                        <v-list-item-title><b>Data utworzenia</b></v-list-item-title>
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
            data: [],
            isDone: false,
        }),
        created(){
            this.search('False')
            // AUTH_API.get('/api/v1/addtodo/')
            // .then(res=>{
            //     res.data.forEach(el=>{
            //       let date = el.created_at.replace("T", " ");
            //       date = date.split('.')[0]
            //       let _data = el
            //       _data.created_at = date
            //       this.data.push(_data)
            //     })
            // })
            // .catch(err=>{
            //     console.log(err)
            // })
        },
         mounted(){
            if(document.querySelector('#doneList')){
                document.querySelector('#doneList').addEventListener('click', ()=>{
                    this.isDone = !this.isDone
                    let replaced = ''
                    if(this.isDone){
                      replaced = 'T' + new String(this.isDone).substring(1);
                    }
                    else{
                      replaced = 'F' + new String(this.isDone).substring(1);
                    }
                    this.search(replaced)
                })
            }
            else{
                document.querySelector('#notDoneList').addEventListener('click', ()=>{
                    this.isDone = !this.isDone
                    let replaced = ''
                    if(this.isDone){
                      replaced = 'T' + new String(this.isDone).substring(1);
                    }
                    else{
                      replaced = 'F' + new String(this.isDone).substring(1);
                    }
                    this.search(replaced)
                })
            }
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
            search(isDone){
              console.log('aaaaa')
              this.data = []
              AUTH_API.get('/api/v1/search/?isDone=' + isDone)
              .then(res=>{
                  res.data.forEach(el=>{
                    let date = el.created_at.replace("T", " ");
                    date = date.split('.')[0]
                    let _data = el
                    _data.created_at = date
                    this.data.push(_data)
                  })
              })
              .catch(err=>{
                  console.log(err)
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