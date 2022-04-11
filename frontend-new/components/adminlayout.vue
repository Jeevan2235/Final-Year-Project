<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      dark
      app
      class="pink accent-4"
      v-if="$auth.loggedIn"
    >
      <v-row class="mt-1" justify="center">
        <v-icon size="130">mdi-account</v-icon>
      </v-row>
      <v-divider class="mt-3"></v-divider>
      <v-list flat class="mt-10">
        <v-list-item
          v-for="link in links"
          :key="link"
          router
          :to="link.route"
          active-class="border"
        >
          <v-list-item-action>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ link.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <template v-slot:append>
        <div class="pa-2">
          <v-btn block @click="logout"> Log out </v-btn>
        </div>
      </template>
    </v-navigation-drawer>
    <v-main>
      <Nuxt />
    </v-main>
  </v-app>
</template>

<script>
import Swal from "sweetalert2";
export default {
  data() {
    return {
      links: [
        { title: "Booked", icon: "mdi-view-dashboard", route: "/admin/booked" },
        {
          title: "Purchase",
          icon: "mdi-currency-usd",
          route: "/admin/purchase",
        },
        { title: "Flights", icon: "mdi-gavel", route: "/admin/flights" },
        { title: "Users", icon: "mdi-account-box", route: "/admin/users" },
        { title: "Ticket", icon: "mdi-ticket", route: "/admin/ticket" },
      ],
    };
  },
  methods: {
    logout() {
      Swal.fire({
        title: "Are you sure?",
        text: "You're about to be signed out",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, sign out!",
      }).then((result) => {
        if (result.value) {
          this.$auth.logout().then(() => {
            this.$router.push("/login");
          });
        }
      });
    },
  },
};
</script>

<style></style>
