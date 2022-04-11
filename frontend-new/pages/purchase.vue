<template>
  <div>
    <v-container class="center">
      <v-row>
        <v-col>
          <v-card tile elevation="0">
            <h2
              class="text-center pt-3"
              style="font-family: playfair display, serif; color: #0285b9"
            >
              welcome
            </h2>
            <v-card-text
              class="text-center"
              style="
                font-family: playfair display, serif;
                color: #0285b9;
                font-size: 18px;
              "
            >
              Enter details to purchase ticket</v-card-text
            >
            <v-container>
              <v-row>
                <v-text-field
                  outlined
                  class="me-2"
                  v-model="ticket.passenger_name"
                  label="Passenger Name"
                ></v-text-field>
                <v-select
                  outlined
                  :items="gender"
                  v-model="ticket.passenger_gender"
                  label="Gender"
                ></v-select>
              </v-row>
              <v-row>
                <v-select
                  outlined
                  class="me-2"
                  :items="document_type"
                  v-model="ticket.passenger_document_type"
                  label="Document Type"
                ></v-select>
                <v-text-field
                  outlined
                  v-model="ticket.passenger_document_number"
                  label="Document Number"
                ></v-text-field>
              </v-row>
              <v-row>
                <v-text-field
                  outlined
                  v-model="ticket.passenger_nationality"
                  label="Nationality"
                ></v-text-field>
              </v-row>

              <v-row>
                <v-text-field
                  outlined
                  class="me-2"
                  v-model="ticket.contact_name"
                  label="Contact Name"
                ></v-text-field>
                <v-select
                  outlined
                  :items="gender"
                  v-model="ticket.contact_gender"
                  label="Contact Gender"
                ></v-select>
              </v-row>
              <v-row>
                <v-text-field
                  outlined
                  class="me-2"
                  v-model="ticket.contact_phone"
                  label="Contact Phone"
                ></v-text-field>
                <v-text-field
                  outlined
                  v-model="ticket.contact_email"
                  label="Contact Email"
                ></v-text-field>
              </v-row>
              <div class="text-center">
                <v-btn
                  color="#0285b9"
                  @click="purchaseFlight"
                  class="white--text mb-5"
                  width="15em"
                >
                  Purchase</v-btn
                >
              </div>
            </v-container>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import swal from "sweetalert2";
export default {
  created() {
    if (this.$route.query.id) {
      this.ticket.ticket = this.$route.query.id;
    } else {
      this.$router.push("/booking");
    }
  },
  data() {
    return {
      action: "/bookings/purchase-ticket/",
      gender: ["MALE", "FEMALE"],
      document_type: ["CITIZENSHIP", "LICENSE"],
      ticket: {
        passenger_name: "",
        passenger_gender: "",
        passenger_document_type: "",
        passenger_document_number: "",
        passenger_nationality: "",
        contact_name: "",
        contact_gender: "",
        contact_phone: "",
        contact_email: "",
        ticket: "",
      },
      rules: {
        required: (value) => !!value || "required.",
      },
    };
  },
  methods: {
    async purchaseFlight() {
      try {
        if (!this.ticket.ticket) {
          swal.fire("error", "No ticket number", "error");
        }
        await this.$axios.post(this.action, this.ticket).then((response) => {
          swal.fire("Success", "Ticket Purchase Successful", "success");
        });
      } catch (err) {
        if (err.response.data.contact_phone) {
          swal.fire("error", err.response.data.contact_phone[0], "error");
        } else {
          swal.fire("error", "please try again later", "error");
        }
      }
    },
  },
};
</script>

<style>
.center {
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  justify-content: center;
  max-width: 800px;
}
</style>
