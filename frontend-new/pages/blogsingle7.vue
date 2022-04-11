<template>
  <div>
    <v-img src="bg.jpg">
      <v-container class="mb-16">
        <v-row justify="center" class="mt-16">
          <h1>Florida Blog</h1>
        </v-row>
        <v-row>
          <v-card elevation="0">
            <v-img src="flo.jpg"></v-img>
            <v-row>
              <v-col md="10"> <v-card-text>Photography</v-card-text> </v-col>
              <v-col md="2"> <v-card-text>Miami</v-card-text> </v-col>
            </v-row>
            <v-card-title
              >Famous Places to Visit in Florida</v-card-title
            >
            <v-divider></v-divider>
            <v-card-text style="text-align: justify"
              >Beaches, amusement parks, national parks, and an array of unique
              tourist attractions make Florida one of the most visited states in
              America. Families flock to Orlando to thrill the kids with visits
              to the theme parks, while sunseekers head to the coastal cities
              like Miami, Fort Lauderdale, and a string of cities along the
              southern Gulf Coast. In summer, visitors from around Florida and
              surrounding states often escape the heat and head to the cooling
              breezes and brilliant white-sand beaches of the Florida Panhandle.
            </v-card-text>
            <v-divider></v-divider>
            <v-card-title>Walt Disney World</v-card-title>
            <v-row>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >For the ultimate amusement park experience, there's no place
                  quite like Disney World in Orlando. The magic of Disney has
                  not worn off over the decades as millions of visitors come
                  here each year to enjoy the Magic Kingdom and the many other
                  attractions of this mega amusement park. The number of things
                  to do and see here has grown over the years and now includes
                  an extensive list that reaches far beyond the traditional
                  theme parks. If you're looking for more ideas, consider
                  checking out the water parks of Blizzard Beach and Typhoon
                  Lagoon, the exotic animals of Animal Kingdom Park, or Disney
                  Hollywood Studios. You'll also find exceptional dining
                  experiences, shopping areas, and shows, some of which are
                  target to adults only. For the ultimate amusement park
                  experience, there's no place quite like Disney World in
                  Orlando. The magic of Disney has not worn off over the decades
                  as millions of visitors come here each year to enjoy the Magic
                  Kingdom and the many other attractions of this mega amusement
                  park. The number of things to do and see here has grown over
                  the years and now includes an extensive list that reaches far
                  beyond the traditional theme parks. If you're looking for more
                  ideas, consider checking out the water parks of Blizzard Beach
                  and Typhoon Lagoon, the exotic animals of Animal Kingdom Park,
                  or Disney Hollywood Studios. You'll also find exceptional
                  dining experiences, shopping areas, and shows.
                </v-card-text>
              </v-col>
              <v-col md="6">
                <v-img src="walt.jpg" class="ma-3"></v-img>
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-card-title
              >Miami Beach and the Art Deco Historic District</v-card-title
            >
            <v-row>
              <v-col md="6">
                <v-img class="ma-3" src="miam.jpg"></v-img>
              </v-col>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >Although time spent lounging on the beach on a hot day is a
                  must, Miami Beach is about much more than just the glorious,
                  wide stretch of golden sand that lines the Atlantic. One of
                  the things that makes Miami Beach so unique among Florida's
                  beach destinations is the Art Deco Historic District.
                  Beautifully restored buildings, mainly from the 1930s and
                  early 1940s, reflect the city's vibrant history and create an
                  ambience like you won't find in other cities. Today, many of
                  these buildings are high-end hotels, condominiums, and
                  restaurants. Along Ocean Drive, the legendary oceanfront
                  street overlooking South Beach, you'll find several
                  outstanding Art Deco buildings, including the Hotel Breakwater
                  South Beach, The Carlyle, and the Park Central Hotel (now part
                  of the new Celino Hotel complex). Collins Avenue is another
                  street in the area worth strolling along, with more classic
                  buildings. The Delano South Beach and the National Hotel Miami
                  Beach are both standout Art Deco properties along Collins
                  Avenue. Along Ocean Drive, the legendary oceanfront
                  street overlooking South Beach, you'll find several
                  outstanding Art Deco buildings, including the Hotel Breakwater
                  South Beach, The Carlyle, and the Park Central Hotel (now part
                  of the new Celino Hotel complex). Collins Avenue is another
                  street in the area worth strolling along, with more classic
                  buildings. </v-card-text
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
