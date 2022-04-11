<template>
  <div class="pa-5">
    <v-data-table
      :headers="headers"
      :items="desserts"
      sort-by="date"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Flight List</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
                New Flight
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-card-text>Airline</v-card-text>
                  <v-select outlined :items="links"></v-select>
                  <v-card-text>Flight Number</v-card-text>
                  <v-text-field
                    outlined
                    v-model="defaultItem.flight_number"
                  ></v-text-field>
                  <v-row>
                    <v-col cols="12" md="6">
                      <v-card-text>Departure Location</v-card-text>
                      <v-select
                        outlined
                        :items="departure"
                        v-model="defaultItem.departure_location"
                      ></v-select>
                    </v-col>
                    <v-col cols="12" md="6">
                      <v-card-text>Arrival Location</v-card-text>
                      <v-select
                        outlined
                        :items="arrival"
                        v-model="defaultItem.arrival_location"
                      ></v-select>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="12" md="6">
                      <v-card-text>Flight Time</v-card-text>
                      <v-text-field
                        outlined
                        v-model="defaultItem.flight_time"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" md="6">
                      <v-card-text>Departure Date</v-card-text>
                      <v-text-field
                        outlined
                        v-model="defaultItem.departure_date"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="12" md="6">
                      <v-card-text>Baggage Limit</v-card-text>
                      <v-text-field
                        outlined
                        v-model="defaultItem.baggage_limit"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" md="6">
                      <v-card-text>Duration</v-card-text>
                      <v-text-field
                        outlined
                        v-model="defaultItem.duration"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">
                  Cancel
                </v-btn>
                <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogCancel" max-width="500px">
            <v-card>
              <v-card-title class="text-h5"
                >Are you sure you want to cancel this flight?</v-card-title
              >
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeCancel"
                  >Cancel</v-btn
                >
                <v-btn color="blue darken-1" text @click="cancelItemConfirm"
                  >OK</v-btn
                >
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5"
                >Are you sure you want to delete this flight?</v-card-title
              >
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete"
                  >Cancel</v-btn
                >
                <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                  >OK</v-btn
                >
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
        <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
        <v-icon small @click="cancelItem(item)"> mdi-cancel </v-icon>
      </template>
      <!-- <template v-slot:no-data>
        <v-btn color="primary" @click="initialize"> Reset </v-btn>
      </template> -->
    </v-data-table>
  </div>
</template>

<script>
export default {
  middleware: "auth-admin",
  data() {
    return {
      action: "/tickets/flight/",
      dialog: false,
      dialogDelete: false,
      dialogCancel: false,
      headers: [
        {
          text: "Flight Number",
          align: "start",
          sortable: false,
          value: "flight_number",
        },
        { text: "Departure Date", value: "departure_date" },
        { text: "Flight Time", value: "flight_time" },
        { text: "Baggage Limit", value: "baggage_limit" },
        { text: "Arriaval Location", value: "arrival_location" },
        { text: "Departure Location", value: "departure_location" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      links: ["Buddha Airlines", "Yeti Airlines", "Tara Airlines"],
      departure: ["Kathmandu", "Pokhara", "Biratnagar"],
      arrival: ["Butwal", "Kathmandu", "Bhojpur"],
      desserts: [],
      editedIndex: -1,
      defaultItem: {
        flight_number: "",
        baggage_limit: "",
        flight_time: "",
        duration: "",
        departure_date: "",
        arrival_location: "",
        departure_location: "",
      },
    };
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Flight" : "Edit Flight";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  async created() {
    this.initialize();
    await this.getFlights();
    console.log(this.desserts);
  },

  methods: {
    initialize() {
      // this.desserts = [
      //   {
      //     date: "March 6, 2022",
      //     information: 518,
      //     seats: 26.0,
      //     booked: 65,
      //     price: 7,
      //   },
      // ];
    },

    editItem(item) {
      console.log(item.arrival_location);
      this.editedIndex = this.desserts.indexOf(item);
      this.defaultItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.defaultItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    cancelItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.defaultItem = Object.assign({}, item);
      this.dialogCancel = true;
    },

    deleteItemConfirm() {
      // this.desserts.splice(this.editedIndex, 1);
      this.deleteFlight();
      this.closeDelete();
    },

    cancelItemConfirm() {
      this.cancelFlight();
      this.closeCancel();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.defaultItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.defaultItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeCancel() {
      this.dialogCancel = false;
      this.$nextTick(() => {
        this.defaultItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },
    save() {
      // if (this.editedIndex > -1) {
      //   Object.assign(this.desserts[this.editedIndex], this.editedItem);
      // } else {
      //   this.desserts.push(this.editedItem);
      // }
      if (this.editedIndex == -1) {
        this.postFlight();
      } else {
        this.putFlight();
      }
      this.close();
    },
    async getFlights() {
      // var self = this;
      const url = this.action;
      await this.$axios
        .get(url, {
          dataType: "json",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
          mode: "no-cors",
          credentials: "include",
        })
        .then((response) => {
          this.desserts = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    async postFlight() {
      const url = this.action;
      await this.$axios
        .post(url, this.defaultItem)
        .then((response) => {
          // this.desserts = response.data;
          this.getFlights();
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    async putFlight() {
      const url = this.action + this.defaultItem.id + "/";
      await this.$axios
        .patch(url, this.defaultItem)
        .then((response) => {
          // this.desserts = response.data;
          this.getFlights();
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    async deleteFlight() {
      const url = this.action + this.defaultItem.id + "/";
      await this.$axios
        .delete(url)
        .then((response) => {
          // this.desserts = response.data;
          this.getFlights();
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    async cancelFlight() {
      const url = this.action + this.defaultItem.id + "/";
      await this.$axios
        .patch(url, { cancelled: true })
        .then((response) => {
          // this.desserts = response.data;
          this.getFlights();
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
