<template>
  <div>
    <v-container>
      <v-row>
        <v-col md="6">
          <v-card tile elevation="0">
            <h2
              class="text-center pt-3"
              style="font-family: playfair display, serif; color: #0285b9"
            >
              Welcome
            </h2>
            <v-card-text
              class="text-center"
              style="
                font-family: playfair display, serif;
                color: #0285b9;
                font-size: 18px;
              "
            >
              Please Sign Up to Continue</v-card-text
            >
            <v-container>
              <v-row>
                <v-text-field
                  outlined
                  class="mx-6 my-2"
                  v-model="info.name"
                  label="Full Name"
                ></v-text-field>
                <v-text-field
                  outlined
                  class="mx-6 my-2"
                  v-model="info.address"
                  label="Address"
                ></v-text-field>
              </v-row>
              <v-text-field
                outlined
                class="mx-3"
                v-model="info.email"
                label="E-mail Address"
              ></v-text-field>
              <v-text-field
                outlined
                class="mx-3"
                v-model="info.phone"
                label="Phone Number"
              ></v-text-field>
              <v-text-field
                outlined
                class="mx-3"
                label="Password"
                v-model="info.password"
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[rules.required, rules.min]"
                :type="show1 ? 'text' : 'password'"
                name="input-10-1"
                @click:append="show1 = !show1"
              ></v-text-field>
              <v-text-field
                v-model="info.password"
                :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[rules.required, rules.min]"
                :type="show2 ? 'text' : 'password'"
                name="input-10-1"
                outlined
                class="mx-3"
                label="Confirm Password"
              ></v-text-field>
              <div class="text-center">
                <v-btn
                  color="#0285b9"
                  @click="register"
                  class="white--text mb-5"
                  width="15em"
                >
                  Sign Up</v-btn
                >
              </div>
            </v-container>
          </v-card>
        </v-col>
        <v-col md="6">
          <v-container>
            <v-img src="sign.jpg"></v-img>
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import swal from "sweetalert2";
export default {
  data() {
    return {
      action: "/accounts/register-customer/",
      info: {
        name: "",
        email: "",
        address: "",
        phone: "",
        password: "",
      },
      show1: false,
      show2: false,
      rules: {
        required: (value) => !!value || "required.",
        // min: (v) => v.length >= 8 || "min 8 characters",
        // emailmatch: () => `the email and password you entered don't match`,
      },
    };
  },
  methods: {
    async register() {
      try {
        const res = await this.$axios.post(this.action, {
          ...this.info,
        });
        swal.fire("success", "user registration successful", "success");
        this.$router.push({
          path: "/home",
        });
      } catch (err) {
        if (err.response.data.email) {
          swal.fire("error", err.response.data.email[0], "error");
        } else {
          swal.fire("error", "please try again later", "error");
        }
      }
    },
  },
};
</script>

<style></style>
