<template>
  <v-container>
    <h1
      class="text-center"
      style="font-family: Playfair Display, serif; color: #0e385d"
    >
      Recent Blog Articles
    </h1>
    <v-row class="mt-5">
      <v-col cols="12" md="4">
        <v-card
          img="pennsylvenia.jpg"
          class="d-flex flex-column justify-end"
          min-height="400"
          elevation="0"
          width="100%"
          to="/blogsingle9"
        >
          <v-card color="transparent" width="90%" tile elevation="0">
            <v-container class="ma-3">
              <p class="font-weight-black" style="color: #24cb83">
                PHOTOGRAPHY
              </p>
              <p class="white--text" style="font-size: 18px">PENNSYLVANIA</p>
              <p class="white--text">2021, January 1</p>
            </v-container>
          </v-card>
        </v-card>
      </v-col>
      <v-col cols="12" md="4">
        <v-card
          img="virginia.jpg"
          class="d-flex flex-column justify-end"
          min-height="400"
          elevation="0"
          width="100%"
          to="/blogsingle8"
        >
          <v-card color="transparent" width="90%" tile elevation="0">
            <v-container class="ma-3">
              <p class="font-weight-black" style="color: #24cb83">
                PHOTOGRAPHY
              </p>
              <p class="white--text" style="font-size: 18px">VIRGINIA</p>
              <p class="white--text">2021, January 1</p>
            </v-container>
          </v-card>
        </v-card>
      </v-col>
      <v-col cols="12" md="4">
        <v-card
          img="hawai.jpg"
          class="d-flex flex-column justify-end"
          min-height="400"
          elevation="0"
          width="100%"
          to="/blogsingle6"
        >
          <v-card color="transparent" width="90%" tile elevation="0">
            <v-container class="ma-3">
              <p class="font-weight-black" style="color: #24cb83">
                PHOTOGRAPHY
              </p>
              <p class="white--text" style="font-size: 18px">HAWAI</p>
              <p class="white--text">2021, January 1</p>
            </v-container>
          </v-card>
        </v-card>
      </v-col>
    </v-row>
    <div class="text-center mt-12">
      <v-btn class="white--text mb-10" height="3.5em" color="blue" to="/blog">
        View All Blogs
      </v-btn>
    </div>
  </v-container>
</template>

<script>
export default {};
</script>

<style></style>
