<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar slot="bottom">
        <ion-tab-button tab="feed" href="/tabs/feed">
          <ion-icon :icon="trendingUpOutline" />
          <ion-label>Trending</ion-label>
        </ion-tab-button>
          
        <ion-tab-button tab="add" href="/tabs/add">
          <ion-icon :icon="addCircleOutline" />
          <ion-label>New Post</ion-label>
        </ion-tab-button>
        
        <ion-tab-button tab="profile" href="/tabs/profile">
          <ion-icon :icon="personOutline"  />
          <ion-label>Profile</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script>
import { IonTabBar, IonTabButton, IonTabs, IonLabel, IonIcon, IonPage, IonRouterOutlet } from '@ionic/vue';
import { personOutline, addCircleOutline, trendingUpOutline } from 'ionicons/icons';

export default {
  name: 'Tabs',
  components: { IonLabel, IonTabs, IonTabBar, IonTabButton, IonIcon, IonPage, IonRouterOutlet },
  setup() {
    return {
      trendingUpOutline,
      addCircleOutline,
      personOutline,
    }
  }
}
</script>