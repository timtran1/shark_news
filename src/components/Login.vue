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
} from '@ionic/vue';
import api from "../base/api";
import {Storage} from "@capacitor/storage";
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
    async init_new_user() {
      let res = await axios.get(`${this.host}/new_user`)
      await Storage.set({
        key: 'token',
        value: res.data.token,
      })
      return true
    },
    async submit() {
      let token = await Storage.get({key: 'token'})
      const headers = {Authorization: `Bearer ${token.value}`}

      if (!token.value) {
        await this.init_new_user()
        token = await Storage.get({key: 'token'})
      }

      const res = await axios.get(`${this.host}/login`, {
        params: {
          email: this.email,
          password: this.password
        },
        headers
      })

      await Storage.set({
        key: 'uid',
        value: res.data.uid
      })

      this.$router.back()
    }
  }
}
</script>

<style scoped>
form {
  padding-top: 50%;
}
</style>