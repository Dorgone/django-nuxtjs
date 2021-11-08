<template>
  <v-app>



    <v-app-bar fixed app >

    
      <v-btn icon to="/">
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <div class="authentication-buttons">
        <div v-if="$auth.loggedIn">
          <v-btn icon to="" class="logout-btn">
              <v-icon light @click="$auth.logout()">mdi-logout</v-icon>
          </v-btn>
          {{ $auth.user.email }}
        </div>
        <div v-else>
          <v-btn icon to="/login" class="login-btn">
              <v-icon>mdi-login</v-icon>
          </v-btn>
          <v-btn icon to="/register" class="register-btn">
              <v-icon>mdi-account-key-outline</v-icon>
          </v-btn>
        </div>
      </div>
    
    
    

      

          <v-spacer />
          <!--
          <v-toolbar-title class="text-h3" v-if="$auth.loggedIn">
            <div v-if="$auth.user.is_staff">Admin panel</div>
            <div v-else>User panel</div>
          </v-toolbar-title>
          <v-toolbar-title class="text-h3" v-else>
            Authentication app
          </v-toolbar-title>
          -->
          <v-spacer />



        <div class="" v-if="$auth.loggedIn">{{ $auth.user.first_name }} {{ $auth.user.last_name }}</div>
  
    </v-app-bar>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>

    <v-footer
      app
      class="justify-center"
    >
      <span>Authentication app &copy;{{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
}
</script>
