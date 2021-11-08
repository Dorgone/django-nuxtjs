<!-- pages/register.vue -->
<template>
  <div class="register-page">
    <v-container>
      <v-layout flex align-center justify-center>
        <v-flex xs6 sm6 elevation-6>
          <v-card>
            <v-card-title class="justify-center">
              <h1>Register</h1>
            </v-card-title>
            <v-card-text class="pt-4">
              <div>
                <v-form ref="form">
                  <v-text-field
                    v-model="userData.first_name"
                    label="First name"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="userData.last_name"
                    label="Last name"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="userData.email"
                    label="Email"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="userData.password"
                    label="Password"
                    required
                    :append-icon="
                      userData.showPassword ? 'mdi-eye' : 'mdi-eye-off'
                    "
                    :type="userData.showPassword ? 'text' : 'password'"
                    @click:append="
                      userData.showPassword = !userData.showPassword
                    "
                  ></v-text-field>
                  <v-text-field
                    v-model="userData.password2"
                    label="Confirm password"
                    :append-icon="
                      userData.showPassword2 ? 'mdi-eye' : 'mdi-eye-off'
                    "
                    :type="userData.showPassword2 ? 'text' : 'password'"
                    required
                    @click:append="
                      userData.showPassword2 = !userData.showPassword2
                    "
                  ></v-text-field>


                  <v-checkbox
                    v-model="userData.is_staff"
                    label="Is staff?"
                    required
                    @click:append="userData.is_staff = !userData.is_staff"
                  ></v-checkbox>

                  <v-checkbox
                    v-model="userData.is_superuser"
                    label="Is superuser?"
                    required
                    @click:append="userData.is_superuser = !userData.is_superuser"
                  ></v-checkbox>


                  <v-layout justify-center>
                    <v-btn @click="signUp(userData)">
                      Register
                    </v-btn>
                    
                  </v-layout>
                </v-form>
              </div>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  data: () => ({
    userData: {
      email: '',
      password: '',
      password2: '',
      first_name: '',
      last_name: '',
      is_staff: false,
      is_superuser: false,
      showPassword: false,
      showPassword2: false,
    },
  }),
  methods: {
    async signUp(registrationInfo) {
      const header = {
        headers:{
          'Authorization': "Bearer " + localStorage.getItem('JWTAccess')
        }
      }
      console.log(header);
      await this.$axios
        .$post('authentication/users/', registrationInfo, header)
        .then((response) => {
          console.log('Registration successful')
        })
        .catch((error) => {
          console.log('errors:', error.response)
        })
      this.$auth.loginWith('local', {
        data: registrationInfo,
      })
    },
  },
}
</script>