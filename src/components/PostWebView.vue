<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button default-href="/tabs/feed"></ion-back-button>
        </ion-buttons>
        <ion-title v-if="post">{{ post.title }}</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true" class="">
      <ion-progress-bar v-if="loading" type="indeterminate"></ion-progress-bar>

      <iframe v-if="post" :src="post.url" frameborder="0" @load="loaded"></iframe>

      <p v-if="!post">Loading...</p>

      <ion-card v-if="post" class="ion-no-margin">
        <post-summary :post="post"/>
      </ion-card>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonContent,
  IonCard,
  IonHeader,
  IonToolbar,
  IonBackButton,
  IonButtons,
  IonTitle,
  IonProgressBar
} from '@ionic/vue';
import {shareOutline, chatboxEllipsesOutline, fishOutline, personCircleOutline} from 'ionicons/icons';
import PostSummary from "../components/PostSummary";
import mixpanel from "mixpanel-browser";
import api from "../base/api";

const axios = require("axios").default

export default {
  name: "PostWebView",
  mixins: [api],
  components: {
    IonContent,
    IonPage,
    IonCard,
    IonHeader,
    IonToolbar,
    IonBackButton,
    IonButtons,
    IonTitle,
    PostSummary,
    IonProgressBar
  },
  data() {
    return {
      shareOutline,
      chatboxEllipsesOutline,
      fishOutline,
      personCircleOutline,
      post: {},
      loading: true
    }
  },
  created() {
    this.fetch_post()
  },
  methods: {
    async fetch_post() {
      const post_id = this.$route.params.id
      const res = await axios.get(`${this.host}/post/summary/${post_id}`)
      this.post = res.data.post

      mixpanel.track('Post view', {
        distinct_id: this.$store.state.uid
      })
    },
    async loaded() {
      console.log('loaded')
      await this.sleep(3000)
      this.loading = false
    }
  }
}
</script>

<style scoped>
iframe {
  height: 93%;
  width: 100%;
}


</style>