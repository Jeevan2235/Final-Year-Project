<template>
  <div>
    <v-img src="welcome.jpg">
      <v-container>
        <v-card class="my-16 mx-auto">
          <v-row>
            <v-col md="6">
              <v-row justify="center" class="my-2">
                <v-btn
                  :color="login == false ? '#a0e7f1' : '#0596c8'"
                  elevation="0"
                  height="5em"
                  width="20em"
                  class="mx-1 white--text"
                  @click="switchAccountVue('login')"
                  >Login</v-btn
                >
              </v-row>
            </v-col>
            <v-col md="6">
              <v-row justify="center" class="my-2">
                <v-btn
                  :color="login ? '#a0e7f1' : '#0596c8'"
                  elevation="0"
                  height="5em"
                  width="20em"
                  class="mx-1 white--text"
                  @click="switchAccountVue('signup')"
                  >signup</v-btn
                >
              </v-row>
            </v-col>
          </v-row>

          <login v-if="login" />
          <signup v-else />
        </v-card>
      </v-container>
    </v-img>
  </div>
</template>

<script>
import Login from "../components/login.vue";
import Signup from "../components/signup.vue";
export default {
  middleware: "loggedIn",
  auth: "guest",
  components: { Login, Signup },
  data() {
    return {
      login: false,
      items: [{ icon: "mdi-view-dashboard" }],
    };
  },

  methods: {
    switchAccountVue(value) {
      value == "login" ? (this.login = true) : (this.login = false);
    },
  },
};
</script>

<style scoped></style>
