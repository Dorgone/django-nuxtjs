<template>


  <div v-if="$auth.loggedIn">
    <v-img
      max-width="100"
      src="/hypsoma-logo.png"
      class="mx-auto"
    ></v-img>

    <v-card 
      outlined
      shaped
      tile
      max-width="400"
      class="mx-auto mt-4"
    >
      <v-card-title v-if="$auth.user.is_staff" class="justify-center">
        <h1>Admin panel</h1>
      </v-card-title>
      <v-card-title v-else class="justify-center">
        <h1>User panel</h1>
      </v-card-title>
        <v-card-text class="pt-4">
          <p v-if="$auth.user.is_staff">You have staff level access</p>
          <p v-else>You don't have staff level access</p>
          <p v-if="$auth.user.is_superuser">You have super user level access</p>
          <p v-else>You don't have superuser level access</p>
        </v-card-text>
      </v-card>

      <div class="text-center">
        <v-layout d-inline-flex justify-center>
          <v-btn to="" @click="$auth.logout()">
            Log out
          </v-btn>
        </v-layout>
      </div>

  </div>

  <div v-else class="text-center">
      <v-img
        max-width="200"
        src="/hypsoma-logo.png"
        class="mx-auto mb-4"
      ></v-img>
    <v-layout d-inline-flex justify-center>
      <v-btn to="/login">
        Login
      </v-btn>
    </v-layout>
    <v-layout d-inline-flex justify-center>
      <v-btn to="/register">
        Register
      </v-btn>
    </v-layout>
  </div>

</template>

<script>
import Logo from '~/components/Logo.vue'
import VuetifyLogo from '~/components/VuetifyLogo.vue'

export default {
  components: {
    Logo,
    VuetifyLogo
  },
}
</script>
