<template>
  <div class="mt-16">
    <v-container>
      <v-row>
        <v-col cols="12" md="4">
          <h2 style="font-family: Playfair Display, serif; color: #0e385d">
            Departure 
          </h2>
          <div class="mt-5" v-for="link in links" :key="link">
            <p>{{ link }}</p>
            <v-divider></v-divider>
          </div>
        </v-col>
        <v-col cols="12" md="3">
          <h2 style="font-family: Playfair Display, serif; color: #0e385d">
            Arrival 
          </h2>
          <div class="mt-5" v-for="thing in things" :key="thing">
            <p>{{ thing }}</p>
            <v-divider></v-divider>
          </div>
        </v-col>
        <v-col cols="12" md="3">
          <h2 style="font-family: Playfair Display, serif; color: #0e385d">
            Airlines
          </h2>
          <div class="mt-5" v-for="wifi in wifis" :key="wifi">
            <p>{{ wifi }}</p>
            <v-divider></v-divider>
          </div>
        </v-col>
        <v-col cols="12" md="2">
          <h2 style="font-family: Playfair Display, serif; color: #0e385d">
            Fares
          </h2>
          <div class="mt-5" v-for="phone in phones" :key="phone">
            <p>{{ phone }}</p>
            <v-divider></v-divider>
          </div>
        </v-col>
      </v-row>
    </v-container>
    <h1
      class="text-center mt-16 mb-10"
      style="font-family: Playfair Display, serif; color: #0e385d"
    >
      Similar Packages
    </h1>
    <v-container>
      <v-row justify="center" class="mt-5">
      <v-col cols="12" md="3" >
        <v-card class="mb-16" elevation="1" to="/flights">
          <v-img src="texas.jpg"  height="250"> </v-img>
          <v-card-title>Texas To Colorado</v-card-title>
          <v-card-text></v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="3" >
        <v-card class="mb-16" elevation="1" to="/flights2">
          <v-img src="newyrk.jpg"  height="250"> </v-img>
          <v-card-title>Miami To New York</v-card-title>
          <v-card-text></v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="3" >
        <v-card class="mb-16" elevation="1" to="/flight3">
          <v-img src="boston.jpg" height="250"> </v-img>
          <v-card-title>Seattle To Boston</v-card-title>
          <v-card-text></v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="3" >
        <v-card class="mb-16" elevation="1" to="/flight4">
          <v-img src="hawai.jpg"  height="250"> </v-img>
          <v-card-title>Washington To Hawai</v-card-title>
          <v-card-text></v-card-text>
        </v-card>
      </v-col>
    </v-row>
    </v-container>
  </div>
</template>

<script>
import deals from "./deals.vue";
export default {
  components: { deals },
  data: () => ({
    links: [
      "1 : 45 AM",
      "2 : 45 AM",
      "3 : 45 AM",
      "4 : 45 AM",
      "5 : 45 AM",
      "6 : 45 AM",
    ],

    things: [
      "1 : 45 AM",
      "2 : 45 AM",
      "3 : 45 AM",
      "4 : 45 AM",
      "5 : 45 AM",
      "6 : 45 AM",
    ],

    wifis: [
      "American Airlines",
      "United Airlines",
      "Alaska Airlines",
      "JetBlue Airways",
      "Cape Air",
      "Frontier Airlines",
    ],

    phones: ["$200", "$100", "$350", "$150", "$70", "$125"],
  }),
};
</script>

<style></style>
