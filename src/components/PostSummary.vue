<template>

  <ion-row>
    <ion-col size="4">
      <ion-button fill="clear" size="small" expand="block">
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
      <ion-button fill="clear" size="small" expand="block">
        <ion-img :src="require('@/assets/ss.png')"/>
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
  IonImg
} from '@ionic/vue';
import {
  shareOutline,
  chatboxEllipsesOutline,
} from 'ionicons/icons';

export default {
  name: "PostSummary",
  components: {
    IonRow,
    IonCol,
    IonIcon,
    IonImg
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
  methods: {
    open_post_discussion(id) {
      let path = `/post/discussion/${id}`
      if (path !== this.$route.path) this.$router.push(path)
    },
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