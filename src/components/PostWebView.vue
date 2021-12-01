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

      <div class="iframe-wrapper" :style="{
        backgroundImage:`url(${require('@/assets/loading.svg')})`,
        backgroundPosition: 'center center',
        backgroundRepeat: 'no-repeat'
      }">
        <iframe v-if="post" :src="post.url" frameborder="0"></iframe>
      </div>

      <p v-if="!post">Loading...</p>

      <ion-card v-if="post" class="post-summary ion-no-margin">
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
} from '@ionic/vue';
import {shareOutline, chatboxEllipsesOutline, fishOutline, personCircleOutline} from 'ionicons/icons';
import PostSummary from "../components/PostSummary";
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
    },
  }
}
</script>

<style scoped>
.iframe-wrapper {
  width: 100%;
  height: 100%;
}

iframe {
  width: 100%;
  height: 100%;
}

.post-summary {
  position: fixed;
  bottom: 1rem;
  left: 1%;
  width: 98%;
}

</style>