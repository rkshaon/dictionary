<template>
    <div class="row mb-3">
        <div class="col-6">
            <label for="baseLanguage" class="form-label">Base</label>
            <select class="form-select" aria-label="Default select example" v-model="baseLanguage">
                <option v-for="language in languages" :key="language.id" :value="language.id">{{ language.name }}</option>
            </select>
        </div>
        <div class="col-6">
            <label for="secondaryLanguage" class="form-label">Secondary</label>
            <select class="form-select" aria-label="Default select example" v-model="secondaryLanguage">
                <option v-for="language in languages" :key="language.id" :value="language.id">{{ language.name }}</option>
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
            baseLanguage: '',
            secondaryLanguage: '',
        }
    },
    computed: {
        ...mapGetters(['getLanguages']),
        languages() {
            return this.getLanguages;
        },
    },
    mounted() {
        this.fetchLanguages();
    },
    watch: {
        getLanguages: {
            immediate: true,
            handler(languages) {
                if (languages.length > 0) {
                    this.baseLanguage = this.getLanguageIdByName('English');
                    this.secondaryLanguage = this.getLanguageIdByName('Bengali');
                }
            },
        },
    },
    methods: {
        fetchLanguages() {
            axios.get(`http://10.10.10.84:8000/configure-api/languages`)
            .then(response => {
                this.$store.commit('setLanguages', response.data);

            })
            .catch(error => {
                console.log('Error fetching languages: ', error);
            })
        },
        getLanguageIdByName(name) {
            if (this.languages) {
                const language = this.languages.find(language => language.name === name);
                return language ? language.id : '';
            }
            return '';
        },
    }
})
</script>