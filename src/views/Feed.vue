<template>
  <ion-page>
    <ion-header collapse="condense">
      <ion-toolbar>
        <!--        <ion-title>New post</ion-title>-->
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true">
      <ion-refresher slot="fixed" @ionRefresh="fetch_feed($event, true)">
        <ion-refresher-content></ion-refresher-content>
      </ion-refresher>

      <div class="posts ion-justify-content-center ion-align-items-center">
        <div v-for="post in posts" :key="post.id">
          <ion-row class="user-name-row ion-padding-start ion-padding-end ion-padding-top">
            <ion-col size="6" class="ion-justify-content-center user-col" color="light">
              <span>
                <small>{{ post.user.name }}</small>
              </span>
            </ion-col>
            <ion-col size="5">
            </ion-col>
            <ion-col size="1" class="ion-text-right" @click.stop="more_actions_post(post)">
              <span class="ion-text-right">
                <ion-icon :icon="ellipsisHorizontalOutline"/>
              </span>
            </ion-col>
          </ion-row>
          <post-display :post="post"/>
        </div>
      </div>

      <ion-modal :is-open="writing_report">
        <content-report-modal @dismiss="toggle_write_report" @send="report_sent" :reasons="reasons"/>
      </ion-modal>

      <ion-infinite-scroll
          @ionInfinite="fetch_feed"
          threshold="100px"
          id="infinite-scroll"
          :disabled="$store.state.feed_end_reached"
      >
        <ion-infinite-scroll-content
            loading-spinner="dots"
            loading-text="Loading more posts...">
        </ion-infinite-scroll-content>
      </ion-infinite-scroll>

    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonContent,
  IonRefresher,
  IonRefresherContent,
  IonHeader,
  IonToolbar,
  IonInfiniteScrollContent,
  IonInfiniteScroll,
  IonRow,
  IonCol,
  IonIcon,
  IonModal
} from '@ionic/vue';
import api from "../base/api";
import PostDisplay from "../components/PostDisplay";
import content_report from "../base/content_report";
import ContentReportModal from "../components/ContentReportModal";

const axios = require("axios").default
import {
  ellipsisHorizontalOutline
} from 'ionicons/icons';


export default {
  name: 'Feed',
  mixins: [api, content_report],
  components: {
    IonContent,
    IonPage,
    IonRefresher,
    IonRefresherContent,
    IonHeader,
    IonToolbar,
    IonInfiniteScrollContent,
    IonInfiniteScroll,
    PostDisplay,
    IonRow,
    IonCol,
    IonIcon,
    IonModal,
    ContentReportModal
  },
  data() {
    return {
      ellipsisHorizontalOutline,
      posts: []
    }
  },
  created() {
    this.fetch_feed()
  },
  methods: {
    async fetch_feed(event = null, refresh = false) {
      if (refresh) this.$store.state.feed_offset = 0
      let res = await axios.get(`${this.host}/feed`, {
        headers: this.headers,
        params: {offset: this.$store.state.feed_offset}
      })

      if (refresh) this.posts = res.data.posts
      else this.posts = this.posts.concat(res.data.posts)

      this.$store.state.feed_offset += res.data.posts.length
      if (res.data.posts.length === 0) this.$store.state.feed_end_reached = true

      if (refresh) this.$store.state.feed_end_reached = false
      console.log(this.$store.state.feed_end_reached)

      if (event) event.target.complete()
      return true
    }
  }
}
</script>

<style scoped>
.posts {
  display: flex;
  flex-direction: column;
}

span {
  color: grey;
}

.user-col {
  padding-left: 0 !important;
}
</style>