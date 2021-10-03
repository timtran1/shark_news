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
      <iframe v-if="post" :src="post.url" frameborder="0"></iframe>

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
} from '@ionic/vue';
import {shareOutline, chatboxEllipsesOutline, fishOutline, personCircleOutline} from 'ionicons/icons';
import PostSummary from "../components/PostSummary";

const axios = require("axios").default

export default {
  name: "PostWebView",
  components: {
    IonContent,
    IonPage,
    IonCard,
    IonHeader,
    IonToolbar,
    IonBackButton,
    IonButtons,
    IonTitle,
    PostSummary
  },
  data() {
    return {
      shareOutline,
      chatboxEllipsesOutline,
      fishOutline,
      personCircleOutline,
      post: {}
    }
  },
  created() {
    const post_id = this.$route.params.id
    let host = ''

    if (process.env.NODE_ENV === 'development') {
      host = 'http://localhost'
    }

    axios.get(`${host}/post/summary/${post_id}`)
        .then(res => {
          this.post = res.data.post
        })
  },
}
</script>

<style scoped>
iframe {
  height: 94%;
  width: 100%;
}


</style>