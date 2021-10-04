<template>
  <ion-page>

    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button default-href="/tabs/profile"></ion-back-button>
        </ion-buttons>
        <ion-title>Signup</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding ion-justify-content-center ion-align-items-center">
      <form class="ion-padding" @submit.prevent="submit">

        <ion-input clear-input placeholder="Choose your username" required v-model="name"></ion-input>

        <ion-input clear-input placeholder="Email" type="email" autocomplete="email" inputmode="email"
                   required v-model="email"></ion-input>

        <ion-input clear-input placeholder="Password" type="password" minlength="6" required
                   v-model="password"></ion-input>

        <ion-input clear-input placeholder="Confirm password" type="password" minlength="6" required
                   v-model="confirm_password"></ion-input>

        <ion-button type="submit" color="primary" expand="block" class="ion-margin">
          Signup
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
  alertController
} from '@ionic/vue';
import api from "../base/api";

const axios = require("axios").default

export default {
  name: "SignUp",
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
      name: '',
      email: '',
      password: '',
      confirm_password: '',
    }
  },
  methods: {
    async submit() {
      if (this.password !== this.confirm_password) {
        let alert = await alertController.create({
          header: 'Passwords do not match',
          message: 'Please re-confirm your password',
          buttons: ['OK']
        })
        await alert.present()
      }

      const token = this.$store.state.token
      const headers = {Authorization: `Bearer ${token}`}

      const res = await axios.get(`${this.host}/signup`, {
        params: {
          name: this.name,
          email: this.email,
          password: this.password
        },
        headers
      })

      this.$store.commit('set_uid', res.data.uid)
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