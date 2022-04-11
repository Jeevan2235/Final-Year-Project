<template>
  <div>
    <v-img src="haw.jpg"> </v-img>
    <h1
      class="text-center mt-16"
      style="font-family: Playfair Display, serif; color: #0e385d"
    >
      Overview of Washington To Hawai
    </h1>
    <v-container>
      <p class="mt-10" style="text-align: justify">
        Hawaii's tropical climate and laid-back Pacific Island atmosphere are
        just part of what makes the state so special. Occupying the tops of
        massive volcanic mountaintops jutting from the sea, these islands have a
        diverse and beautiful landscape that varies from the stark lunar surface
        of the Kilauea volcano to lush green forests filled with exotic flowers.
        The boardwalk, known as the Waikiki Beach Walk, is lined with cafes and
        entertainment venues, while Kuhio and KalaKaua Avenues are where the
        bulk of the area's restaurants and boutiques can be found. Diamond Head
        State Monument sits at the end of the crescent-shaped beach, creating a
        distinctive profile on the coastline.
      </p>
    </v-container>
    <flightdetails />
  </div>
</template>

<script>
import flightdetails from "~/components/flightdetails.vue";

export default {
  components: { flightdetails },
};
</script>

<style></style>
