<template>
  <ion-page>

    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button default-href="/tabs/profile"></ion-back-button>
        </ion-buttons>
        <ion-title>Login</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding ion-justify-content-center">
      <form class="ion-padding" @submit.prevent="submit">

        <ion-input clear-input placeholder="Email" type="email" autocomplete="email" inputmode="email"
                   required v-model="email"></ion-input>

        <ion-input clear-input placeholder="Password" type="password" autocomplete="password"
                   required v-model="password"></ion-input>

        <ion-button type="submit" color="primary" expand="block" class="ion-margin">
          Login
        </ion-button>
      </form>
    </ion-content>

  </ion-page>
</template>

<script>
import {
  IonPage,
  IonContent,
  IonButton,
  IonInput,
  IonHeader,
  IonToolbar,
  IonBackButton,
  IonButtons,
  IonTitle,
  toastController, alertController
} from '@ionic/vue';
import api from "../base/api";
import {default as axios} from "axios";

export default {
  name: "Login",
  mixins: [api],
  components: {
    IonContent,
    IonPage,
    IonButton,
    IonInput,
    IonHeader,
    IonToolbar,
    IonBackButton,
    IonButtons,
    IonTitle
  },
  data() {
    return {
      email: '',
      password: '',
    }
  },
  methods: {
    async submit() {
      const res = await axios.get(`${this.host}/login`, {
        params: {
          email: this.email,
          password: this.password
        }
      })

      if (!res.data.uid) {
        const alert = await alertController.create({
          message: res.data.err,
          buttons: ['OK']
        })
        return alert.present()
      }

      this.$store.commit('set_uid', res.data.uid)
      this.$store.commit('set_token', res.data.token)
      this.$router.back()
      const toast = await toastController
          .create({
            message: 'Logged in!',
            duration: 2000,
            color: 'primary'
          })
      toast.present();
    }
  }
}
</script>

<style scoped>
form {
  padding-top: 50%;
}
</style>