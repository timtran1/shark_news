<template>
  <ion-page>
    <!--    <ion-header>-->
    <!--      <ion-toolbar>-->
    <!--&lt;!&ndash;        <ion-title>Feed</ion-title>&ndash;&gt;-->
    <!--      </ion-toolbar>-->
    <!--    </ion-header>-->
    <ion-content :fullscreen="true">
      <!--      <ion-header collapse="condense">-->
      <!--        <ion-toolbar>-->
      <!--&lt;!&ndash;          <ion-title size="large">Feed</ion-title>&ndash;&gt;-->
      <!--        </ion-toolbar>-->
      <!--      </ion-header>-->

      <div class="ion-padding post-container">
        <h4>US, Pakistan face each other again on Afghanistan threats</h4>
        <ion-img class="post-img"
                 src="https://storage.googleapis.com/afs-prod/media/75df45af32054561acff1ec13a32319b/1000.jpeg"/>
        <p>The Taliban’s takeover of Kabul has deepened the mutual distrust between the U.S. and Pakistan, two putative
          allies who have tangled over Afghanistan. But both sides still need each other.</p>
        <ion-row class="user-name-row">
          <!--          <ion-button fill="clear" size="small" color="secondary">-->
          <ion-col size="4" class="ion-justify-content-center" color="light">
          <span>  <ion-icon :icon="personCircleOutline"  color="light"/>
            user565</span>
          </ion-col>
          <ion-col size="4">
          </ion-col>
          <ion-col size="4">
          </ion-col>
          <!--          </ion-button>-->
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

        <div class="bottom-divider"></div>
      </div>
      <div class="ion-padding post-container">
        <h4>US, Pakistan face each other again on Afghanistan threats</h4>
        <ion-img class="post-img"
                 src="https://storage.googleapis.com/afs-prod/media/75df45af32054561acff1ec13a32319b/1000.jpeg"/>
        <p>The Taliban’s takeover of Kabul has deepened the mutual distrust between the U.S. and Pakistan, two putative
          allies who have tangled over Afghanistan. But both sides still need each other.</p>
        <ion-row>
          <ion-col>
            <ion-button expand="full" fill="clear" size="small">
              <ion-icon :icon="shareOutline" slot="start"/>
              Share
            </ion-button>
          </ion-col>
          <ion-col>
            <ion-button expand="full" fill="clear" size="small">
              <ion-icon :icon="chatboxEllipsesOutline" slot="start"/>
              24
            </ion-button>
          </ion-col>
          <ion-col>
            <ion-button expand="full" fill="clear" size="small">
              <ion-icon :icon="fishOutline" slot="start"/>
              127
            </ion-button>
          </ion-col>
        </ion-row>

        <div class="bottom-divider"></div>
      </div>

      <div class="ion-padding post-container">
        <h4>US, Pakistan face each other again on Afghanistan threats</h4>
        <ion-img class="post-img"
                 src="https://storage.googleapis.com/afs-prod/media/75df45af32054561acff1ec13a32319b/1000.jpeg"/>
        <p>The Taliban’s takeover of Kabul has deepened the mutual distrust between the U.S. and Pakistan, two putative
          allies who have tangled over Afghanistan. But both sides still need each other.</p>
        <ion-row>
          <ion-col>
            <ion-button expand="full" fill="clear" size="small">
              <ion-icon :icon="shareOutline" slot="start"/>
              Share
            </ion-button>
          </ion-col>
          <ion-col>
            <ion-button expand="full" fill="clear" size="small">
              <ion-icon :icon="chatboxEllipsesOutline" slot="start"/>
              24
            </ion-button>
          </ion-col>
          <ion-col>
            <ion-button expand="full" fill="clear" size="small">
              <ion-icon :icon="fishOutline" slot="start"/>
              127
            </ion-button>
          </ion-col>
        </ion-row>

        <div class="bottom-divider"></div>
      </div>

    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonPage,
  // IonHeader,
  // IonToolbar,
  // IonTitle,
  IonContent,
  IonImg,
  IonRow,
  IonCol,
  IonIcon,
  IonButton
} from '@ionic/vue';
import {shareOutline, chatboxEllipsesOutline, fishOutline, personCircleOutline} from 'ionicons/icons';

export default {
  name: 'Feed',
  components: {
    // ExploreContainer,
    // IonHeader,
    // IonToolbar,
    // IonTitle,
    IonContent,
    IonPage,
    IonImg,
    IonRow,
    IonCol,
    IonIcon,
    IonButton
  },
  data() {
    return {
      shareOutline,
      chatboxEllipsesOutline,
      fishOutline,
      personCircleOutline
    }
  }
}
</script>

<style scoped>
.post-img {
  border-radius: 10px !important;
  overflow: hidden;
}

.bottom-divider {
  border-bottom: 1px solid lightgrey;
  padding-bottom: 16px;
}

.post-container {
  padding-bottom: 0;
}

ion-col {
  padding: 0 !important;
}

ion-button {
  margin: 0 !important;
}

p {
  margin-bottom: 0;
}

span {
  color: #8c8c8c;
  font-size: 0.8rem;
}

.user-name-row {
  padding-top: 5px;
  padding-bottom: 5px;
}
</style>