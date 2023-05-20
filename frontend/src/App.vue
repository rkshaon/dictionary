<template>
  <NavBarComponent />
  <div class="container">
    <HomeComponent />
  </div>
</template>

<script>
import NavBarComponent from "./components/NavBarComponent.vue";
import HomeComponent from "./components/HomeComponent.vue";

export default {
  name: 'App',
  components: {
    HomeComponent,
    NavBarComponent
  }
}
</script>

<style>
/* background */
.bg-dark-theme1 {
  background-color: rgb(95, 93, 93);
}
</style>
