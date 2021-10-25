<template>
  <div @click="open_post" class="ion-padding-start ion-padding-end post-container">
    <h4>{{ $props.post.title }}</h4>
    <ion-img class="post-img" v-if="$props.post.image" :src="$props.post.image"/>
    <p>{{ $props.post.subtext }}</p>

    <post-summary :post="$props.post"/>

    <div class="bottom-divider"/>
  </div>
</template>

<script>
import {
  IonImg
} from '@ionic/vue';
import api from "../base/api";
import PostSummary from "./PostSummary";
import {Browser} from '@capacitor/browser';
import {
  ellipsisHorizontalOutline
} from 'ionicons/icons';


export default {
  name: "PostDisplay",
  mixins: [api],
  components: {
    IonImg,
    PostSummary
  },
  props: {
    post: Object,
    show_username: Boolean
  },
  data() {
    return {
      ellipsisHorizontalOutline
    }
  },
  methods: {
    open_post() {
      if (this.$props.post.url) {
        if (this.$props.post.can_load_iframe) this.$router.push(`/post/view/${this.$props.post.id}`)
        else Browser.open({url: this.$props.post.url})
      } else {
        this.$router.push(`/post/discussion/${this.$props.post.id}`)
      }
    },
  }
}
</script>

<style scoped>
h4 {
  margin-top: 0 !important;
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
  max-width: 700px;
  cursor: pointer;
}
</style>