<template>
  <div>
    <v-img src="mimi.jpg"> </v-img>
    <h1
      class="text-center mt-16"
      style="font-family: Playfair Display, serif; color: #0e385d"
    >
      Overview of Miami To New York
    </h1>
    <v-container>
      <p class="mt-10" style="text-align: justify">
        New York has to be one of the most famous cities in the world. Often
        referred to as the 'Big Apple', this vibrant city is known for its
        exclusive shops, flashy Broadway performances, and high-flying business
        tycoons, and it's a city that has long captivated people from all over
        the world. The first stop is the statue, where visitors can enjoy views
        of both the monument and the New York City skyline at no charge. You can
        also purchase tickets to access the pedestal or crown, although crown
        passes sell out at least six months in advance. Be sure to wander
        through the museum in the base of the statue and check out the extensive
        educational signs, statues, and historic markers.
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
