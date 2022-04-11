<template>
  <div>
    <v-img src="bg.jpg">
      <v-container class="mb-16">
        <v-row justify="center" class="mt-16">
          <h1>Texas Blog</h1>
        </v-row>
        <v-row>
          <v-card elevation="0">
            <v-img src="txs.jpg"></v-img>
            <v-row>
              <v-col md="10"> <v-card-text>Photography</v-card-text> </v-col>
              <v-col md="2"> <v-card-text>Texas</v-card-text> </v-col>
            </v-row>
            <v-card-title
              >Famous Places to Visit in Texas</v-card-title
            >
            <v-divider></v-divider>
            <v-card-text style="text-align: justify"
              >The second largest state in the US, Texas is brimming with
              countless possibilities for fun and adventure. Geographically and
              culturally diverse, the state offers a wealth of unique
              attractions and things to do. From the cities to the coastal
              beaches, mountains, and desert, vacation possibilities in Texas
              are extensive. For nature lovers, some of the best places to visit
              are the parks, like Big Bend National Park, set along a bend in
              the Rio Grande in West Texas, and Padre Island National Sea Shore,
              along the Gulf of Mexico.
            </v-card-text>
            <v-divider></v-divider>
            <v-card-title>San Antonio's River Walk </v-card-title>
            <v-row>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >Stretching for several miles along the San Antonio River in
                  the heart of the city, the River Walk is lined with
                  restaurants and lovely outdoor patios, where you can sit and
                  dine alongside the river. Built below street level, this
                  pedestrian walkway hugs the river as it winds and weaves
                  through the city, and is as popular among locals as it is for
                  tourists, day and night. Although strolling along the river is
                  the most popular thing to do here, another great way to enjoy
                  the ambience of the area is on a leisurely cruise on a river
                  boat. These run all the time and range from standard
                  sightseeing trips to dinner cruises. Stretching for several
                  miles along the San Antonio River in the heart of the city,
                  the River Walk is lined with restaurants and lovely outdoor
                  patios, where you can sit and dine alongside the river. Built
                  below street level, this pedestrian walkway hugs the river as
                  it winds and weaves through the city, and is as popular among
                  locals as it is for tourists, day and night. Although
                  strolling along the river is the most popular thing to do
                  here, another great way to enjoy the ambience of the area is
                  on a leisurely cruise on a river boat. These run all the time
                  and range from standard sightseeing trips to dinner cruises.
                  These run all the time and range from standard sightseeing
                  trips to dinner cruises.</v-card-text
                >
              </v-col>
              <v-col md="6">
                <v-img src="antonio.jpg" class="ma-3"></v-img>
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-card-title>Space Center Houston</v-card-title>
            <v-row>
              <v-col md="6">
                <v-img class="ma-3" src="space.jpg"></v-img>
              </v-col>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >Just 30 minutes' drive from the heart of Houston, Space
                  Center Houston is one of the most popular tourist attractions
                  in Texas. This is a wonderful place to learn about space
                  exploration, upcoming missions, NASA's latest projects, and
                  possibly even meet an astronaut. Space Center Houston is also
                  home to Johnson Space Center and Mission Control, which can be
                  visited on a tour. Plan to spend at least a half-day exploring
                  the entire complex, which includes a space shuttle replica
                  mounted on a shuttle carrier. Visitors can walk inside the
                  shuttle and the carrier. You can also walk inside a replica of
                  America's first space station, Skylab. Other highlights
                  include seeing rockets and touching a rock from the moon and
                  Mars. The center provides a fascinating insight into the
                  operations of the world's largest space program, with
                  countless exhibits, as well as films, models,
                  astronaut-related artifacts, and displays on the experiments
                  and developments at NASA. You can also walk inside a replica of
                  America's first space station, Skylab. Other highlights
                  include seeing rockets and touching a rock from the moon and
                  Mars. The center provides a fascinating insight into the
                  operations of the world's.
                </v-card-text>
              </v-col>
            </v-row>
          </v-card>
        </v-row>
      </v-container>
    </v-img>
  </div>
</template>

<script>
import travel from "../components/travel.vue";

export default {
  components: { travel },
};
</script>

<style></style>
