<template>
  <div>
    <form @submit.prevent="login">
      <v-row justify="center">
        <v-col md="6" class="pa-10">
          <v-card-text
            style="
              font-family: Playfair Display, serif;
              font-size: 20px;
              color: #0285b9;
            "
            >Email Address</v-card-text
          >
          <v-text-field
            outlined
            class="mx-3"
            v-model="email"
            :rules="[rules.required]"
          ></v-text-field>
          <v-card-text
            style="
              font-family: Playfair Display, serif;
              font-size: 20px;
              color: #0285b9;
            "
            >Password</v-card-text
          >
          <v-text-field
            outlined
            class="mx-3"
            v-model="password"
            :rules="[rules.required, rules.min]"
            :type="'password'"
            name="input-10-1"
          ></v-text-field>
          <div class="text-center">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
              @click="login"
            >
              Login
            </v-btn>
          </div>
        </v-col>
      </v-row>
    </form>
  </div>
</template>

<script>
import Swal from "sweetalert2";
export default {
  auth: "guest",
  middleware: "loggedIn",
  data() {
    return {
      show1: false,
      email: "",
      password: "",
      rules: {
        required: (value) => !!value || "Required.",
        min: (v) => v.length >= 5 || "Min 5 characters",
        emailMatch: () => `The email and password you entered don't match`,
      },
    };
  },
  methods: {
    login() {
      try {
        this.$auth
          .loginWith("local", {
            data: { email: this.email, password: this.password },
          })
          .then((response) => {
            this.$auth.$storage.setUniversal("user", response.data.user, true);
            this.$nuxt.refresh();
            this.$router.push("/");
          });
      } catch (err) {
        if (err.response.data.detail) {
          Swal.fire("Error", err.response.data.detail, "error");
        }
      }
    },
  },
};
</script>

<style>
.btn {
  width: 17em;
  background-color: black;
  height: 3.5em;
  border: 1px black;
}
</style>
