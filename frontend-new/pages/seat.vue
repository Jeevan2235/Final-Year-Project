<template>
  <div>
    <h2
      class="text-center mt-10"
      style="
        font-size: 30px;
        font-family: Playfair Display, serif;
        color: #0e385d;
      "
    >
      <!-- Please Select Your Seat -->
      Your Selected Seat
    </h2>
    <v-container>
      <v-card class="mb-16">
        <v-row class="mt-16">
          <v-col md="6" class="align-middle">
            <h1 class="ma-4 text-center">
              Selected Seat: {{ seatNo }}{{ ticketClass }}
            </h1>
            <div class="text-center mt-16">
              <!-- <v-btn elevation="1" color="#cbe8ff" @click="bookFlight">
                Continue To Payment
              </v-btn> -->
              <v-btn elevation="1" color="#dbe8ff" @click="bookFlight"
                >Book Now</v-btn
              >

              <router-link
                :to="{
                  path: '/purchase',
                  query: {
                    id: id,
                  },
                }"
              >
                <v-btn elevation="1" color="#abe8ff">Purchase</v-btn>
              </router-link>
            </div>
          </v-col>
          <!-- <v-col v-for="link in links" :key="link" md="6">
            <v-select
              :items="items"
              label="Please Select Your Seat"
              outlined
              class="ma-8"
            ></v-select>
            <p class="ma-4 text-center">{{ link.text }}</p>
            <div class="text-center mt-16">
              <v-btn elevation="1" color="#cbe8ff"> Continue To Payment </v-btn>
            </div>
          </v-col> -->
          <v-col md="6">
            <v-img src="seats.png"></v-img>
          </v-col>
        </v-row>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import Swal from "sweetalert2";
export default {
  mounted() {
    if (!this.$route.query.id) {
      this.$router.push("/booking");
    }
    if (this.$route.query) {
      this.seatNo = this.$route.query.seat_no;
      this.ticketClass = this.$route.query.ticket_class;
      this.id = this.$route.query.id;
    }
  },
  data: () => ({
    id: "",
    seatNo: "",
    ticketClass: "",

    // items: ["1A", "1B", "1C", "1D", "1E", "1F"],

    // links: [
    //   {
    //     text: "Selected Seats : 1D, 1F, 1A",
    //   },
    // ],
  }),
  methods: {
    bookFlight() {
      this.$axios
        .post("/bookings/book-ticket/", {
          booked_by: this.$auth.user.id,
          ticket: this.id,
        })
        .then((response) => {
          // this.flights = response.data;
          console.log(response);
          const data = JSON.stringify(response.data);
          if (data) {
            localStorage.setItem("booking-details", data);
            this.$router.push("/booking-details");
          }
          // Swal.fire("Success", "Ticket Booked Successful", "success");
        })
        .catch((err) => {
          console.log(err.response.data);
          const error =
            err.response.data[0] || "Error!Booking Please try later";
          Swal.fire("Error", error, "error");
          this.$router.push("/booking");
        });
    },
  },
};
</script>

<style>
.align-middle {
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
}
</style>
