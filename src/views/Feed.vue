<template>
  <ion-page>
    <ion-content :fullscreen="true">

      <div v-for="post in posts" :key="post.id" @click="open_post(post.id)" class="ion-padding post-container">
        <h4>{{ post.title }}</h4>
        <ion-img class="post-img" v-if="post.image" :src="post.image"/>
        <p>{{ post.subtext }}</p>

        <ion-row class="user-name-row">
          <ion-col size="4" class="ion-justify-content-center" color="light">
          <span>
            <ion-icon :icon="personCircleOutline" color="light"/>
            user56545345
          </span>
          </ion-col>
          <ion-col size="4">
          </ion-col>
          <ion-col size="4">
          </ion-col>
        </ion-row>

        <post-summary :post="post"/>

        <div class="bottom-divider"></div>
      </div>

    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonContent,
  IonImg,
  IonRow,
  IonCol,
  IonIcon,
} from '@ionic/vue';
import PostSummary from "../components/PostSummary";
import api from "../base/api";

const axios = require("axios").default

export default {
  name: 'Feed',
  mixins: [api],
  components: {
    IonContent,
    IonPage,
    IonImg,
    IonRow,
    IonCol,
    IonIcon,
    PostSummary
  },
  data() {
    return {
      posts: []
    }
  },
  created() {
    this.fetch_feed()
  },
  methods: {
    open_post(id) {
      this.$router.push(`/post/view/${id}`)
    },

    async fetch_feed() {
      let token = this.$store.state.token
      let res = await axios.get(`${this.host}/feed`, {
        headers: {'Authorization': `Bearer ${token}`}
      })
      this.posts = res.data.posts
      return true
    }
  }
}
</script>

<style scoped>
.post-img {
  border-radius: 10px !important;
  overflow: hidden;
}

.bottom-divider {
  border-bottom: 1px solid lightgrey;
  padding-bottom: 16px;
}

.post-container {
  padding-bottom: 0;
}

ion-col {
  padding: 0 !important;
}

ion-button {
  margin: 0 !important;
}

p {
  margin-bottom: 0;
}

span {
  color: #8c8c8c;
  font-size: 0.8rem;
}

.user-name-row {
  padding-top: 5px;
  padding-bottom: 5px;
}
</style>