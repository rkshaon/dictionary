<template>
  <div class="container">
    <HomeComponent />
  </div>
</template>

<script>
import HomeComponent from "./components/HomeComponent.vue";

export default {
  name: 'App',
  components: {
    HomeComponent
  }
}
</script>

<style>
/* background */
.bg-dark-theme1 {
  background-color: rgb(95, 93, 93);
}
</style>
