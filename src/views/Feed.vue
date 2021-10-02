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

      <div v-for="post in posts" :key="post.id" @click="open_post(post.id)" class="ion-padding post-container">
        <h4>{{ post.title }}</h4>
        <ion-img class="post-img" v-if="post.image" :src="post.image"/>
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
      posts: []
    }
  },
  created() {
    if (process.env.NODE_ENV === 'development') {
      this.fetch_feed()
    }
  },
  methods: {
    open_post(id){
      this.$router.push(`/post/view/${id}`)
    },
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