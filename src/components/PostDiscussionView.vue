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
          <ion-button color="medium" size="small" @click.stop="more_actions_post(post)">
            <ion-icon :icon="ellipsisHorizontalOutline"/>
          </ion-button>
        </ion-buttons>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true" class="">
      <ion-refresher slot="fixed" @ionRefresh="fetch_post">
        <ion-refresher-content></ion-refresher-content>
      </ion-refresher>

      <div class="posts ion-justify-content-center ion-align-items-center ion-padding-top">
        <post-display :post="post"/>
      </div>

      <comment v-for="comment in post.comments" :key="comment.id" :comment="comment" @reply="write_reply"
               @more="more_actions_comment"/>

      <div class="ion-padding bottom-pad"></div>

      <ion-modal :is-open="writing_comment">
        <write-comment-modal @dismiss="toggle_write_comment" @send="comment_sent"
                             :post="post" :parent_comment="writing_comment_parent"/>
      </ion-modal>

      <ion-modal :is-open="writing_report">
        <content-report-modal @dismiss="toggle_write_report" @send="report_sent" :reasons="reasons"/>
      </ion-modal>

      <ion-fab vertical="bottom" horizontal="end" slot="fixed">
        <ion-card @click="write_comment">
          <ion-card-content>
            Add a comment...
          </ion-card-content>
        </ion-card>
      </ion-fab>

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
  IonCardContent,
  IonCard,
  IonModal,
  IonRefresher,
  IonRefresherContent,
  IonIcon,
  IonFab,
} from '@ionic/vue';
import {
  shareOutline,
  chatboxEllipsesOutline,
  fishOutline,
  personCircleOutline,
  sendOutline,
  ellipsisHorizontalOutline
} from 'ionicons/icons';
import Comment from "./Comment";
import WriteCommentModal from "./WriteCommentModal";
import ContentReportModal from "./ContentReportModal";
import api from "../base/api";
import content_report from "../base/content_report";
import mixpanel from "mixpanel-browser";
import PostDisplay from "./PostDisplay";
const axios = require("axios").default


export default {
  name: "PostDiscussionView",
  mixins: [api, content_report],
  components: {
    IonContent,
    IonPage,
    IonButton,
    IonHeader,
    IonToolbar,
    IonBackButton,
    IonButtons,
    IonImg,
    IonCardContent,
    IonCard,
    IonFab,
    IonModal,
    Comment,
    WriteCommentModal,
    IonRefresher,
    IonRefresherContent,
    ContentReportModal,
    IonIcon,
    PostDisplay
  },
  data() {
    return {
      shareOutline,
      chatboxEllipsesOutline,
      fishOutline,
      personCircleOutline,
      sendOutline,
      ellipsisHorizontalOutline,
      comment: '',
      post: {},
      writing_comment: false,
      writing_comment_parent: null
    }
  },
  created() {
    this.fetch_post()
  },
  methods: {
    async fetch_post(event = null) {
      const post_id = this.$route.params.id
      const res = await axios.get(`${this.host}/post/discussion/${post_id}`, {headers: this.headers})
      this.post = res.data.post

      mixpanel.track('Post discussion view', {
        unique_id: this.$store.state.uid
      })

      if (event) event.target.complete()
    },
    toggle_write_comment() {
      this.writing_comment = !this.writing_comment
    },
    write_comment() {
      if (!this.uid) {
        this.$router.push('/auth')
        return
      }

      this.writing_comment_parent = null
      this.toggle_write_comment()
    },
    write_reply(parent_comment) {
      if (!this.uid) {
        this.$router.push('/auth')
        return
      }

      this.writing_comment_parent = parent_comment
      this.toggle_write_comment()
    },
    comment_sent(comment) {
      this.toggle_write_comment()
      if (this.writing_comment_parent) {
        this.writing_comment_parent.children.unshift(comment)
      } else {
        this.post.comments.unshift(comment)
      }
    }
  }
}
</script>

<style scoped>
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

/*.add-comment-hover {*/
/*  position: fixed;*/
/*  bottom: 0;*/
/*  right: 0;*/
/*  color: #8c8c8c;*/
/*  !*width: 100%;*!*/
/*}*/

.bottom-pad {
  padding-bottom: 6rem;
}

.posts {
  display: flex;
  flex-direction: column;
}
</style>