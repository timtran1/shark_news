<template>
  <ion-page>
    <ion-content :fullscreen="true" class="ion-padding  ion-justify-content-center">

      <div class="ion-padding  ion-justify-content-center">

        <ion-row>
          <ion-col size="12">
            <ion-button color="danger" expand="block">
              <ion-icon :icon="logoGoogle" slot="start"/>
              Continue with Google
            </ion-button>
          </ion-col>
        </ion-row>

        <ion-row>
          <ion-col size="12">
            <ion-button color="primary" expand="block">
              <ion-icon :icon="mailOutline" slot="start"/>
              Continue with email
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
  IonCol
} from '@ionic/vue';
import {mailOutline, logoGoogle} from 'ionicons/icons';

export default {
  name: "AuthOptions",
  components: {
    IonContent,
    IonPage,
    IonButton,
    IonRow,
    IonIcon,
    IonCol
  },
  data() {
    return {
      mailOutline,
      logoGoogle
    }
  }
}
</script>

<style scoped>
div {
  display: flex;
  flex-direction: column;
  padding-top: 40%;

}
</style>