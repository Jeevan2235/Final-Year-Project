<template>
  <AdminLayout v-if="$auth.user && $auth.user.role === 'STAFF'" />
  <UserLayout v-else />
</template>

<script>
import AdminLayout from "@/components/adminlayout";
import UserLayout from "@/components/userlayout";
export default {
  components: {
    UserLayout,
    AdminLayout,
  },
};
</script>

<style scoped></style>
