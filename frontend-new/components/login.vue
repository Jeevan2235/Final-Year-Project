<template>
  <div>
    <v-row>
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
          label="E-mail Address"
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
          label="Password"
          v-model="password"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required, rules.min]"
          :type="show1 ? 'text' : 'password'"
          name="input-10-1"
          @click:append="show1 = !show1"
        ></v-text-field>
        <div class="text-center">
          <v-btn
            class="mb-5 white--text"
            width="17em"
            color="#0596c8"
            height="3.5em"
            @click="login"
            >LogIn</v-btn
          >
        </div>
      </v-col>

      <v-col md="6">
        <v-container>
          <v-img src="login.png"></v-img>
        </v-container>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import Swal from "sweetalert2";
export default {
  data() {
    return {
      show1: false,
      show2: true,
      show3: false,
      show4: false,
      email: "",
      password: "",
      rules: {
        required: (value) => !!value || "Required.",
        min: (v) => v.length >= 6 || "Min 6 characters",
        emailMatch: () => `The email and password you entered don't match`,
      },
    };
  },
  methods: {
    async login() {
      this.errors = [];
      try {
        const response = await this.$auth.loginWith("local", {
          data: { email: this.email, password: this.password },
        });
        let newLocation = new URL(location.toString()).origin;
        if (this.$auth.user.role === "STAFF") {
          newLocation += "/admin/booked";
          location.assign(newLocation);
        } else {
          location.assign(newLocation);
        }
      } catch (err) {
        console.log(err);
        if (err.response.data.detail) {
          Swal.fire("Error", err.response.data.detail, "error");
        } else {
          Swal.fire("Error", "Invalid Login", "error");
        }
      }
    },
  },
};
</script>

<style></style>
