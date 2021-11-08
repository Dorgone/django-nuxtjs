<!-- pages/login.vue -->
<!-- This contains the login form. You should also add some custom validation yourself. -->
<template>
  <div class="login-page">
    <v-layout flex align-center justify-center>
      <v-flex xs6 sm6 elevation-6>
        <v-card>
          <v-card-title class="justify-center">
            <h1>Login</h1>
          </v-card-title>
          <v-card-text class="pt-4">
            <div>
              <v-form ref="form">
                <v-text-field
                  v-model="userData.email"
                  label="Email"
                  counter
                  required
                ></v-text-field>
                <v-text-field
                  v-model="userData.password"
                  label="Password"
                  :append-icon="
                    userData.showPassword ? 'mdi-eye-off' : 'mdi-eye'
                  "
                  :type="userData.showPassword ? 'text' : 'password'"
                  required
                  @click:append="userData.showPassword = !userData.showPassword"
                ></v-text-field>
                <v-layout justify-center>
                  <v-btn @click="logInUser(userData)">
                    Login
                  </v-btn>
                </v-layout>
              </v-form>
            </div>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
export default {
  data: () => ({
    userData: { email: '', password: '', showPassword: false },
  }),
  methods: {
    async logInUser(userData) {
      console.log(userData);
      try {
        await this.$auth.loginWith('local', {
          data: userData,
        })
        console.log('Logged in');
        console.log(this.$auth)
      } catch (error) {
        console.log('Error while logging in');
        console.log(error);
      }
    },
  },
}
</script>
