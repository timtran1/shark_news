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

      <comment v-for="comment in post.comments" :key="comment.id" :comment="comment" @reply="write_reply"/>

      <div class="ion-padding bottom-pad"></div>

      <ion-card class="add-comment-hover" @click="write_comment">
        <ion-card-content>
          Add a comment...
        </ion-card-content>
      </ion-card>

      <ion-modal :is-open="writing_comment">
        <write-comment-modal @dismiss="toggle_write_comment" @send="comment_sent"
                             :post="post" :parent_comment="writing_comment_parent"/>
      </ion-modal>

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
  // modalController
} from '@ionic/vue';
import {shareOutline, chatboxEllipsesOutline, fishOutline, personCircleOutline, sendOutline} from 'ionicons/icons';
import Comment from "./Comment";
import PostSummary from "../components/PostSummary";
import WriteCommentModal from "./WriteCommentModal";
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
    IonCardContent,
    IonCard,
    IonModal,
    Comment,
    PostSummary,
    WriteCommentModal
  },
  data() {
    return {
      shareOutline,
      chatboxEllipsesOutline,
      fishOutline,
      personCircleOutline,
      sendOutline,
      comment: '',
      post: {},
      writing_comment: false,
      writing_comment_parent: null
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
.post-img {
  border-radius: 10px !important;
  overflow: hidden;
}

.bottom-divider {
  border-bottom: 1px solid lightgrey;
  padding-bottom: 10px;
  margin-bottom: 10px;
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
  /*width: 100%;*/
}

.bottom-pad {
  padding-bottom: 5rem;
}
</style>