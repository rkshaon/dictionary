<template>
    <div class="row mb-3">
        <div class="col-6">
            <label for="language" class="form-label">Base</label>
            <select class="form-select" aria-label="Default select example">
                <option selected>English</option>
                <option value="1">One</option>
            </select>
        </div>
        <div class="col-6">
            <label for="language" class="form-label">Secondary</label>
            <select class="form-select" aria-label="Default select example">
                <option selected>Bengali</option>
                <option value="1">One</option>
            </select>
        </div>
    </div>
    <div class="mb-3">
        <input type="email" class="form-control" aria-describedby="emailHelp" placeholder="Type your word here...">
        <div id="emailHelp" class="form-text">When you will stop typing the result will be shown in below.</div>
    </div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default ({
    name: 'SearchBarComponent',
    data() {
        return {
            languages: [],
        }
    },
    computed: {
        ...mapGetters(['getLanguages'])
    },
    mounted() {
        this.fetchLanguages();
    },
    methods: {
        fetchLanguages() {
            axios.get(`http://10.10.10.84:8000/configure-api/languages`)
                .then(response => {
                    // this.languages = response.data;
                    // this.$store.commit('setLanguages', response.data);
                    commit('setLanguages', response.data);
                    console.log('Response data: ', response.data);
                })
                .catch(error => {
                    console.log('Error fetching languages: ', error);
                })
        }
    }
})
</script>