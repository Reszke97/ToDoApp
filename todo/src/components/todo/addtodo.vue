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
                        label="Godzina hh-mm"
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
                                color="success"
                                style="width:100%!important"
                            >
                                Wyślij
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
            };

        },
        computed: {
        },
        methods: {
            submit() {
                this.dateTime = this.date + ':' + this.hour
                 AUTH_API.post('/api/v1/addtodo/', {
                    title: this.title,
                    description: this.description,
                    deadline: this.dateTime
                })
            },
        },
    }
</script>