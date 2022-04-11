<template>
  <v-container>
    <h1
      class="text-center"
      style="font-family: Playfair Display, serif; color: #0e385d"
    >
      Featured Flight Deals
    </h1>
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
</template>

<script>
export default {
  
};
</script>

<style></style>
