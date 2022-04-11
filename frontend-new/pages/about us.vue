<template>
  <div>
    <v-img src="aboutus.jpg"></v-img>
    <div>
      <v-container>
        <h1
          class="text-center"
          style="
            font-size: 40px;
            font-family: Playfair Display, serif;
            color: #0596c8;
          "
        >
          We are truly committed to making your travel experience as
          straightforward and enjoyable as possible!
        </h1>
      </v-container>
    </div>
    <div>
      <v-container>
        <p style="text-align: justify; font-size: 18px; line-height: 2">
          JeevanFlights was established with the sole purpose of helping
          travelers with seamless online ticketing and booking flights all over
          Nepal. We aim to offer the best deals, services along with
          cutting-edge technology, and dedicated round-the-clock customer
          support. We offer flight information in a well-integrated and
          easy-to-use design for online booking and ticketing.
          <span class="font-weight-bold"
            >Travelers have the facility to compare and choose their preferred
            tickets out of numerous options. JeevanFlights is one of the only
            few online ticketing portals in Nepal which provides the cheapest
            flight tickets from six airlines of Nepal.</span
          >
          The prime target for us now as an award-winning and one of the most
          recognized travel agencies in Nepal is to show our appreciation to our
          valued clients and gain their utmost satisfaction.
        </p>
        <p style="text-align: justify; font-size: 18px; line-height: 2">
          <span class="font-weight-bold"
            >With dedicated 24/7 Customer Support and the best Travel Crisis
            Management, JeevanFlights is there for the travelers whenever and
            wherever.</span
          >
          Be Smart, Book Smart: Best Place to book travel services in Nepal
          Having been awarded a number of awards throughout the years for our
          unrivaled traveling solutions, we still strive to help travelers with
          seamless online ticketing and booking of flights all over Nepal. We
          offer a wide variety of airline tickets and cheap flights, tour
          packages, accommodations, car rentals, and many more. All of the
          bookings will only be done under the traveler’s supervision and their
          preferences only. We aim to be a helping hand for travelers to get the
          best out of their long-awaited vacation. JeevanFlights is dedicated to
          making travel hassle-free.
          <span class="font-weight-bold"
            >JeevanFlights tends to be one of the best Travel Crisis Management
            companies as it provides the best alternatives to the travelers if
            the previous plan doesn’t go as well as intended.</span
          >
        </p>
      </v-container>
    </div>
    <v-divider></v-divider>
    <div class="mt-5">
      <v-container>
        <h1
          class="text-center"
          style="
            font-size: 40px;
            font-family: Playfair Display, serif;
            color: #0596c8;
          "
        >
          Why Choose Us?
        </h1>
        <v-row>
          <v-col v-for="link in links" :key="link" cols="12" md="4">
            <v-card class="mb-16 mt-10" elevation="0">
              <v-row justify="center">
                <v-icon class="mt-5" color="#0596c8" size="80">{{
                  link.icon
                }}</v-icon>
              </v-row>
              <v-row justify="center">
                <v-card-title>{{ link.title }}</v-card-title>
              </v-row>
              <v-card-text style="font-size: 16px">{{ link.text }}</v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    links: [
      {
        icon: "mdi-seal",
        title: "Award-Winning  Service",
        text: "Travel with confidence, knowing that we are available 24 hours a day, seven days a week.",
      },
      {
        icon: "mdi-earth",
        title: "Global Coverage",
        text: "More than 1,200,000 hotels in over 200 countries and regions, as well as flights to over 5,000 locations",
      },
      {
        icon: "mdi-currency-usd",
        title: "Competitive Pricing",
        text: "JeevanFlights can save you more money because it has 500+ suppliers and the purchasing power of 300 million members.",
      },
    ],
  }),
};
</script>

<style></style>
