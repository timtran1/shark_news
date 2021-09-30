<template>
  <ion-page>
    <ion-content :fullscreen="true" class="ion-padding">

      <auth-options v-if="!loading && !uid"/>

      <p v-if="loading">Loading...</p>

      <p v-if="uid">Logged In!</p>

      <ion-button v-if="uid" color="danger" fill="outline" @click="logout">Log out</ion-button>

    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonContent,
  IonButton
} from '@ionic/vue';
import AuthOptions from "../components/AuthOptions";
import {Storage} from '@capacitor/storage';

export default {
  name: 'Profile',
  components: {
    AuthOptions,
    IonContent,
    IonPage,
    IonButton
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
  },
  methods: {
    logout() {
      Storage.clear()
      this.$router.replace('/tabs/feed')
    }
  }
}
</script>