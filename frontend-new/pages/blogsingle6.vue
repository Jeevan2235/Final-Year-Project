<template>
  <div>
    <v-img src="bg.jpg">
      <v-container class="mb-16">
        <v-row justify="center" class="mt-16">
          <h1>Hawai Blog</h1>
        </v-row>
        <v-row>
          <v-card elevation="0">
            <v-img src="hwi.jpg"></v-img>
            <v-row>
              <v-col md="10"> <v-card-text>Photography</v-card-text> </v-col>
              <v-col md="2"> <v-card-text>Hawai</v-card-text> </v-col>
            </v-row>
            <v-card-title>Famous Places to Visit in Hawai</v-card-title>
            <v-divider></v-divider>
            <v-card-text style="text-align: justify"
              >Hawaii's tropical climate and laid-back Pacific Island atmosphere
              are just part of what makes the state so special. Occupying the
              tops of massive volcanic mountaintops jutting from the sea, these
              islands have a diverse and beautiful landscape that varies from
              the stark lunar surface of the Kilauea volcano to lush green
              forests filled with exotic flowers.
            </v-card-text>
            <v-divider></v-divider>
            <v-card-title
              >Waikiki Beach and Diamond Head State Monument</v-card-title
            >
            <v-row>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >Waikiki, with its beautiful stretch of oceanfront beach, is
                  Hawaii's biggest tourist attraction. A suburb of Honolulu,
                  Waikiki is popular for its big resorts, dining, entertainment,
                  and shopping. The Waikiki Historic Trail includes historic
                  markers made of surfboards, inspired by Waikiki's own Duke
                  Kahanamoku, an Olympic gold medalist swimmer and avid surfer.
                  The boardwalk, known as the Waikiki Beach Walk, is lined with
                  cafes and entertainment venues, while Kuhio and KalaKaua
                  Avenues are where the bulk of the area's restaurants and
                  boutiques can be found. Diamond Head State Monument sits at
                  the end of the crescent-shaped beach, creating a distinctive
                  profile on the coastline. It was once an important vantage
                  point for the island's coastal defense, and a steep hike to
                  the top brings you to the old bunkers and artillery control
                  station and rewards your efforts with panoramic views. Diamond
                  Head State Monument sits at the end of the crescent-shaped
                  beach, creating a distinctive profile on the coastline. It was
                  once an important vantage point for the island's coastal
                  defense, and a steep hike to the top brings you to the old
                  bunkers and artillery control station and rewards your efforts
                  with panoramic views. It was once an important vantage point
                  for the island's coastal defense, and a steep hike to the top
                  brings you to the old bunkers and artillery control station
                  and rewards your efforts with panoramic views.</v-card-text
                >
              </v-col>
              <v-col md="6">
                <v-img src="waiki.jpg" class="ma-3"></v-img>
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-card-title> Pearl Harbor and USS Arizona Memorial</v-card-title>
            <v-row>
              <v-col md="6">
                <v-img class="ma-3" src="pearl.jpg"></v-img>
              </v-col>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >Pearl Harbor is a National Historic Landmark and active
                  military base that earned its place in history for the 1941
                  attack, which killed 1,177 servicemen on the USS Arizona. The
                  site is now home to several attractions that are part of the
                  World War II Valor in the Pacific Monument, including the USS
                  Arizona Memorial, which floats above the remains of the sunken
                  ship - parts of which can be seen protruding from the water.
                  There is no cost for a tour of the memorial, however
                  reservations are recommended due to its popularity. The Pearl
                  Harbor Visitor Center has free admission and is the meeting
                  place for tours, including transportation to the Pacific
                  Aviation Museum on Ford Island, where visitors can see WWII
                  aircraft and artifacts, as well as experience landing an
                  airplane on an aircraft carrier in a flight simulator. Other
                  attractions include the USS Oklahoma, USS Utah, and the
                  Battleship USS Missouri whose deck can be toured by visitors.
                  Aviation Museum on Ford Island, where visitors can see WWII
                  aircraft and artifacts, as well as experience landing an
                  airplane on an aircraft carrier in a flight simulator. Other
                  attractions include the USS Oklahoma, USS Utah, and the
                  Battleship USS Missouri whose deck can be toured by visitors. Other
                  attractions include the USS Oklahoma, USS Utah.
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
