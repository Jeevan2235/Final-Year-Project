<template>
  <div>
    <v-row class="pa-5">
      <v-col cols="12" md="4">
        <v-card class="pa-4">
          <v-card-title>Airport's Form</v-card-title>
          <v-divider></v-divider>
          <v-card-text>Airport</v-card-text>
          <v-text-field outlined></v-text-field>
          <v-card-text>Location</v-card-text>
          <v-text-field outlined></v-text-field>
          <v-row justify="center">
            <v-btn class="ma-3 white--text" elevation="0" color="blue"
              >Save</v-btn
            >
            <v-btn class="ma-3 white--text" elevation="0" color="blue"
              >Cancel</v-btn
            >
          </v-row>
        </v-card>
      </v-col>
      <v-col cols="12" md="8">
        <v-card>
          <v-data-table
            :headers="headers"
            :items="desserts"
            sort-by="date"
            class="elevation-1"
          >
            <template v-slot:top>
          
            
                <v-spacer></v-spacer>
                <v-dialog v-model="dialog" max-width="500px">
                  <v-card>
                    <v-card-text>
                      <v-container>
                        <v-row>
                          <v-col cols="12" sm="6" md="4">
                            <v-text-field
                              v-model="editedItem.Number"
                              label="Number"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6" md="4">
                            <v-text-field
                              v-model="editedItem.Airport"
                              label="Airport"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6" md="4">
                            <v-text-field
                              v-model="editedItem.Location"
                              label="Location"
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
                      <v-btn color="blue darken-1" text @click="save">
                        Save
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
                <v-dialog v-model="dialogDelete" max-width="500px">
                  <v-card>
                    <v-card-title class="text-h5"
                      >Are you sure you want to delete this item?</v-card-title
                    >
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" text @click="closeDelete"
                        >Cancel</v-btn
                      >
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="deleteItemConfirm"
                        >OK</v-btn
                      >
                      <v-spacer></v-spacer>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </v-toolbar>
            </template>
            <template v-slot:item.actions="{ item }">
              <v-icon small class="mr-2" @click="editItem(item)">
                mdi-pencil
              </v-icon>
              <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
            </template>
            <template v-slot:no-data>
              <v-btn color="primary" @click="initialize"> Reset </v-btn>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  middleware: "auth-admin",
  data: () => ({
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: "S.N.",
        align: "start",
        sortable: false,
        value: "Number",
      },
      { text: "Airport", value: "Airport" },
      { text: "Location", value: "Location" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    desserts: [],
    editedIndex: -1,
    editedItem: {
      Number: 0,
      Airport: "Tribhuwan International Airport",
      Location: "Kathmandu",
    },
    defaultItem: {
      Number: 0,
      Airport: "Tribhuwan International Airport",
      Location: "Kathmandu",
    },
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
      this.desserts = [
        {
          Number: 1,
          Airport: "Tribhuwan International Airport",
          Location: "Kathmandu",
        },
        {
          Number: 5,
          Airport: "TribhuwCDSCFt",
          Location: "KathmaCSCSCndu",
        },
        {
          Number: 3,
          Airport: "Tribhuwan ICSCrport",
          Location: "KathmCSCCEFWFandu",
        },
      ];
    },

    editItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.desserts.splice(this.editedIndex, 1);
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.desserts[this.editedIndex], this.editedItem);
      } else {
        this.desserts.push(this.editedItem);
      }
      this.close();
    },
  },
};
</script>
