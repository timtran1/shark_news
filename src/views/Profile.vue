<template>
  <ion-page>
    <ion-content :fullscreen="true" class="ion-padding">

      <div v-if="uid">
        Logged In!
        <ion-button color="danger" fill="outline" @click="logout">Log out</ion-button>
      </div>

      <auth-options v-else/>

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
import init_user from "../store/init_user";
import api from "../base/api";

export default {
  name: 'Profile',
  mixins: [api],
  components: {
    AuthOptions,
    IonContent,
    IonPage,
    IonButton
  },
  methods: {
    async logout() {
      const token = await init_user()
      this.$store.commit('set_token', token)
      this.$store.commit('set_uid', 0)
      this.$router.replace('/tabs/feed')
    }
  }
}
</script>