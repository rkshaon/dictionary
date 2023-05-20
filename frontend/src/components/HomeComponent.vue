<template>
    <div class="row mt-3">
        <div class="col-6">
            <SearchBarComponent />
        </div>
        <div class="col-6">add</div>
    </div>
</template>

<script>
import SearchBarComponent from './SearchBarComponent.vue';

export default {
    name: 'HomeComponent',
    components: { SearchBarComponent },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
