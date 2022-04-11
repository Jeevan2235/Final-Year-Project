<template>
  <div>
    <v-img src="bos.jpg" height="650px"> </v-img>
    <h1
      class="text-center mt-16"
      style="font-family: Playfair Display, serif; color: #0e385d"
    >
      Overview of Seattle To Boston
    </h1>
    <v-container>
      <p class="mt-10" style="text-align: justify">
        Perhaps no other city in America holds as much history of the colonial
        and Revolutionary War era as Boston. It's not surprising then that its
        main sites have become a pilgrimage trail for Americans and for others
        who hope to get a sense of that history. But more than that, the Freedom
        Trail is a good introduction to today's city, connecting or passing
        close to some of its best loved tourist attractions. Boston is easy to
        navigate on foot, as its major sights are relatively close, and
        America's first subway system, the T, connects its important
        neighborhoods.
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
