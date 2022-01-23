<template>
    <div style="padding-top:1rem">
        <v-row 
            align="center"
            justify="center"
        >
            <v-col
                align="center"
                justify="center"
                cols="11"
                sm="9"
                md="6"
                lg="4"
            >
                <v-card>
                    <v-alert
                        style="text-align:left"
                        type="info"
                    >
                        Data utworzenia: {{ data2.created_at}}
                    </v-alert>
                </v-card>
                <v-card style="cursor: pointer; text-align:left" id="done" v-if="data2.isDone">
                    <v-alert
                        type="success"
                    >
                        Status Zadania: Rozwiązane
                    </v-alert>
                </v-card>
                <v-card style="cursor: pointer; text-align:left" id="notDone" v-if="!data2.isDone">
                    <v-alert
                        type="warning"
                    >
                        Status Zadania: Nie Rozwiązane
                    </v-alert>
                </v-card>
                
                <v-date-picker v-model="data2.date" color="red"/>
                <v-form
                    style="padding-top:2rem"
                    ref="form"
                    lazy-validation
                    v-model="valid"
                >
                    <v-text-field
                        v-model="data2.title"
                        label="Tytuł"
                        outlined
                    ></v-text-field>

                    <v-text-field
                        v-model="data2.description"
                        label="Opis"
                        required
                        outlined
                    ></v-text-field>

                    <v-text-field
                        v-model="data2.hour"
                        :rules = hourRules
                        label="Godzina hh:mm"
                        :validate-on-blur = true
                        outlined
                    ></v-text-field>
                    <v-text-field
                        v-model="data2.date"
                        label="Data"
                        :readonly="true"
                        outlined
                    ></v-text-field>
                    <v-row
                        
                    >
                        <v-col
                            cols="6"
                            sm="4"
                        >
                            <v-btn
                                @click="submit"
                                :disabled="!valid"
                                color="success"
                                style="width:100%!important"
                            >
                                Zapisz
                            </v-btn>
                        </v-col>
                        
                    </v-row>
                </v-form>
            </v-col>
        </v-row>
    </div>
    
</template>




<script>
    import { AUTH_API } from '../../authorization/AuthAPI'
    export default {
        data() {
            return {
                id: null,
                data: null,
                date: '',
                hour: '',
                description: '',
                title: '',
                dateTime:'',
                valid: true,
                hourRules: [
                    v => {return(v.length == 0 || /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/.test(v)) || 'Godzina musi mieć format: hh:mm'},
                ],
            };

        },
        created(){
            this.id = this.$route.query.id
            AUTH_API.get('/api/v1/gettodo/'+ '?id=' + this.id)
              .then(res=>{
                  let date = res.data.created_at.replace("T", " ");
                  date = date.split('.')[0]
                  let _data = res.data
                  _data.created_at = date
                  _data.hour = _data.deadline.split(' ')[1]
                  _data.date = _data.deadline.split(' ')[0]
                  this.data = _data
                  console.log(this.data)
              })
              .catch(err=>{
                  window.location.href = '/';
                  console.log(error)
            })
        },

        mounted(){
            if(document.querySelector('#done')){
                document.querySelector('#done').addEventListener('click', ()=>{
                    this.data.isDone = !this.data.isDone
                })
            }
            else{
                document.querySelector('#notDone').addEventListener('click', ()=>{
                    this.data.isDone = !this.data.isDone
                })
            }
        },
        computed:{
            data2(){
                if(this.data!==null){
                    return this.data
                }
                let _data = {
                    created_at: '',
                    created_at: '',
                    deadline: '',
                    description: '',
                    id: '',
                    isDone: false, 
                    title: '',
                    user_id: '',
                    date: '',
                    hour: '',
                }
                return _data
            }
        },
        methods: {
            toTimestamp(date){
                let datum = Date.parse(date);
                return datum/1000;
            },
            test(){
                console.log('a')
            },
            submit(){
                AUTH_API.patch('/api/v1/addtodo/?id=' + this.id, {
                    deadline: this.data2.date + ' ' + this.data2.hour,
                    description: this.data2.description,
                    isDone: this.data2.isDone,
                    title: this.data2.title,
                })
                .then(res=>{
                    console.log(res.data)
                    alert('Dane zaktualizowane')
                    window.location.reload(true);
                })
                .catch(err=>{
                    console.log(err.data)
                })
            },
        },
    }
</script>