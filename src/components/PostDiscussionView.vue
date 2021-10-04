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
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true" class="">
      <div v-if="post" class="post-container ion-padding">

        <h4>{{ post.title }}</h4>
        <ion-img class="post-img" v-if="post.image" :src="post.image"/>
        <p>{{ post.subtext }}</p>

        <post-summary :post="post"/>

        <div class="bottom-divider"></div>
      </div>

      <form class="ion-padding-start ion-padding-end ion-padding-top" @submit.prevent="add_comment">
        <ion-row>
          <ion-col size="10">
            <ion-textarea ref="comment" v-model="comment" placeholder="Add a comment..." required/>
          </ion-col>
          <ion-col size="2">
            <ion-button type="submit" fill="clear" size="small">
              <ion-icon :icon="sendOutline" slot="end"/>
            </ion-button>
          </ion-col>
        </ion-row>
      </form>

      <comment v-for="comment in post.comments" :key="comment.id" :comment="comment"/>

      <div class="ion-padding bottom-pad"></div>

      <!--      <ion-card class="add-comment-hover" @click="focus_comment">-->
      <!--        <ion-card-content>-->
      <!--          Add a comment...-->
      <!--        </ion-card-content>-->
      <!--      </ion-card>-->

    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonContent,
  IonButton,
  IonHeader,
  IonToolbar,
  IonBackButton,
  IonButtons,
  IonImg,
  IonTextarea,
  // IonCardContent,
  // IonCard,
  IonRow,
  IonCol,
  IonIcon
} from '@ionic/vue';
import {shareOutline, chatboxEllipsesOutline, fishOutline, personCircleOutline, sendOutline} from 'ionicons/icons';
import Comment from "./Comment";
import PostSummary from "../components/PostSummary";
import api from "../base/api";

const axios = require("axios").default

export default {
  name: "PostDiscussionView",
  mixins: [api],
  components: {
    IonContent,
    IonPage,
    IonButton,
    IonHeader,
    IonToolbar,
    IonBackButton,
    IonButtons,
    IonImg,
    IonTextarea,
    // IonCardContent,
    // IonCard,
    IonRow,
    IonCol,
    IonIcon,
    Comment,
    PostSummary
  },
  data() {
    return {
      shareOutline,
      chatboxEllipsesOutline,
      fishOutline,
      personCircleOutline,
      sendOutline,
      comment: '',
      post: {}
    }
  },
  created() {
    const post_id = this.$route.params.id
    axios.get(`${this.host}/post/discussion/${post_id}`,
        {headers: this.headers}
    )
        .then(res => {
          this.post = res.data.post
        })
  },
  methods: {
    async add_comment() {
      if (!this.uid) {
        this.$router.push('/auth')
        return
      }

      if (this.comment) {
        const res = await axios.get(`${this.host}/post/comment`, {
          params: {
            comment: this.comment,
            post_id: this.post.id
          },
          headers: this.headers
        })

        const comment = res.data.comment
        this.post.comments.unshift(comment)
        this.comment = ''
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

.user-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 5px;
}

.add-comment-hover {
  position: fixed;
  bottom: 0;
  right: 0;
  color: #8c8c8c;
}

.bottom-pad {
  padding-bottom: 5rem;
}
</style>