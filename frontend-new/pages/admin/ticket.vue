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
          <v-toolbar-title>Ticket List</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
                New Ticket
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-card-text>Ticket Class</v-card-text>
                  <v-select
                    outlined
                    :items="ticket_class"
                    v-model="defaultItem.ticket_class"
                  ></v-select>
                  <v-card-text>Seat Number</v-card-text>
                  <v-text-field
                    outlined
                    v-model="defaultItem.seat_no"
                  ></v-text-field>
                  <v-row>
                    <v-col cols="12" md="6">
                      <v-card-text>Price</v-card-text>
                      <v-text-field
                        outlined
                        v-model="defaultItem.price"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" md="6">
                      <v-card-text>Booked</v-card-text>
                      <v-select
                        outlined
                        :items="choice"
                        v-model="defaultItem.booked"
                      ></v-select>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="12" md="6">
                      <v-card-text>Purchased</v-card-text>
                      <v-select
                        outlined
                        :items="choice"
                        v-model="defaultItem.purchased"
                      ></v-select>
                    </v-col>
                    <v-col cols="12" md="6">
                      <v-card-text>Refundable</v-card-text>
                      <v-select
                        outlined
                        :items="choice"
                        v-model="defaultItem.refundable"
                      ></v-select>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-card-text>Flight</v-card-text>
                      <v-select
                        outlined
                        :items="flights"
                        v-model="defaultItem.flight"
                      ></v-select>
                      <!-- <select
                        class="form-control"
                        v-model="defaultItem.flight"
                        required
                        @change="changeLocation"
                      >
                        <option selected>Choose Province</option>
                        <option
                          v-for="option in flights"
                          v-bind:value="option.id"
                          v-bind:key="option.id"
                        >
                          {{ option.name }}
                        </option>
                      </select> -->
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
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5"
                >Are you sure you want to delete this ticket?</v-card-title
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
      action: "/tickets/ticket/",
      dialog: false,
      dialogDelete: false,
      dialogCancel: false,
      headers: [
        { text: "Ticket Class", value: "ticket_class" },
        { text: "Seat No", value: "seat_no" },
        { text: "Price Currency", value: "price_currency" },
        { text: "Price", value: "price" },
        { text: "Booked", value: "booked" },
        { text: "Refundable", value: "refundable" },
        { text: "Flight", value: "flight" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      ticket_class: ["A", "B", "C"],
      choice: [true, false],
      desserts: [],
      editedIndex: -1,
      flights: [],
      defaultItem: {
        ticket_class: "",
        seat_no: "",
        price: "",
        booked: "",
        refundable: "",
        flight: "",
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
    await this.getFlights();
    await this.getTickets();
  },

  methods: {
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
      this.deleteTicket();
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
      if (this.editedIndex == -1) {
        this.postTicket();
      } else {
        this.putTicket();
      }
      this.close();
    },
    async getTickets() {
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

    async postTicket() {
      const url = this.action;
      await this.$axios
        .post(url, this.defaultItem)
        .then((response) => {
          this.getTickets();
          // const { ticket_class, seat_no, price, booked, refundable, flight } =
          //   response.data;
          // this.desserts = {
          //   ticket_class,
          //   seat_no,
          //   price,
          //   booked,
          //   refundable,
          //   flight,
          // };
        })
        .catch(function (error) {
          Swal.fire("error", error.response.data, "error");
        });
    },
    async putTicket() {
      const url = this.action + this.defaultItem.id + "/";
      await this.$axios
        .patch(url, this.defaultItem)
        .then((response) => {
          this.getTickets();
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    async deleteTicket() {
      const url = this.action + this.defaultItem.id + "/";
      await this.$axios
        .delete(url)
        .then((response) => {
          this.getTickets();
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
          this.desserts = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    async getFlights() {
      // var self = this;
      const url = "/tickets/flight/";
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
          console.log(response.data.map((item) => item.id));
          this.flights = response.data.map((item) => item.id);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
