<template>
  <v-container>
    <div class="mb-16">
      <v-row justify="center">
        <h3>Thank You, your booking is complete</h3>
      </v-row>

      <v-row>
        <v-col md="6" v-for="link in links" :key="link">
          <v-card outlined>
            <v-container>
              <v-card-title>BOOKING DETAILS</v-card-title>
              <v-divider></v-divider>
              <v-card-title>FLIGHT NUMBER</v-card-title>
              <v-card-text>{{ link.flight_details.flight_number }}</v-card-text>
              <v-card-title>DEPARTURE DATE</v-card-title>
              <v-card-text>{{
                link.flight_details.departure_date
              }}</v-card-text>
              <v-card-title>ARRIVAL</v-card-title>
              <v-card-text>{{
                link.flight_details.arrival_location
              }}</v-card-text>
              <v-card-title>DEPARTURE</v-card-title>
              <v-card-text>{{
                link.flight_details.departure_location
              }}</v-card-text>
              <v-card-title>SEATS</v-card-title>
              <v-card-text
                >{{ link.seat_no }}{{ link.ticket_class }}</v-card-text
              >
            </v-container>
          </v-card>
        </v-col>

        <v-col md="6" v-for="thing in things" :key="thing">
          <v-card outlined>
            <v-container>
              <v-card-title>PERSONAL DETAILS</v-card-title>
              <v-divider></v-divider>
              <v-card-title>FULL NAME</v-card-title>
              <v-card-text>{{ thing.name }}</v-card-text>
              <v-card-title>ADDRESS</v-card-title>
              <v-card-text>{{ thing.address }}</v-card-text>
              <v-card-title>GENDER</v-card-title>
              <v-card-text>{{ thing.gender }}</v-card-text>
              <v-card-title>E-mail</v-card-title>
              <v-card-text>{{ thing.email }}</v-card-text>
              <v-card-title>PHONE</v-card-title>
              <v-card-text>{{ thing.phone }}</v-card-text>
            </v-container>
          </v-card>
        </v-col>
      </v-row>
      <div class="text-center mt-6">
        <v-btn @click="cancelBooking">Cancel Booking</v-btn>
      </div>
    </div>
  </v-container>
</template>

<script>
import Swal from "sweetalert2";
export default {
  mounted() {
    this.initialize();
  },
  data: () => ({
    action: "/bookings/cancel-booking/",
    links: [],
    things: [],
    id: "",
  }),
  methods: {
    initialize() {
      let data = localStorage.getItem("booking-details");
      if (data) {
        data = JSON.parse(data);
        this.links = [data.ticket_details].flat();
        this.things = [data.booking_user_details].flat();
        this.id = data.id;
      } else {
        this.$router.push("/booking");
      }
    },
    async cancelBooking() {
      const url = this.action + this.id + "/";
      await this.$axios
        .post(url)
        .then((response) => {
          Swal.fire("Success", "Ticket Cancel Successful", "success");
          localStorage.removeItem("booking-details");
          this.$router.push("/");
        })
        .catch(function (error) {
          Swal.fire("error", error.response.data, "error");
        });
    },
  },
};
</script>

<style></style>
