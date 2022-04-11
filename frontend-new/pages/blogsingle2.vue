<template>
  <div>
    <v-img src="bg.jpg">
      <v-container class="mb-16">
        <v-row justify="center" class="mt-16">
          <h1>Boston Blog</h1>
        </v-row>
        <v-row>
          <v-card elevation="0">
            <v-img src="bstn.jpg"></v-img>
            <v-row>
              <v-col md="10"> <v-card-text>Photography</v-card-text> </v-col>
              <v-col md="2"> <v-card-text>Boston</v-card-text> </v-col>
            </v-row>
            <v-card-title
              >Famous Places To Visit In Boston</v-card-title
            >
            <v-divider></v-divider>
            <v-card-text style="text-align: justify"
              >Perhaps no other city in America holds as much history of the
              colonial and Revolutionary War era as Boston. It's not surprising
              then that its main sites have become a pilgrimage trail for
              Americans and for others who hope to get a sense of that history.
              But more than that, the Freedom Trail is a good introduction to
              today's city, connecting or passing close to some of its best
              loved tourist attractions. Boston is easy to navigate on foot, as
              its major sights are relatively close, and America's first subway
              system, the T, connects its important neighborhoods.
            </v-card-text>
            <v-divider></v-divider>
            <v-card-title>Walk the Freedom Trail</v-card-title>
            <v-row>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >The three-mile Freedom Trail leads you past – and into – 16
                  of the city's principal historic monuments and sites. It's
                  easy to follow, by the line of red bricks in the sidewalk and
                  by footprints at street crossings. Begin by picking up
                  brochures on the attractions at the Visitor Center in the
                  Boston Common before heading to the State House. The trail
                  will take you to Old Granary Burying Ground (where Paul
                  Revere, Samuel Adams, and John Hancock are buried), King's
                  Chapel Burying Ground (Boston's oldest cemetery with the
                  graves of Governor John Winthrop and two Mayflower
                  passengers), Old South Meeting House (where the ringing
                  speeches of patriots spawned the Boston Tea Party), and the
                  Old State House. This is Boston's oldest public building and
                  the site of the Boston Massacre. The Freedom Trail continues
                  through Boston's North End, past the Paul Revere House and Old
                  North Church, and ends across the bridge in Charlestown with
                  the 54-gun frigate USS Constitution and the 220-foot granite
                  Bunker Hill Monument. The trail will take you to Old Granary
                  Burying Ground (where Paul Revere, Samuel Adams, and John
                  Hancock are buried), King's Chapel Burying Ground (Boston's
                  oldest cemetery with the graves of Governor John Winthrop and
                  two Mayflower.</v-card-text
                >
              </v-col>
              <v-col md="6">
                <v-img src="three.jpg" class="ma-3"></v-img>
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-card-title>Faneuil Hall</v-card-title>
            <v-row>
              <v-col md="6">
                <v-img class="ma-3" src="fauc.jpg"></v-img>
              </v-col>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >Known as the "cradle of liberty," Faneuil Hall was built in
                  1740-42 by Huguenot merchant Peter Faneuil as a market hall
                  and presented to the city on condition that it should always
                  be open to the public. The ground floor is still occupied by
                  market stalls; on the upper floor is a council chamber, which
                  in the 18th and 19th centuries was the meeting place of
                  revolutionaries and later, of abolitionists. On its fourth
                  floor is the Ancient and Honorable Artillery Museum, with
                  weaponry, uniforms, and paintings of significant battles. The
                  adjoining Faneuil Hall Marketplace includes three long halls
                  (Quincy Market, North Market, and South Market), dating from
                  the early 19th century, now occupied by a lively assortment of
                  shops, restaurants, and exhibitions. In good weather, you'll
                  find street performers and buskers putting on shows in the
                  square around the market, and along with the numerous food
                  stalls, there are also shops selling jewelry, clothing, gifts,
                  and souvenirs. The market stalls are some of the favorite
                  places to eat lunch in Boston. The ground floor is still occupied by
                  market stalls; on the upper floor is a council chamber, which
                  in the 18th and 19th centuries was the meeting place of
                  revolutionaries and later, of abolitionists.</v-card-text
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
