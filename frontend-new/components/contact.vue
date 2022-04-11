<template>
  <v-row>
    <v-col md="6">
      <v-row v-for="link in links" :key="link">
        <v-card class="ma-2" width="30em" elevation="0" tile color="#f5f5f5">
          <v-container>
            <v-card-title style="font-family: Playfair Display, serif; color: #0e385d">{{ link.text }}</v-card-title>

            <v-card-text >
              {{ link.text1 }}
            </v-card-text>
          </v-container>
        </v-card>
      </v-row>
    </v-col>
    <v-col md="6">
      <v-card
        v-for="thing in things"
        :key="thing"
        elevation="0"
        tile
        color="#f5f5f5"
        class="mb-16 pa-6"
      >
        <v-container>
          <h1 class="text-center" style="font-family: Playfair Display, serif; color: #0e385d">Contact Us</h1>
          <div class="mt-10">
            <v-row>
              <v-col
                >{{ thing.text }} <v-text-field outlined></v-text-field>
              </v-col>
              <v-col
                >{{ thing.text2 }}
                <v-text-field outlined></v-text-field>
              </v-col>
            </v-row>
          </div>
          <p>{{ thing.text3 }}</p>
          <v-text-field outlined></v-text-field>
          <p>{{ thing.text4 }}</p>
          <v-textarea outlined height="10em"></v-textarea>
          <div class="text-center">
            <v-btn width="20em" color="#0596c8" class="white--text mb-5 mt-3">
              Submit
            </v-btn>
          </div>
        </v-container>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data: () => ({
    things: [
      {
        text: "First Name",
        text2: "Last Name",
        text3: "E-mail",
        text4: "Message",
      },
    ],
    links: [
      {
        text: "Contact Number",
        text1: "980100000 / 9843877154",
      },
      {
        text: "Email",
        text1: "shresthajeevan889@gmail.com  ",
      },
      {
        text: "Address",
        text1: "Kathmandu, Nepal 44600 Bagbazar ",
      },
    ],
  }),
};
</script>

<style></style>
