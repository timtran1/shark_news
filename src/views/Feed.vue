<template>
  <ion-page>
    <ion-header collapse="condense" class="ion-margin-bottom">
      <ion-toolbar>
        <!--        <ion-title>New post</ion-title>-->
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true">
      <ion-refresher slot="fixed" @ionRefresh="fetch_feed($event, true)">
        <ion-refresher-content></ion-refresher-content>
      </ion-refresher>

      <div class="posts ion-justify-content-center ion-align-items-center">
        <post-display v-for="post in posts" :key="post.id" :post="post" :show_username="true"/>
      </div>

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
  IonInfiniteScroll
} from '@ionic/vue';
import api from "../base/api";
import mixpanel from "mixpanel-browser";
import PostDisplay from "../components/PostDisplay";

const axios = require("axios").default


export default {
  name: 'Feed',
  mixins: [api],
  components: {
    IonContent,
    IonPage,
    IonRefresher,
    IonRefresherContent,
    IonHeader,
    IonToolbar,
    IonInfiniteScrollContent,
    IonInfiniteScroll,
    PostDisplay
  },
  data() {
    return {
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

      if (refresh)this.posts = res.data.posts
      else this.posts = this.posts.concat(res.data.posts)
      this.$store.state.feed_offset += res.data.posts.length
      if (res.data.posts.length === 0) this.$store.state.feed_end_reached = true

      mixpanel.track('Feed request', {
        unique_id: this.$store.state.uid
      })

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
</style>