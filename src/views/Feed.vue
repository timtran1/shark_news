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
import {shareOutline, chatboxEllipsesOutline, fishOutline} from 'ionicons/icons';

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
      fishOutline
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
</style>