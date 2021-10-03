<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button default-href="/tabs/feed"></ion-back-button>
        </ion-buttons>
        <ion-buttons slot="end" v-if="post.user">
          <ion-button color="medium" size="small">
            <ion-img :src="host + post.user.image" class="user-avatar"/>
            <span class="user-name">{{ post.user.name }}</span>
          </ion-button>
        </ion-buttons>

        <!--        <ion-title v-if="post">{{ post.title }}</ion-title>-->
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true" class="">
      <div v-if="post" class="post-container ion-padding">

        <h4 class="ion-no-margin">{{ post.title }}</h4>
        <ion-img class="post-img" v-if="post.image" :src="post.image"/>
        <p>{{ post.subtext }}</p>

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

      <comment v-for="comment in post.comments" :key="comment.id" :comment="comment"/>


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
  IonButton,
  IonHeader,
  IonToolbar,
  IonBackButton,
  IonButtons,
  IonImg
} from '@ionic/vue';
import {shareOutline, chatboxEllipsesOutline, fishOutline, personCircleOutline} from 'ionicons/icons';
import Comment from "./Comment";
const axios = require("axios").default

export default {
  name: "PostDiscussionView",
  components: {
    IonContent,
    IonPage,
    IonRow,
    IonCol,
    IonIcon,
    IonButton,
    IonHeader,
    IonToolbar,
    IonBackButton,
    IonButtons,
    IonImg,
    Comment
  },
  data() {
    return {
      shareOutline,
      chatboxEllipsesOutline,
      fishOutline,
      personCircleOutline,
      post: {}
    }
  },
  created() {
    const post_id = this.$route.params.id
    let host = ''

    if (process.env.NODE_ENV === 'development') {
      host = 'http://localhost'
    }

    axios.get(`${host}/post/discussion/${post_id}`)
        .then(res => {
          this.post = res.data.post
        })
  },
  computed: {
    host() {
      let host = ''

      if (process.env.NODE_ENV === 'development') {
        host = 'http://localhost'
      }

      return host
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

.user-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 5px;
}
</style>