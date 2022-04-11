<template>
  <div>
    <v-card height="45em" width="23em" v-for="thing in things" :key="thing">
      <v-container>
        <v-card-title class="text-center">{{ thing.title }}</v-card-title>
        <v-btn class="ma-2 white--text" color="blue" width="8em">{{
          thing.btn1
        }}</v-btn>
        <v-btn class="ma-2 white--text" color="blue" width="8em">{{
          thing.btn2
        }}</v-btn>
        <div class="mt-8">
          <v-text-field outlined label="KATHMANDU"> </v-text-field>
          <v-text-field outlined label="BHOJPUR"> </v-text-field>
          <v-text-field outlined label="Departure Date"> </v-text-field>
          <v-text-field outlined label="Return Date"> </v-text-field>

          <v-text-field label="Number of Adults(12yrs+) : 1"> </v-text-field>
          <v-text-field label="Number of Child(02-12yrs)"> </v-text-field>
          <div class="text-center">
            <v-btn class="white--text mt-2" color="blue" width="22em"
              >Search Flight</v-btn
            >
          </div>
        </div>
      </v-container>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    things: [
      {
        title: "BOOK A FLIGHT",
        btn1: "One Way",
        btn2: "Round Trip",
        from: "KTM",
        location: "Tribhuwan International Airport",
        to: "BJP",
        location2: "Bhojpur Airport",
        date: "10 Dec, 2021",
      },
    ],
  }),
};
</script>

<style></style>
