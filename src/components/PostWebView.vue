<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <iframe :src="$props.post.url" frameborder="0"></iframe>

      <ion-row class="user-name-row">
        <ion-col size="4" class="ion-justify-content-center" color="light">
          <span>  <ion-icon :icon="personCircleOutline" color="light"/>
            user56545345</span>
        </ion-col>
        <ion-col size="4">
        </ion-col>
        <ion-col size="4">
        </ion-col>
      </ion-row>

      <ion-row>
        <ion-col size="4">
          <ion-button fill="clear" size="small" expand="block">
            <ion-icon :icon="shareOutline" slot="start"/>
            Share
          </ion-button>
        </ion-col>
        <ion-col size="4">
          <ion-button fill="clear" size="small" expand="block">
            <ion-icon :icon="chatboxEllipsesOutline" slot="start"/>
            24
          </ion-button>
        </ion-col>
        <ion-col size="4">
          <ion-button fill="clear" size="small" expand="block">
            <ion-icon :icon="fishOutline" slot="start"/>
            127
          </ion-button>
        </ion-col>
      </ion-row>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonContent,
  IonRow,
  IonCol,
  IonIcon,
  IonButton
} from '@ionic/vue';

export default {
  name: "PostWebView",
    props: {
    post: Object
  },
  components: {
    IonContent,
    IonPage,
    IonRow,
    IonCol,
    IonIcon,
    IonButton
  },
}
</script>

<style scoped>

</style>