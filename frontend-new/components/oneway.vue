<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="4">
        <v-card-text>Departure Date</v-card-text>
        <client-only
          ><date-picker
            placeholder="YYYY/MM/DD"
            :format="format"
            input-class="my-picker-class"
            v-model="values.departure_date"
            :rules="[rules.required]"
        /></client-only>
        <!-- <v-select outlined> -->
        <!-- <v-row justify="center">
            <v-date-picker v-model="picker"></v-date-picker>
          </v-row> -->
        <!-- </v-select> -->
      </v-col>
      <v-col cols="12" md="4">
        <v-card-text>From</v-card-text>
        <v-select
          outlined
          :items="from"
          v-model="values.departure_location"
          :rules="[rules.required]"
        >
          <template #search="{ attributes, events }">
            <input
              class="vs__search"
              :required="!values.departure_location"
              v-bind="attributes"
              v-on="events"
            />
          </template>
        </v-select>
      </v-col>
      <v-col cols="12" md="4">
        <v-card-text>To</v-card-text>
        <v-select
          outlined
          :items="to"
          v-model="values.arrival_location"
        ></v-select>
      </v-col>
    </v-row>
    <v-row style="margin-bottom: 4em">
      <v-col cols="12" md="4">
        <v-card-text>Adult</v-card-text>
        <v-select
          :items="adult"
          :clearable="false"
          v-model="values.adult"
        ></v-select>
      </v-col>
      <v-col cols="12" md="4">
        <v-card-text>Child</v-card-text>
        <v-select
          :items="child"
          :clearable="false"
          v-model="values.child"
        ></v-select>
      </v-col>
      <v-col cols="12" md="4"
        ><v-btn
          height="4em"
          color="#15aabe"
          class="mt-14 white--text mb-5"
          to="/booking"
          :disabled="isDisabled"
        >
          <!-- <router-link
            :to="{
              path: '/booking',
              query: this.values,
            }"
          >
            Search Flights</router-link
          > -->

          <nuxt-link
            :to="{
              path: '/booking',
              query: {
                ...this.values,
                departure_date: new Date(this.values.departure_date)
                  .toISOString()
                  .substring(0, 10),
              },
            }"
            >Search Flights</nuxt-link
          >
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: function () {
    return {
      format: "yyyy-MM-dd",
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
      rules: {
        required: (value) => !!value || "Required.",
      },
    };
  },

  computed: {
    isDisabled() {
      return !(
        this.values.arrival_location.length > 0 &&
        this.values.departure_location.length > 0 &&
        this.values.departure_date &&
        this.values.adult &&
        this.values.child
      );
    },
  },
};
</script>

<style>
.my-picker-class {
  border: none !important;
  border-bottom: 1px solid black !important;
  max-width: 100%;
  padding: 12px;
}
</style>
