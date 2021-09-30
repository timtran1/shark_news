<template>
  <ion-page>
    <ion-content :fullscreen="true" class="ion-padding">

      <auth-options v-if="!loading && !uid"/>

      <p v-if="loading">Loading...</p>

       <p v-if="uid">Logged In!</p>

    </ion-content>
  </ion-page>
</template>

<script>
import {IonPage, IonContent} from '@ionic/vue';
import AuthOptions from "../components/AuthOptions";
import {Storage} from '@capacitor/storage';

export default {
  name: 'Profile',
  components: {
    AuthOptions,
    IonContent,
    IonPage
  },
  created() {
    Storage.get({key: 'uid'})
        .then(uid => {
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