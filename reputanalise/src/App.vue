<template>
  <!-- <h1>ReputAnalysis</h1> -->
  <div class="search">
    <input type="text" class="search-field" placeholder="Insira o tweet coletado..." v-model="tweet">
    <div class="search-button-wrapper">
      <button class="search-button" @click="getSentiment">
        <vue-feather type="search" class="search-icon"></vue-feather>
      </button>
    </div>
  </div>
  <div class="sentiment-analysis" :class="sentiment_class" v-if="sentiment_score != ''">
    <p class="result">
      {{sentiment}}
    </p>
    <p class="result-score">
      Score: {{sentiment_score}}
    </p>
  </div>
</template>

<script>
import VueFeather from 'vue-feather';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    VueFeather
  },
  data() {
    return {
      sentiment_available: false,
      sentiment: "",
      sentiment_score: "",
      tweet: "",
      sentiment_class: ""
    }
  },
  methods: {
    async getSentiment() {
      var json = {
        "tweet" : this.tweet
      };
      var url = "http://localhost:8000/predict";
      const info = await axios.post(url, json);
      this.sentiment = info.data.sentiment;
      this.sentiment_score = info.data.confidence

      switch (info.data.sentiment) {
        case "Negativo":
          this.sentiment_class = "sentiment-analysis--negative"
          break;
          case "Neutro":
          this.sentiment_class = "sentiment-analysis--neutral"
          break;
          case "Positivo":
          this.sentiment_class = "sentiment-analysis--positive"
          break;
        default:
          break;
      }
    }
  }
}
</script>