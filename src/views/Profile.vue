<template>
  <ion-page>
    <ion-content :fullscreen="true" class="ion-padding">

      <auth-options/>

    </ion-content>
  </ion-page>
</template>

<script>
import {IonPage, IonContent} from '@ionic/vue';
import AuthOptions from "../components/AuthOptions";

export default {
  name: 'Profile',
  components: {
    AuthOptions,
    IonContent,
    IonPage
  }
}
</script>