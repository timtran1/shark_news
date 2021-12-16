<template>
  <div>
    <ion-row class="user-name-row ion-padding-start ion-padding-end ion-padding-top">
      <ion-col size="6" class="ion-justify-content-center user-col" color="light">
        <span>
          <small>{{ $props.post.user.name }}</small>
        </span>
      </ion-col>
      <ion-col size="5">
      </ion-col>
      <ion-col size="1" class="ion-text-right" @click.stop="more_actions_post( $props.post)">
        <span class="ion-text-right">
          <ion-icon :icon="ellipsisHorizontalOutline"/>
        </span>
      </ion-col>
    </ion-row>
    <post-display :post=" $props.post"/>
  </div>
</template>

<script>
import {
  IonRow,
  IonCol,
  IonIcon,
} from '@ionic/vue';
import api from "../base/api";
import PostDisplay from "./PostDisplay";
import {default as axios} from "axios";
import {
  ellipsisHorizontalOutline
} from 'ionicons/icons';
import content_report from "../base/content_report";


export default {
  name: "PostDisplayFeedUnit",
  mixins: [api, content_report],
  components: {
    PostDisplay,
    IonRow,
    IonCol,
    IonIcon,
  },
  props: {
    post: Object
  },
  data() {
    return {
      ellipsisHorizontalOutline
    }
  },
  mounted() {
    let observer = new IntersectionObserver(entries => {
      if (entries[0].intersectionRatio >= 1.0) {
        // rate previous post
        if (this.$store.state.viewing_post_id !== this.$props.post.id) {
          const rating = Date.now() - this.$store.state.starting_viewing_timestamp
          if (this.$store.state.starting_viewing_timestamp > 0 && rating > 0) {
            axios.get(`${this.host}/post/rate/${this.$store.state.viewing_post_id}/${rating}`, {
              headers: this.headers,
            })
          }

          this.$store.state.viewing_post_id = this.$props.post.id
          this.$store.state.starting_viewing_timestamp = Date.now()
        }
      }

    }, {
      root: document.querySelector('#scrollArea'),
      rootMargin: '0px',
      threshold: 1.0
    });
    observer.observe(this.$el);
  },
}
</script>

<style scoped>


span {
  color: grey;
}

.user-col {
  padding-left: 0 !important;
}
</style>