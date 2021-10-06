<template>

  <form @submit.prevent="send">
    <ion-header translucent>
      <ion-toolbar>
        <ion-title>
          {{ $props.parent_comment ? `Replying to ${$props.parent_comment.user.name}` : 'Add a comment' }}
        </ion-title>
        <ion-buttons slot="start">
          <ion-button @click="dismiss">Close</ion-button>
        </ion-buttons>
        <ion-buttons slot="end">
          <ion-button type="submit">Send</ion-button>
        </ion-buttons>
      </ion-toolbar>
    </ion-header>
    <ion-content fullscreen>
      <div class="ion-padding-start ion-padding-end ion-padding-top">
        <ion-row>
          <ion-col size="12">
            <ion-textarea ref="comment" v-model="comment" required autofocus rows="10"/>
          </ion-col>
        </ion-row>
      </div>
    </ion-content>
  </form>

</template>

<script>
import {
  IonRow,
  IonCol,
  IonTextarea,
  IonButton,
  IonButtons,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  loadingController
} from '@ionic/vue';
import api from "../base/api";
import {default as axios} from "axios";


export default {
  name: "WriteCommentModal",
  mixins: [api],
  components: {
    IonRow,
    IonCol,
    IonTextarea,
    IonButton,
    IonButtons,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent
  },
  emits: ['send', 'dismiss'],
  data() {
    return {
      comment: ''
    }
  },
  props: {
    post: Object,
    parent_comment: Object
  },
  methods: {
    async send() {
      const loading = await loadingController
          .create({
            cssClass: 'my-custom-class',
            message: 'Please wait...',
            duration: 2000
          });
      await loading.present();

      let params = {
        comment: this.comment,
        post_id: this.$props.post.id
      }

      if (this.$props.parent_comment) {
        params.parent_comment_id = this.$props.parent_comment.id
      }

      const res = await axios.get(`${this.host}/post/comment`, {
        params,
        headers: this.headers
      })

      const comment = res.data.comment
      loading.dismiss()
      this.$emit('send', comment)

    },
    dismiss() {
      this.$emit('dismiss')
    }
  }
}
</script>

<style scoped>

</style>