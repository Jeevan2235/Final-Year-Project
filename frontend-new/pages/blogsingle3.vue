<template>
  <div>
    <v-img src="bg.jpg">
      <v-container class="mb-16">
        <v-row justify="center" class="mt-16">
          <h1>California Blog</h1>
        </v-row>
        <v-row>
          <v-card elevation="0">
            <v-img src="clf.jpg"></v-img>
            <v-row>
              <v-col md="10"> <v-card-text>Photography</v-card-text> </v-col>
              <v-col md="2"> <v-card-text>California</v-card-text> </v-col>
            </v-row>
            <v-card-title>Famous Places to Visit in California</v-card-title>
            <v-divider></v-divider>
            <v-card-text style="text-align: justify"
              >California is one of the top vacation destinations in the United
              States, both for Americans and international travelers. Vibrant
              cities, beaches, amusement parks, and natural wonders like nowhere
              else on Earth make California an intriguing land of possibilities
              for travel. The gateway cities of San Francisco and Los Angeles
              are home to some of the state's most well-known sites, from the
              Golden Gate Bridge to Hollywood and Disneyland. This is also where
              many of the top cultural attractions can be found.</v-card-text
            >
            <v-divider></v-divider>
            <v-card-title
              >San Francisco and the Golden Gate Bridge</v-card-title
            >
            <v-row>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >One of the most beautiful cities in America, San Francisco
                  should be on everyone's must-see list. The ocean and hills
                  provide a stunning natural setting, but the quaint
                  neighborhoods, historic sites, green spaces, inspiring
                  cultural institutions, and relaxed attitude are what truly
                  make this city special. The iconic Golden Gate Bridge is one
                  of the key sights and what many people call to mind when they
                  think of the San Francisco, and even California. The orange
                  frame against the blue water of San Francisco Bay, or rising
                  out of the fog that often covers the area is an unforgettable
                  sight. You can appreciate the bridge from afar or, for a more
                  personal experience, drive over it, walk on it, or even bike
                  across it. Other popular tourist attractions include
                  Fisherman's Wharf and the infamous Alcatraz Island. This
                  former jail is now a national park and well worth a visit.
                  Ferries leave for the island from Pier 33 near Fisherman's
                  Wharf. If you have time to explore the city and are up for a
                  little exercise, see some of the sights on foot. Families
                  traveling with children will find a world of activities to
                  entertain youngsters and even older children with our article
                  on things to do with kids in San Francisco. Other popular
                  tourist attractions include Fisherman's Wharf and the infamous
                  Alcatraz Island. This former jail is now a national park and
                  well worth a visit.
                </v-card-text>
              </v-col>
              <v-col md="6">
                <v-img src="bridge.jpg" class="ma-3"></v-img>
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-card-title> Disneyland</v-card-title>
            <v-row>
              <v-col md="6">
                <v-img class="ma-3" src="disney.jpg"></v-img>
              </v-col>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >Disneyland, located in Anaheim, is California's premier
                  family destination and has been for decades. This massive
                  amusement park is home to all kinds of rides, games, shows,
                  and entertainment, complete with restaurants and hotels. The
                  park is a combination of theme rides and recreated worlds and
                  cultures. You can find shows and other entertainment designed
                  for both children and adults. Long line ups and wait times
                  have been reduced somewhat by the invention of FastPass+,
                  which gives you the ability to book specific ride times, a hug
                  with a character, and entertainment events. However, when kids
                  are out of school, either for the summer, Christmas, spring
                  break, or any other holiday, you can be sure that the park
                  will be very busy. Keep in mind there is more to Disneyland
                  than just the parks. The entire Disneyland resort experience
                  features hotels, dining, shopping at the Downtown Disney
                  District, and the Disney Adventure Park. Although the parks
                  are definitely what your children are here to see, you'll find
                  something fun for everyone in the family.  Keep in mind there is more to Disneyland
                  than just the parks. The entire Disneyland resort experience
                  features hotels, dining, shopping at the Downtown Disney
                  District, and the Disney Adventure Park. The
                  park is a combination of theme rides and recreated worlds and
                  cultures. You can find shows and other entertainment designed
                  for both children and adults. Long line ups and wait times
                  have been reduced somewhat by the invention of FastPass+,
                  which gives you the ability to book specific ride times, a hug
                  with a character.</v-card-text
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
