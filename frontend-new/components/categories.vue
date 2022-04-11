<template>
  <div>
      
      <v-card width="23em" >
          <v-container>
          <v-card-title>Categories</v-card-title>
          <v-divider></v-divider>
          <div class="pa-2" v-for="link in links" :key="link">
          <p>{{link}}</p>
          <v-divider></v-divider>
    
        
          
          </div>
           </v-container>
      </v-card>
     
  </div>
</template>

<script>
export default {
     data: () => ({
    links: ["Airlines in Nepal","Bungee","Domestic Airlines", "News", "Things to do", "Travel Stories",  ],


  }),

}
</script>

<style>

</style>