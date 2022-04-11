<template>
  <div>
    <v-card tile elevation="0">
      <v-container>
        <v-row justify="center" class="mt-16">
          <h1>Famous Blog Articles About Places in United States</h1>
        </v-row>

        <v-row>
          <v-col cols="12" md="4">
            <blog1 />
          </v-col>
          <v-col cols="12" md="4">
            <blog2 />
          </v-col>
          <v-col cols="12" md="4">
            <blog-3 />
          </v-col>
          <v-col cols="12" md="4">
            <blog-4 />
          </v-col>
          <v-col cols="12" md="4">
            <blog-5 />
          </v-col>
          <v-col cols="12" md="4">
            <blog-6 />
          </v-col>
          <v-col cols="12" md="4">
            <blog-7 />
          </v-col>
          <v-col cols="12" md="4">
            <blog-8 />
          </v-col>
          <v-col cols="12" md="4">
            <blog-9 />
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </div>
</template>

<script>
import blog1 from "../components/blog1.vue";
import Blog2 from "../components/blog2.vue";
import Blog3 from "../components/blog3.vue";
import Blog4 from "../components/blog4.vue";
import Blog5 from "../components/blog5.vue";
import Blog6 from "../components/blog6.vue";
import Blog8 from "../components/blog8.vue";
import Blog9 from "../components/blog9.vue";
export default {
  components: { blog1, Blog2, Blog4, Blog3, Blog5, Blog6, Blog8, Blog9 },
};
</script>

<style></style>
