<template>
  <ion-page>
    <ion-header collapse="condense" class="ion-margin-bottom ion-padding-top">
      <ion-toolbar>
        <ion-title>New post</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true" class="ion-padding">

      <form v-if="uid" class="ion-padding" @submit.prevent="send">

        <ion-label position="stacked">Title</ion-label>
        <ion-input clear-input placeholder="Give your post a title" required v-model="title"></ion-input>

        <ion-label position="stacked" type="url">URL (optional)</ion-label>
        <ion-input clear-input placeholder="Link your article here" v-model="url"></ion-input>

        <ion-label position="stacked">Subtext (optional)</ion-label>
        <ion-textarea clear-input rows="5" v-model="subtext"
                      placeholder="Include #hashtags to help your post reach relevance"></ion-textarea>

        <ion-button type="submit" color="primary" expand="block" class="ion-margin">
          Submit
        </ion-button>
      </form>

      <auth-options v-else/>

    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonLabel,
  IonInput,
  IonButton,
  IonTextarea,
  loadingController
} from '@ionic/vue';
import api from "../base/api";
import AuthOptions from "../components/AuthOptions";
import {default as axios} from "axios";
import mixpanel from "mixpanel-browser";

export default {
  name: 'Add',
  mixins: [api],
  components: {
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonPage,
    IonLabel,
    IonInput,
    IonButton,
    IonTextarea,
    AuthOptions
  },
  data() {
    return {
      title: '',
      url: '',
      subtext: ''
    }
  },
  methods: {
    async send() {
      const loading = await loadingController
          .create({
            cssClass: 'my-custom-class',
            message: 'Sending...',
            duration: 2000,
          });
      await loading.present()

      let params = {title: this.title}

      if (this.url) params.url = this.url
      if (this.subtext) params.subtext = this.subtext

      const res = await axios.get(`${this.host}/post/new`, {
        params,
        headers: this.headers
      })

      const post = res.data.post
      console.log({post})

      mixpanel.track('Post added', {
        distinct_id: this.$store.state.uid
      })

      this.$router.replace('/tabs/feed')

    },
  }
}
</script>