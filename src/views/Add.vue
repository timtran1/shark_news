<template>
  <ion-page>
    <ion-header collapse="condense" class="ion-margin-bottom">
      <ion-toolbar>
        <ion-title>New post</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true" class="ion-padding">

      <form v-if="uid" class="ion-padding">

        <ion-label position="stacked">Title</ion-label>
        <ion-input clear-input placeholder="Give your post a title" required></ion-input>

        <ion-label position="stacked" type="url">URL (optional)</ion-label>
        <ion-input clear-input placeholder="Link your article here"></ion-input>

        <ion-label position="stacked">Subtext (optional)</ion-label>
        <ion-textarea clear-input placeholder="Include #hashtags to help your post reach relevance"></ion-textarea>

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
    IonTextarea
} from '@ionic/vue';
import api from "../base/api";
import AuthOptions from "../components/AuthOptions";

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
}
</script>