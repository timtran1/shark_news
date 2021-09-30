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
      <form class="ion-padding">

        <ion-input clear-input placeholder="Email" type="email" required></ion-input>

        <ion-input clear-input placeholder="Password" type="password" required></ion-input>

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
  IonTitle
} from '@ionic/vue';

export default {
  name: "Login",
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
}
</script>

<style scoped>
form {
  padding-top: 50%;
}
</style>