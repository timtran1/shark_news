<template>

  <form @submit.prevent="send">
    <ion-header translucent>
      <ion-toolbar>
        <ion-title>
          Report a problem
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
        <form action="">
          <ion-list>
            <ion-radio-group v-model="reason_value">
              <ion-list-header>
                <ion-label>Tell us what's wrong with this content</ion-label>
              </ion-list-header>

              <ion-item v-for="reason in $props.reasons" :key="reason">
                <ion-label>{{ reason }}</ion-label>
                <ion-radio slot="start" :value="reason"></ion-radio>
              </ion-item>
            </ion-radio-group>
          </ion-list>

          <ion-textarea v-show="reason_value==='Other' " placeholder="Please specify here..."
                        :required="reason_value==='Other'"
                        v-model="reason_value_other"></ion-textarea>
        </form>
      </div>
    </ion-content>
  </form>

</template>

<script>
import {
  IonItem,
  IonLabel,
  IonList,
  IonListHeader,
  IonRadio,
  IonRadioGroup,
  IonButton,
  IonButtons,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  loadingController,
  IonTextarea
} from '@ionic/vue';
import api from "../base/api";
import {default as axios} from "axios";


export default {
  name: "WriteCommentModal",
  mixins: [api],
  components: {
    IonItem,
    IonLabel,
    IonList,
    IonListHeader,
    IonRadio,
    IonRadioGroup,
    IonButton,
    IonButtons,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonTextarea
  },
  emits: ['send', 'dismiss'],
  data() {
    return {
      reason_value: '',
      reason_value_other: ''
    }
  },
  props: {
    reasons: Array,
    post: Object,
    parent_comment: Object
  },
  methods: {
    async send() {
      const loading = await loadingController
          .create({
            cssClass: 'my-custom-class',
            message: 'Sending...',
            duration: 2000
          });
      await loading.present();

      let params = {
        reason: this.reason_value === 'Other' ? this.reason_value_other : this.reason_value,
      }

      if (this.$store.state.reporting === 'comment') {
        params.comment_id = this.$store.state.reporting_comment.id
      } else {
        params.post_id = this.$store.state.reporting_post.id
      }

      const res = await axios.get(`${this.host}/report/new`, {
        params,
        headers: this.headers
      })

      const report = res.data.report
      loading.dismiss()
      this.$emit('send', report)

    },
    dismiss() {
      this.$emit('dismiss')
    }
  }
}
</script>

<style scoped>

</style>