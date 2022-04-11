<template>
  <div>
    <v-img src="pen.jpg">
      <v-container class="mb-16">
        <v-row justify="center" class="mt-16">
          <h1>Pennsylvania Blog</h1>
        </v-row>
        <v-row>
          <v-card elevation="0">
            <v-img src="pen.jpg"></v-img>
            <v-row>
              <v-col md="10"> <v-card-text>Photography</v-card-text> </v-col>
              <v-col md="2"> <v-card-text>Pennsylvania</v-card-text> </v-col>
            </v-row>
            <v-card-title>Famous Places To Visit In Pennsylvania</v-card-title>
            <v-divider></v-divider>
            <v-card-text style="text-align: justify"
              >Pennsylvania is known as the Keystone State for its role in
              building the foundations of the United States of America. It is
              here that the Declaration of Independence, U.S. Constitution, and
              the Gettysburg Address were written. Tourists will find an
              abundance of historic landmarks and attractions, from the Liberty
              Bell in Philadelphia to the Valley Forge and Gettysburg battle
              sites. It is also known as the Quaker State for the religion of
              the state's namesake, William Penn.
            </v-card-text>
            <v-divider></v-divider>
            <v-card-title
              >Independence National Park and the Liberty Bell</v-card-title
            >
            <v-row>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >One of America's most historic areas and home to the Liberty
                  Bell, Independence National Historical Park in Philadelphia is
                  a national treasure. Independence Hall is the central
                  attraction at the park, famous as the site where the
                  Declaration of Independence was signed and where the
                  Constitution was drafted. The Liberty Bell sits on display
                  across from Independence Hall, surrounded by a series of
                  exhibits describing its history. Independence Mall, laid out
                  in 1948, extends north of here, forming the remainder of the
                  park, which is paved with old cobblestone streets. Here, you
                  will find historic buildings, like Congress Hall and Old City
                  Hall, and museums including the Ben Franklin Museum and the
                  National Museum of American Jewish History. Independence Mall,
                  laid out in 1948, extends north of here, forming the remainder
                  of the park, which is paved with old cobblestone streets.
                  Here, you will find historic buildings, like Congress Hall and
                  Old City Hall, and museums including the Ben Franklin Museum
                  and the National Museum of American Jewish History.
                  Independence Mall, laid out in 1948, extends north of here,
                  forming the remainder of the park, which is paved with old
                  cobblestone streets. Here, you will find historic buildings,
                  like Congress Hall and Old City Hall, and museums including
                  the Ben Franklin Museum and the National Museum of American
                  Jewish History.
                </v-card-text>
              </v-col>
              <v-col md="6">
                <v-img src="ind.jpg" class="ma-3"></v-img>
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-card-title> Hershey Park</v-card-title>
            <v-row>
              <v-col md="6">
                <v-img class="ma-3" src="her.jpg"></v-img>
              </v-col>
              <v-col md="6">
                <v-card-text style="text-align: justify"
                  >Families will enjoy an outing to this famous amusement park
                  in Hershey, a town also closely associated with chocolate.
                  Hershey Park is the town's main attraction with 90 acres of
                  rides and entertainment for kids and adults, ranging from
                  roller coasters to aquatic shows. The park was originally
                  built in 1906 as a recreational area for Hershey's workers but
                  expanded over the years to attract visitors from all over.
                  Hershey Park continues to expand, offering a wide range of
                  things to do for all ages. In addition to kiddie rides, the
                  park has all the family favorites like a carousel, train,
                  bumper cars, and Ferris wheel. There are also several water
                  rides perfect for a hot summer's day and more than a dozen
                  roller coasters designed to thrill. Other attractions include
                  midway-style games and two large video arcades. Adjacent to
                  the park and included in admission is ZooAmerica. Here,
                  visitors can see more than 200 animals from North American
                  habitats, including bald eagles, mountain lions, and even
                  roadrunners. Zoo guests can also sign up for special
                  behind-the-scenes tours to get a closer look and an
                  opportunity to help feed the animals. For those who want to
                  skip the big park and just visit the zoo, admission is
                  available at a lower rate. For those who want to
                  skip the big park and just visit the zoo, admission is
                  available at a lower rate.</v-card-text
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
