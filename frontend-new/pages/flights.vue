<template>
  <div>
    <v-img src="wing.jpg"> </v-img>
    <h1
      class="text-center mt-16"
      style="font-family: Playfair Display, serif; color: #0e385d"
    >
      Overview of Texas To Colorado
    </h1>
    <v-container>
      <p class="mt-10" style="text-align: justify">
        Colorado is the ideal winter destination with unparalleled skiing and
        snowboarding, snowshoeing, snowmobiling, fat-biking, snowtubing,
        seasonal festivals, a rich cultural heritage and so much more. Plan your
        Colorado vacation now and find out if you're Colo-Ready! The scenic
        byways of Colorado connect the dots between historic sites and acres of
        majestic scenery that span red-rock canyons, the peaks of the Rocky
        Mountains and sun-kissed prairies. Find videos, trip tips, itineraries
        and more.
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
