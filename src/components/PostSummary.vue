<template>

  <ion-row>
    <ion-col size="4">
      <ion-button fill="clear" size="small" expand="block" @click.stop="share">
        <ion-icon :icon="shareOutline" slot="start"/>
        Share
      </ion-button>
    </ion-col>
    <ion-col size="4">
      <ion-button fill="clear" size="small" expand="block" @click.stop="open_post_discussion($props.post.id)">
        <ion-icon :icon="chatboxEllipsesOutline" slot="start"/>
        {{ $props.post.comment_count }}
      </ion-button>
    </ion-col>
    <ion-col size="4">
      <ion-button :fill="like_fill" size="small" expand="block" @click.stop="like">
        <ion-img :src="require('@/assets/shark.svg')"/>
        {{ $props.post.likes }}
      </ion-button>
    </ion-col>
  </ion-row>

</template>

<script>
import {
  IonRow,
  IonCol,
  IonIcon,
  IonImg,
  IonButton
} from '@ionic/vue';
import {
  shareOutline,
  chatboxEllipsesOutline,
} from 'ionicons/icons';
import api from "../base/api";
import {Share} from '@capacitor/share';

const axios = require("axios").default


export default {
  name: "PostSummary",
  mixins: [api],
  components: {
    IonRow,
    IonCol,
    IonIcon,
    IonImg,
    IonButton
  },
  props: {
    post: Object,
  },
  data() {
    return {
      shareOutline,
      chatboxEllipsesOutline,
    }
  },
  computed: {
    like_fill() {
      return this.$props.post.liked ? 'outline' : 'clear'
    }
  },
  methods: {
    open_post_discussion(id) {
      let path = `/post/discussion/${id}`
      if (path !== this.$route.path) this.$router.push(path)
    },
    like() {
      if (!this.uid) {
        this.$router.push('/auth')
        return
      }

      axios.get(`${this.host}/post/like/${this.$props.post.id}`, {
        headers: this.headers
      })
      this.$props.post.liked = !this.$props.post.liked
      if (this.$props.post.liked) this.$props.post.likes++
      else this.$props.post.likes--
    },
    share() {
      const post = this.$props.post
      return Share.share({
        title: `${post.title} - SharkNews`,
        text: `${post.title} - SharkNews`,
        url: `https://sharknews.live/post/discussion/${post.id}`,
        dialogTitle: 'Share post',
      });
    }
  }
}
</script>

<style scoped>
ion-img {
  /*width: 60px;*/
  /*height: 40px;*/
  height: 25px;
  margin-right: 5px;
}
</style>