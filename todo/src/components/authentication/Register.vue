<template>
    <div>
        <v-row 
            align="center"
            justify="center"
        >
            <v-col
                cols="11"
                sm="9"
                md="6"
                lg="3"
            >
                <v-form
                    ref="form"
                    v-model="valid"
                    lazy-validation
                >
                    <v-text-field
                        v-model="email"
                        :rules="emailRules"
                        label="E-mail"
                        required
                    ></v-text-field>

                    <v-text-field
                        v-model="userName"
                        :rules="userNameRules"
                        :counter="10"
                        label="Nazwa użytkownika"
                        required
                    ></v-text-field>

                    <v-text-field
                        v-model="password1"
                        :rules="password1Rules"
                        label="Hasło"
                        required
                        type="password"
                    ></v-text-field>

                    <v-text-field
                        v-model="password2"
                        :rules="password2Rules"
                        label="Potwierdź hasło"
                        required
                        type="password"
                    ></v-text-field>
                    <v-row
                        
                    >
                        <v-col
                            cols="6"
                            sm="4"
                        >
                            <v-btn
                                :disabled="!valid"
                                color="success"
                                @click="submit"
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
    import axios from 'axios'
    import { mapState} from 'vuex';
    export default {
        data: () => ({
            valid: true,
            email: '',
            emailRules: [
                v => !!v || 'E-mail jest wymagany',
                v => /.+@.+\..+/.test(v) || 'E-mail musi być poprawny przykład:\n example@mail.com',
            ],
            userName:'',
            userNameRules: [
                v => !!v || 'Nazwa użytkownika jest wymagana',
                // v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
            ],
            password1:'',
            password1Rules: [
                v => !!v || 'Hasło jest wymagane',
                // v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
            ],
            password2:'',
            password2Rules: [
                v => !!v || 'Potwierdzenie Hasła jest wymagane',
                // v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
            ],
        }),
        computed: {
        },
        methods: {
            submit () {
                const IS_VALID = this.$refs.form.validate()
                if(IS_VALID){
                    this.sendForm()
                }
            },
            sendForm(){
                axios.post(this.$store.state.baseURL+'/api/v1/user/register/', {
                    'email': this.email,
                    'user_name': this.userName,
                    'password': this.password1,
                })
                .then(response => {
                    alert('Twoje konto zostało utworzone')
                })
                .catch(error => {
                    alert(error)
                })
            },
        },
    }
</script>

<style scoped>
    .w40{
    width: 40%;
    margin-left: auto;
    margin-right: auto;
    }
    .w25{
        width: 25%;
    }
    .top-filter{
        position: sticky;
        top: 0;
        z-index: 2;
    }
    .mt1{
        margin-top: 1rem;
    }
</style>