<template>
  <div>
    <div class="flight">
      <v-container>
        <v-row>
          <v-col cols="12" md="2">
            <v-card-text class="text-subtitle-1">From</v-card-text>
            <!-- <v-select :items="items" outlined label="Houston Texas"></v-select> -->
            <v-select
              outlined
              :items="from"
              v-model="values.departure_location"
            ></v-select>
          </v-col>
          <v-col cols="12" md="2">
            <v-card-text class="text-subtitle-1">To</v-card-text>
            <!-- <v-select :items="items" outlined label="Colorado"></v-select> -->
            <v-select
              outlined
              :items="to"
              v-model="values.arrival_location"
            ></v-select>
          </v-col>
          <v-col cols="12" md="2">
            <v-card-text class="text-subtitle-1">Departure Date</v-card-text>
            <!-- <v-select :items="items" outlined label="22nd February"></v-select> -->
            <client-only
              ><date-picker
                placeholder="YYYY/MM/DD"
                format="yyyy/MM/dd"
                input-class="my-picker-class"
                v-model="values.departure_date"
            /></client-only>
          </v-col>
          <v-col cols="12" md="2">
            <v-card-text class="text-subtitle-1">Adult</v-card-text>
            <!-- <v-select :items="items" outlined label="2"></v-select> -->
            <v-select
              :items="adult"
              :clearable="false"
              v-model="values.adult"
            ></v-select>
            <!-- <v-col cols="12" md="4">
              <v-card-text>Adult</v-card-text>
            </v-col> -->
          </v-col>
          <v-col cols="12" md="2">
            <v-card-text class="text-subtitle-1">Child</v-card-text>
            <!-- <v-select :items="items" outlined label="1"></v-select> -->
            <v-select
              :items="child"
              :clearable="false"
              v-model="values.child"
            ></v-select>
          </v-col>
          <v-col cols="12" md="2">
            <v-btn
              height="4em"
              color="#15aabe"
              class="mt-14 white--text mb-5"
              @click="searchFlight"
            >
              Search Flights
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <div class="ticket">
      <v-container>
        <v-row>
          <v-col md="3">
            <v-card class="mt-16" elevation="0">
              <v-expansion-panels>
                <v-expansion-panel>
                  <v-expansion-panel-header>
                    <h3>Departure</h3>
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <v-row>
                      <v-btn
                        v-for="link in links"
                        :key="link"
                        class="ma-2"
                        tile
                        elevation="0"
                        >{{ link }}</v-btn
                      >
                    </v-row>
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
              <v-divider></v-divider>
              <v-expansion-panels>
                <v-expansion-panel>
                  <v-expansion-panel-header>
                    <h3>Arrival</h3>
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <v-row>
                      <v-btn
                        v-for="thing in things"
                        :key="thing"
                        class="ma-2"
                        tile
                        elevation="0"
                        >{{ thing }}</v-btn
                      >
                    </v-row>
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
              <v-divider></v-divider>
              <v-expansion-panels>
                <v-expansion-panel>
                  <v-expansion-panel-header>
                    <h3>Airlines</h3>
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <v-row>
                      <v-checkbox></v-checkbox>
                      <p class="mt-5">American Airlines</p>
                    </v-row>
                    <v-row>
                      <v-checkbox></v-checkbox>
                      <p class="mt-5">American Airlines</p>
                    </v-row>
                    <v-row>
                      <v-checkbox></v-checkbox>
                      <p class="mt-5">American Airlines</p>
                    </v-row>
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </v-card>
          </v-col>
          <v-col md="9">
            <h2
              class="text-center"
              v-if="
                this.values.departure_location && this.values.arrival_location
              "
            >
              {{ this.values.departure_location }}To
              {{ this.values.arrival_location }}
            </h2>

            <v-card
              class="mt-10"
              v-for="flight in flights"
              :key="flight"
              elevation="0"
            >
              <div class="ma-8">
                <v-row>
                  <v-col class="mt-8" md="2">
                    <v-img src="buddha.png" height="70%" width="60%"></v-img>
                  </v-col>
                  <v-col class="mt-8">
                    <p style="font-size: 1.3125rem; font-weight: 500">
                      {{ flight.flight_details.flight_time }}
                    </p>
                    <p>{{ flight.flight_details.departure_location }}</p>
                  </v-col>
                  <v-col class="mt-8">
                    <p>Duration:{{ flight.flight_details.duration }}</p>
                    
                    <p>Ticket Class:{{ flight.ticket_class }}</p>
                  </v-col>
                  <v-col class="mt-8">
                    <p style="font-size: 1.3125rem; font-weight: 500">
                      {{ flight.flight_details.baggage_limit }} Limit
                    </p>
                    <p>{{ flight.flight_details.arrival_location }}</p>
                  </v-col>
                  <v-col class="mt-8">
                    <div class="text-center">
                      <p>{{ flight.price }}</p>
                      <router-link
                        :to="{
                          path: '/seat',
                          query: {
                            id: flight.id,
                            seat_no: flight.seat_no,
                            ticket_class: flight.ticket_class,
                          },
                        }"
                      >
                        <v-btn outlined color="#00c9a7" v-if="$auth.user"
                          >Book Now</v-btn
                        >
                      </router-link>
                      <router-link
                        :to="{
                          path: '/seat',
                          query: {
                            id: flight.id,
                            seat_no: flight.seat_no,
                            ticket_class: flight.ticket_class,
                          },
                        }"
                      >
                        <v-btn outlined color="#4e4e4e">Purchase</v-btn>
                      </router-link>
                    </div>
                  </v-col>
                </v-row>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import Swal from "sweetalert2";
export default {
  created() {},
  mounted() {
    if (this.$route.query) {
      this.values = this.$route.query;
    }
    this.searchFlight();
  },
  data: () => ({
    links: ["4AM-9AM", "6AM-9AM", "3AM-9AM", "4AM-9AM"],
    things: ["4AM-9AM", "6AM-9AM", "3AM-9AM", "4AM-9AM"],

    adult: ["1", "2", "3", "4"],
    child: ["1", "2", "3", "4"],
    from: ["Pokhara", "Kathmandu", "Biratnagar", "Birgunj", "Bhojpur"],
    to: ["Pokhara", "Kathmandu", "Biratnagar", "Birgunj", "Bhojpur"],
    values: {
      arrival_location: "",
      departure_location: "",
      departure_date: new Date(),
      adult: "",
      child: "",
    },

    flights: [
      // {
      //   img: "buddha.png",
      //   time: "08:30 AM",
      //   place: "Houston Texas",
      //   duration: "45 mins",
      //   time2: "09:15 AM",
      //   place2: "Seattle",
      //   price: "$200",
      //   btn: "Book Now",
      // },
      // {
      //   img: "buddha.png",
      //   icon: "mdi-facebook",
      //   time: "08:30 AM",
      //   place: "Houston Texas",
      //   duration: "45 mins",
      //   time2: "09:15 AM",
      //   place2: "Seattle",
      //   price: "$200",
      //   btn: "Book Now",
      // },
      // {
      //   img: "buddha.png",
      //   icon: "mdi-facebook",
      //   time: "08:30 AM",
      //   place: "Houston Texas",
      //   duration: "45 mins",
      //   time2: "09:15 AM",
      //   place2: "Seattle",
      //   price: "$200",
      //   btn: "Book Now",
      // },
      // {
      //   img: "buddha.png",
      //   icon: "mdi-facebook",
      //   time: "08:30 AM",
      //   place: "Houston Texas",
      //   duration: "45 mins",
      //   time2: "09:15 AM",
      //   place2: "Seattle",
      //   price: "$200",
      //   btn: "Book Now",
      // },
      // {
      //   img: "buddha.png",
      //   icon: "mdi-facebook",
      //   time: "08:30 AM",
      //   place: "Houston Texas",
      //   duration: "45 mins",
      //   time2: "09:15 AM",
      //   place2: "Seattle",
      //   price: "$200",
      //   btn: "Book Now",
      // },
      // {
      //   img: "buddha.png",
      //   icon: "mdi-facebook",
      //   time: "08:30 AM",
      //   place: "Houston Texas",
      //   duration: "45 mins",
      //   time2: "09:15 AM",
      //   place2: "Seattle",
      //   price: "$200",
      //   btn: "Book Now",
      // },
    ],
  }),
  methods: {
    searchFlight() {
      let values = this.values;
      let query;
      if (values.departure_date) {
        query = {
          ...values,
          departure_date: new Date(values.departure_date)
            .toISOString()
            .substring(0, 10),
        };
      }
      query = query ? new URLSearchParams(query).toString() : "";
      this.$axios
        .get("/tickets/filtered-ticket/?" + query)
        .then((response) => {
          this.flights = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
.flight {
  background-color: #69f5ff;
}

.ticket {
  background-color: #e1e7ee;
}
</style>
