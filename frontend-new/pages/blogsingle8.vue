<template>
  <div>
    <v-img src="bg.jpg">
      <v-container class="mb-16">
        <v-row justify="center" class="mt-16">
          <h1>Virginia Blog</h1>
        </v-row>
        <v-row>
          <v-card elevation="0">
            <v-img src="virgin.jpg"></v-img>
            <v-row>
              <v-col md="10"> <v-card-text>Photography</v-card-text> </v-col>
              <v-col md="2"> <v-card-text>Virginia</v-card-text> </v-col>
            </v-row>
            <v-card-title
              >Famous Places To Visit In Virginia</v-card-title
            >
            <v-divider></v-divider>
            <v-card-text style="text-align: justify"
              >History is everywhere in Virginia. Four of the first five
              presidents were born in the state, giving it a head start on the
              record of eight, the most of any state. Two of its top tourist
              attractions – Mount Vernon and Monticello – are homes of
              presidents. Virginia also claims the most Civil War battlefields
              of any state and the places where both the Revolution and the
              Civil War ended.</v-card-text
            >
            <v-divider></v-divider>
            <v-card-title
              >Shenandoah National Park and Skyline Drive</v-card-title
            >
            <v-row>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >In the center of Virginia, Shenandoah National Park protects
                  portions of the Blue Ridge Mountains, which range in height
                  between 2,000 and 4,000 feet. Along their crest and running
                  the length of the park is the Skyline Drive, the northern
                  continuation of the Blue Ridge Parkway, with stopping points
                  to enjoy the views and attractions, including President
                  Hoover's summer residence and the old Cave Cemetery below Dark
                  Hollow Falls. The beautiful hiking trails are some of the
                  park's main attractions. Flowering trees and shrubs are at
                  their finest in spring and summer, but the park is best known
                  for its autumn colors in October. Only a short drive west from
                  the Skyline Drive on US 211 are Luray Caverns containing
                  magnificent formations of stalactites and stalagmites. In the
                  center of Virginia, Shenandoah National Park protects portions
                  of the Blue Ridge Mountains, which range in height between
                  2,000 and 4,000 feet. Along their crest and running the length
                  of the park is the Skyline Drive, the northern continuation of
                  the Blue Ridge Parkway, with stopping points to enjoy the
                  views and attractions, including President Hoover's summer
                  residence and the old Cave Cemetery below Dark Hollow Falls.
                  The beautiful hiking trails are some of the park's main
                  attractions. Flowering trees and shrubs are at their finest in
                  spring and summer, but the park is best known for its autumn
                  colors in October.
                </v-card-text>
              </v-col>
              <v-col md="6">
                <v-img src="park.jpg" class="ma-3"></v-img>
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-card-title>Colonial Williamsburg</v-card-title>
            <v-row>
              <v-col md="6">
                <v-img class="ma-3" src="colo.jpg"></v-img>
              </v-col>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >Few places can recreate a setting for the period of the
                  American Revolution as well as Williamsburg, where the
                  original 18th-century buildings are either still standing or
                  have been faithfully reproduced on their original foundations.
                  Here, you can stand where Patrick Henry gave his stirring
                  speech, walk the same streets as Thomas Jefferson, and savor a
                  meal where George Washington enjoyed seafood dinners.
                  Williamsburg was the capital of Virginia from 1705 and
                  throughout the Revolution, and the final battle of the war was
                  fought nearby, so it was a hotbed of the independence
                  movement, along with being one of the most prosperous and
                  politically active colonial capitals. Costumed interpreters
                  help show what life was like for the gentry, the farmers, and
                  the slaves that lived and worked here, and frequent
                  re-enactments add color and action that makes Williamsburg a
                  fun place to visit for all ages. In addition, you can visit
                  two outstanding museums of folk and decorative arts and dozens
                  of authentically recreated colonial gardens. In addition, you can visit
                  two outstanding museums of folk and decorative arts and dozens
                  of authentically recreated colonial gardens. In addition, you can visit
                  two outstanding museums of folk and decorative arts and dozens
                  of authentically recreated colonial gardens.</v-card-text
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
