<template>
  <div @click="open_post" class="ion-padding post-container">
    <h4>{{ $props.post.title }}</h4>
    <ion-img class="post-img" v-if="$props.post.image" :src="$props.post.image"/>
    <p>{{ $props.post.subtext }}</p>

    <ion-row class="user-name-row" v-if="$props.show_username && $props.post.user">
      <ion-col size="4" class="ion-justify-content-center" color="light">
          <span>
            {{ $props.post.user.name }}
          </span>
      </ion-col>
      <ion-col size="4">
      </ion-col>
      <ion-col size="4">
      </ion-col>
    </ion-row>

    <post-summary :post="$props.post"/>

    <div class="bottom-divider"></div>
  </div>
</template>

<script>
import {
  IonRow,
  IonCol,
  IonImg
} from '@ionic/vue';
import api from "../base/api";
import PostSummary from "./PostSummary";
import {Browser} from '@capacitor/browser';


export default {
  name: "PostDisplay",
  mixins: [api],
  components: {
    IonRow,
    IonCol,
    IonImg,
    PostSummary
  },
  props: {
    post: Object,
    show_username: Boolean
  },
  methods: {
    open_post() {
      if (this.$props.post.can_load_iframe) this.$router.push(`/post/view/${this.$props.post.id}`)
      else Browser.open({url: this.$props.post.url})
    },
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

.user-name-row {
  padding-top: 5px;
  padding-bottom: 5px;
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