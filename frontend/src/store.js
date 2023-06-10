import { createStore } from 'vuex';

const store = createStore({
  state: {
    languages: [] // Initial state for languages
  },
  mutations: {
    setLanguages(state, languages) {
      state.languages = languages;
    }
  },
  actions: {
    fetchLanguages() {
      // Replace with your API call to fetch languages
      // Example: axios.get('http://api.example.com/languages')
      // Then, call commit('setLanguages', response.data) to update the state
      // You can also use async/await syntax if needed
    }
  },
  getters: {
    getLanguages(state) {
      return state.languages;
    }
  }
});

export default store;
