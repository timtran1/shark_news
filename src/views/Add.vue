<template>
  <ion-page>
    <ion-header collapse="condense" class="ion-margin-bottom">
      <ion-toolbar>
        <ion-title>New post</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true" class="ion-padding">

      <auth-options v-if="!loading && !uid"/>

      <p v-if="loading">Loading...</p>

      <form class="ion-padding" v-if="uid">

        <ion-label position="stacked">Title</ion-label>
        <ion-input clear-input placeholder="Give your post a title" required></ion-input>

        <ion-label position="stacked" type="url">URL (optional)</ion-label>
        <ion-input clear-input placeholder="Link your article here"></ion-input>

        <ion-label position="stacked">Subtext (optional)</ion-label>
        <ion-input clear-input></ion-input>

        <ion-button type="submit" color="primary" expand="block" class="ion-margin">
          Submit
        </ion-button>
      </form>


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
  IonButton
} from '@ionic/vue';
import {Storage} from "@capacitor/storage";
import AuthOptions from "../components/AuthOptions";

export default {
  name: 'Add',
  components: {
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonPage,
    IonLabel,
    IonInput,
    IonButton,
    AuthOptions
  },
  created() {
    Storage.get({key: 'uid'})
        .then(uid => {
          console.log({uid})
          this.loading = false
          this.uid = uid.value
        })
  },
  data() {
    return {
      uid: null,
      loading: true
    }
  }
}
</script>