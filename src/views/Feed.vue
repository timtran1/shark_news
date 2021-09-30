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

      <div v-for="post in posts" :key="post.url" class="ion-padding post-container">
        <h4>{{ post.title }}</h4>
        <ion-img class="post-img" :src="post.image"/>
        <p>{{ post.subtext }}</p>

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
              {{ post.comment_count }}
            </ion-button>
          </ion-col>
          <ion-col size="4">
            <ion-button fill="clear" size="small" expand="block">
              <ion-icon :icon="fishOutline" slot="start"/>
              {{ post.likes }}
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
import {Storage} from '@capacitor/storage';

const axios = require("axios").default

export default {
  name: 'Feed',
  components: {
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
      personCircleOutline,
      posts: [
        // {
        //   title: 'Panel debates Dems’ $3.5T bill, crunch time for Biden agenda',
        //   subtext: 'Democrats pushed a $3.5 trillion, 10-year bill strengthening social safety net and climate programs toward House Budget Committee approval Saturday, while party leaders hunted behind the scenes for compromises to resolve internal divisions and, they hoped, allow the sprawling package’s eventual passage by Congress.',
        //   image: 'https://storage.googleapis.com/afs-prod/media/d6f377b4c81f4564bc81e0e5c39dd8d7/1000.jpeg',
        //   url: 'https://apnews.com/article/business-bills-caced68243ed52f5d6cb767c77a3b269'
        // },
        // {
        //   title: 'CDC endorses COVID booster for millions of older Americans',
        //   subtext: 'The Centers for Disease Control and Prevention on Thursday endorsed booster shots for millions of older or otherwise vulnerable Americans, opening a major new phase in the U.S vaccination drive against COVID-19.',
        //   image: 'https://storage.googleapis.com/afs-prod/media/38d614f95c1047e48bc09f8f3c29b9a9/2930.jpeg',
        //   url: 'https://apnews.com/article/coronavirus-pandemic-business-science-health-coronavirus-vaccine-95b8d9a432b60fe0e9713adf75dde0ee'
        // },
        // {
        //   title: 'Woman arrested on suspicion of starting California blaze',
        //   subtext: 'A woman has been arrested on suspicion of starting a Northern California wildfire that spread rapidly, burning homes and prompting evacuation orders Thursday in a rural community, authorities said.',
        //   image: 'https://storage.googleapis.com/afs-prod/media/40a85d418f324f5db7c846eba5c30539/1000.jpeg',
        //   url: 'https://apnews.com/article/fires-california-wildfires-evacuations-redding-66a00bdfc6747392f7dfd1d4a6587281'
        // },
        // {
        //   title: 'NY hospitals fear staff shortage as vaccine deadline looms',
        //   subtext: 'Hospitals and nursing homes in New York are bracing for the possibility that a statewide COVID-19 vaccine mandate for health care workers could lead to staff shortages when it takes effect Monday.',
        //   image: 'https://storage.googleapis.com/afs-prod/media/da047e910d6b47ad970345706aa192e3/1000.jpeg',
        //   url: 'https://apnews.com/article/coronavirus-pandemic-lifestyle-business-kathy-hochul-new-york-ceb924e4704c085b05e3439a72c928f2'
        // },
      ]
    }
  },
  created() {
    if (process.env.NODE_ENV === 'development') {
      this.fetch_feed()
    }
  },
  methods: {
    async init_new_user() {
      let res = await axios.get('http://localhost/new_user')
      await Storage.set({
        key: 'token',
        value: res.data.token,
      })
      return true
    },
    async fetch_feed() {
      const feed_url = 'http://localhost/feed'
      let token = await Storage.get({key: 'token'})

      if (token.value) {

        try {
          let res = await axios.get(feed_url, {headers: {'Authorization': `Bearer ${token.value}`}})
          this.posts = res.data.posts
          return true
        } catch (e) {
          await this.init_new_user()
          token = await Storage.get({key: 'token'})
          let res = await axios.get(feed_url, {headers: {'Authorization': `Bearer ${token.value}`}})
          this.posts = res.data.posts
          return true
        }

      } else {

        await this.init_new_user()
        token = await Storage.get({key: 'token'})
        let res = await axios.get(feed_url, {headers: {'Authorization': `Bearer ${token.value}`}})
        this.posts = res.data.posts
        return true

      }
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