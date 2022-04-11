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
          <v-toolbar-title>Purchased Flight List</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col>
                      <v-text-field
                        v-model="defaultItem.id"
                        label="Number"
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="defaultItem.email"
                        label="Email"
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="defaultItem.name"
                        label="Name"
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="defaultItem.phone"
                        label="Phone"
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="defaultItem.flight_time"
                        label="Flight Time"
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="defaultItem.departure_date"
                        label="Departure Date"
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="defaultItem.price"
                        label="Price"
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
                <v-btn color="blue darken-1" text @click="save">Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5"
                >Are you sure you want to cancel the booking?</v-card-title
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
    </v-data-table>
  </div>
</template>

<script>
export default {
  data: () => ({
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: "S.N.",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "Passenger Name", value: "passenger_name" },
      { text: "Contact Name", value: "contact_name" },
      { text: "Contact Email", value: "contact_email" },
      { text: "Contact Phone", value: "contact_phone" },
      {
        text: "Flight Time",
        value: "ticket_details.flight_details.flight_time",
      },
      {
        text: "Departure Date",
        value: "ticket_details.flight_details.departure_date",
      },
      { text: "Price", value: "ticket_details.price" },
      { text: "Booking Status", value: "ticket_details.booked" },
    ],
    desserts: [],
    editedIndex: -1,
    defaultItem: {
      id: "",
      passenger_name: "",
      contact_name: "",
      contact_email: "",
      contact_phone: "",
      flight_time: "",
      departure_date: "",
      price: "",
      booked: "",
    },
    action: "/bookings/all-purchases/",
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
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

  created() {
    this.initialize();
  },

  methods: {
    initialize() {
      this.getBooked();
    },

    editItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.defaultItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.defaultItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      // this.desserts.splice(this.editedIndex, 1);
      this.deleteBooked();
      this.closeDelete();
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

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.desserts[this.editedIndex], this.defaultItem);
      } else {
        this.desserts.push(this.defaultItem);
      }
      this.close();
    },

    async getBooked() {
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
          console.log(JSON.stringify(response.data));
          this.desserts = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
