<template>
  <div>
    <v-img src="bg.jpg">
      <v-container class="mb-16">
        <v-row justify="center" class="mt-16">
          <h1>Washington Blog</h1>
        </v-row>
        <v-row>
          <v-card elevation="0">
            <v-img src="wsg.jpg"></v-img>
            <v-row>
              <v-col md="10"> <v-card-text>Photography</v-card-text> </v-col>
              <v-col md="2"> <v-card-text>Washington</v-card-text> </v-col>
            </v-row>
            <v-card-title>Famous Places to Visit in Washington</v-card-title>
            <v-divider></v-divider>
            <v-card-text style="text-align: justify"
              >The natural world is larger than life in the state of Washington.
              The state is stacked with sleeping volcanoes, lush rainforests,
              and islands full of attractions. And surrounding these verdant
              landscapes are cities big and small brimming with cultural appeal.
              Washington State attracts millions of tourists each year. These
              visitors and potential transplants descend upon the state for a
              variety of reasons.</v-card-text
            >
            <v-divider></v-divider>
            <v-card-title>Olympic National Park</v-card-title>
            <v-row>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >From ocean beaches to glaciered mountaintops, Olympic
                  National Park overflows with incomparable scenery. The park
                  covers most of the Olympic Peninsula, and roads only circle
                  the park, never cutting through the park's mountainous heart.
                  While auto-touring is fun, the best way to experience Olympic
                  is by hiking trail. Iconic coastal areas like Ruby and Rialto
                  Beach define the rugged western edge of the park. This
                  stunning slice of Washington coastline is only a short drive
                  away from the oversized trees and abundant foliage found in
                  the Hoh Rain Forest. Other popular attractions at the park
                  include the snowy peaks of Hurricane Ridge and the welcoming
                  waters of Sol Duc Hot Springs. The hiking trails at Olympic
                  National Park traverse many different landscapes, including a
                  Hall of Mosses and the family-friendly Marymere Falls. The Hoh
                  River Trail is an absolute must-do hike for all ages. This
                  lush hiking trail explores the rainforest and river corridor
                  with a flat path for 13 miles before ascending to the lateral
                  moraine of Blue Glacier on Mount Olympus. The Hoh River Trail
                  is an absolute must-do hike for all ages. This lush hiking
                  trail explores the rainforest and river corridor with a flat
                  path for 13 miles before ascending to the lateral moraine of
                  Blue Glacier on Mount Olympus.</v-card-text
                >
              </v-col>
              <v-col md="6">
                <v-img src="CALIF.jpg" class="ma-3"></v-img>
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-card-title>Seattle Center and the Space Needle</v-card-title>
            <v-row>
              <v-col md="6">
                <v-img class="ma-3" src="califf.jpg"></v-img>
              </v-col>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >Of all the top attractions in Seattle, the Space Needle
                  within the Seattle Center is perhaps the most iconic. It was
                  built for the 1962 World's Fair and stands today as a
                  centerpiece of the sprawling Seattle Center. Surrounding the
                  spinning observation deck are more of the city's most iconic
                  attractions, including some of Seattle's best museums.
                  Alongside the Space Needle, the Seattle Center's 74-acre
                  campus is home to the Monorail, parklands, museums, and
                  restaurants. Among the indoor sightseeing options are the
                  colorful glass artworks at Chihuly Garden and Glass and the
                  Frank O. Gehry designed Museum of Pop Culture. Other fun
                  things to check out at the Seattle Center include a plethora
                  of art installations, various theater and stage
                  accommodations, and multiple garden and fountain settings, and
                  on any sunny day in Seattle, the campus offers an excellent
                  place to stroll outside. Alongside the Space Needle, the Seattle Center's 74-acre
                  campus is home to the Monorail, parklands, museums, and
                  restaurants. Among the indoor sightseeing options are the
                  colorful glass artworks at Chihuly Garden and Glass and the
                  Frank O. Gehry designed Museum of Pop Culture.</v-card-text
                >
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
