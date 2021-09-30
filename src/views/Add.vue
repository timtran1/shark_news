<template>
  <ion-page>
    <ion-content :fullscreen="true" class="ion-padding">
      <ion-header collapse="condense" class="ion-margin-bottom">
        <ion-toolbar>
          <ion-title>New post</ion-title>
        </ion-toolbar>
      </ion-header>


      <form class="ion-padding">

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
    IonButton
  }
}
</script>