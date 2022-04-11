<template>
  <div>
    <hello />

    <div class="mt-10">
      <deals />
    </div>
    <maps />

    <div class="mt-10">
      <blog />
    </div>
  </div>
</template>

<script>
import Deals from "~/components/deals.vue";
import Maps from "~/components/maps.vue";

export default {
  components: { Deals, Maps },
};
</script>

<style></style>
