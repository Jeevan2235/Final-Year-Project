<template>
  <div>
    <div v-for="link in links" :key="link">
      <v-img :src="link.img">
        <h1
          class="text-center"
          style="
            font-size: 60px;
            font-family: Playfair Display, serif;
            color: #0e385d;
          "
        >
          {{ link.text }}
        </h1>
        <p
          class="text-center"
          style="
            font-size: 30px;
            font-family: Playfair Display, serif;
            color: #0e385d;
          "
        >
          {{ link.desc }}
        </p>

        <v-row justify="center">
          <v-card width="35em" class="mb-10 mt-5">
            <p
              class="text-center"
              style="
                font-size: 30px;
                font-family: Playfair Display, serif;
                color: #0e385d;
              "
            >
              SEARCH FOR FLIGHTS
            </p>

            <v-row>
              <v-col md="12" cols="12">
                <oneway />
              </v-col>
            </v-row>
          </v-card>
        </v-row>
      </v-img>
    </div>
  </div>
</template>

<script>
import oneway from "./oneway.vue";

export default {
  components: { oneway },

  data: () => ({
    links: [
      {
        text: "Book your next flight with us",
        img: "airport.png",
        desc: "Search from 100s of different flights that suites the best for your next trip",
      },
    ],
  }),
};
</script>

<style></style>
