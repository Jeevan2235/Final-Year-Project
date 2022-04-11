<template>
  <div>
    <v-card
      v-for="link in links"
      :key="link"
      to="/blogsingle2"
      class="d-flex flex-column justify-end"
      min-height="400"
      elevation="0"
      width="100%"
      :img="link.img"
    >
      <v-card color="transparent" width="90%" tile elevation="0">
        <v-container class="ma-3">
          <p class="font-weight-black" style="color: #24cb83">
            {{ link.txt }}
          </p>
          <p class="white--text" style="font-size: 18px">
            {{ link.text }}
          </p>
          <p class="white--text">{{ link.date }}</p>
        </v-container>
      </v-card>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    links: [
      {
        img: "boston.jpg",
        txt: "PHOTOGRAPHY",
        text: "BOSTON",
        date: "2021, January 1",
      },
    ],
  }),
};
</script>

<style></style>
