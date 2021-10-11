<template>
  <ion-page>
    <ion-header v-if="$props.show_header" collapse="condense" class="ion-margin-bottom ion-padding-top">
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button default-href="/tabs/feed"></ion-back-button>
        </ion-buttons>
        <ion-title>Signup or Login</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true" class="ion-padding ion-justify-content-center">

      <div class="auth-options ion-padding ion-justify-content-center">

        <ion-row>
          <ion-col size="12">
            <ion-button color="primary" expand="block" router-link="/signup">
              <ion-icon :icon="personAddOutline" slot="start"/>
              Create an account
            </ion-button>
          </ion-col>
        </ion-row>

        <ion-row class="ion-text-center">
          <ion-col size="12">
            <small class="ion-text-center">Or</small>
          </ion-col>
        </ion-row>

        <ion-row>
          <ion-col size="12">
            <ion-button color="light" expand="block" router-link="/login">
              <ion-icon :icon="logInOutline" slot="start"/>
              Login
            </ion-button>
          </ion-col>
        </ion-row>
      </div>


    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonContent,
  IonButton,
  IonRow,
  IonIcon,
  IonCol,
  IonHeader,
  IonToolbar,
  IonBackButton,
  IonButtons,
  IonTitle
} from '@ionic/vue';
import {
  // mailOutline,
  // logoGoogle,
  logInOutline,
  personAddOutline
} from 'ionicons/icons';
import api from "../base/api";


export default {
  name: "AuthOptions",
  mixins: [api],
  components: {
    IonContent,
    IonPage,
    IonButton,
    IonRow,
    IonIcon,
    IonCol,
    IonHeader,
    IonToolbar,
    IonBackButton,
    IonButtons,
    IonTitle
  },
  props: {
    show_header: Boolean,
    return_after_auth: Boolean
  },
  data() {
    return {
      logInOutline,
      personAddOutline
    }
  },
  watch: {
    uid(new_uid) {
      if (new_uid && this.$props.return_after_auth) {
        console.log('return')
        this.$router.back()
      }
    }
  }
}
</script>

<style scoped>
.auth-options {
  display: flex;
  flex-direction: column;
  padding-top: 40%;

}
</style>