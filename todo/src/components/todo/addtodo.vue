<template>
    <div style="padding-top:2rem">
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
                lg="3"
            >
                <v-date-picker v-model="date" color="red"/>
                <v-form
                    style="padding-top:2rem"
                    ref="form"
                    lazy-validation
                    v-model="valid"
                >
                    <v-text-field
                        v-model="title"
                        label="Tytuł"
                        outlined
                    ></v-text-field>

                    <v-text-field
                        v-model="description"
                        label="Opis"
                        required
                        outlined
                    ></v-text-field>

                    <v-text-field
                        v-model="hour"
                        :rules = hourRules
                        label="Godzina hh:mm"
                        :validate-on-blur = true
                        outlined
                    ></v-text-field>
                    <v-text-field
                        v-model="date"
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
        computed: {
        },
        methods: {
            toTimestamp(date){
                let datum = Date.parse(date);
                return datum/1000;
            },
            submit() {
                if(this.date === ''){
                    alert('Wybierz datę')
                    return
                }
                // if(this.toTimestamp(this.date + ' ' + this.hour ) < new Date().getTime()){
                //     alert('Wybrano datę ')
                // }
                this.dateTime = this.date + ' ' + this.hour
                 AUTH_API.post('/api/v1/addtodo/', {
                    title: this.title,
                    description: this.description,
                    deadline: this.dateTime
                })
                .then(res=>{
                    alert('Dodano zadanie')
                    this.$refs.form.reset();
                })
            },
        },
    }
</script>