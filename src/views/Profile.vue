<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-button color="medium" size="small" @click="info">
            <ion-icon :icon="informationCircleOutline"/>
          </ion-button>
        </ion-buttons>
        <ion-buttons slot="end" v-if="uid">
          <ion-button color="medium" size="small" @click="more">
            <ion-icon :icon="ellipsisHorizontalOutline"/>
          </ion-button>
        </ion-buttons>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true" class="ion-padding">
      <ion-refresher slot="fixed" @ionRefresh="fetch_posts">
        <ion-refresher-content></ion-refresher-content>
      </ion-refresher>

      <div v-if="uid">

        <div v-if="user"
             class="user-container ion-justify-content-center ion-align-items-center ion-padding">
          <ion-avatar class="ion-text-center ion-margin-top">
            <ion-img :src="host + user.image"/>
          </ion-avatar>
          <ion-text color="primary">
            <h5 class="ion-text-center">{{ user.name }}</h5>
          </ion-text>

        </div>
        <div class="bottom-divider"></div>
        <ion-list v-if="user">
          <ion-list-header class="ion-margin-bottom">Posts</ion-list-header>

          <ion-item v-for="post in user.posts" :key="post.id" @click="open_post(post.id)">

            <ion-img class="post-image" v-if="post.image" :src="post.image" slot="start"/>
            <div class="post-content ion-no-margin" slot="end">
              <p class="ion-no-margin"><small><b>{{ post.title }}</b></small></p>
              <p class="ion-no-margin"><small>{{ post.subtext }}</small></p>
              <post-summary :post="post"/>
            </div>
          </ion-item>
        </ion-list>

      </div>

      <auth-options v-else/>

    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonContent,
  IonButton,
  IonAvatar,
  IonImg,
  IonList,
  IonItem,
  IonListHeader,
  IonText,
  IonRefresher,
  IonRefresherContent,
  IonIcon,
  IonHeader,
  IonButtons,
  actionSheetController,
  IonToolbar,
  alertController
} from '@ionic/vue';
import {
  ellipsisHorizontalOutline,
  informationCircleOutline
} from 'ionicons/icons';
import AuthOptions from "../components/AuthOptions";
import init_user from "../store/init_user";
import api from "../base/api";
import PostSummary from "../components/PostSummary";

const axios = require("axios").default


export default {
  name: 'Profile',
  mixins: [api],
  components: {
    AuthOptions,
    IonContent,
    IonPage,
    IonButton,
    IonAvatar,
    IonImg,
    IonList,
    IonItem,
    IonListHeader,
    IonText,
    PostSummary,
    IonRefresher,
    IonRefresherContent,
    IonIcon,
    IonHeader,
    IonButtons,
    IonToolbar
  },
  props: {
    user_id: Number
  },
  data() {
    return {
      ellipsisHorizontalOutline,
      informationCircleOutline,
      user: null
    }
  },
  created() {
    this.fetch_posts()
  },
  watch: {
    uid(new_uid) {
      if (new_uid) {
        axios.get(`${this.host}/profile/${this.uid}`)
            .then(res => {
              this.user = res.data.user
            })
      }
    }
  },
  methods: {
    async fetch_posts(event = null) {
      if (this.uid) {
        const res = await axios.get(`${this.host}/profile/${this.uid}`)
        this.user = res.data.user
      }
      if (event) event.target.complete()
    },
    async logout() {
      const token = await init_user()
      this.$store.commit('set_token', token)
      this.$store.commit('set_uid', 0)
      this.$router.replace('/tabs/feed')
    },
    async confirm_logout() {
      const alert = await alertController
          .create({
            message: 'Are you sure you want to logout?',
            buttons: [
              {
                text: 'Cancel',
                role: 'cancel',
              },
              {
                text: 'Yes',
                handler: this.logout
              },
            ],
          });
      return alert.present();
    },
    async delete_account() {
      await axios.get(`${this.host}/delete_user`, {headers: this.headers})

      const token = await init_user()
      this.$store.commit('set_token', token)
      this.$store.commit('set_uid', 0)
      this.$router.replace('/tabs/feed')
    },
    async confirm_delete_account() {
      const alert = await alertController
          .create({
            header: 'Warning!',
            message: 'Are you sure you want to delete your account? This action is irreversible.',
            buttons: [
              {
                text: 'Cancel',
                role: 'cancel',
              },
              {
                text: 'Yes',
                handler: this.delete_account
              },
            ],
          });
      return alert.present();
    },
    open_post(id) {
      this.$router.push(`/post/view/${id}`)
    },
    async info() {
      const actionSheet = await actionSheetController
          .create({
            buttons: [
              {
                text: 'Contact us',
                handler: async () => {
                  const alert = await alertController.create({
                    message: 'Please send us an email at <b>contact@sharknews.live</b>, we would love to hear from you!',
                    buttons: ['OK'],
                  });
                  return alert.present();
                }
              },
              {
                text: 'Privacy policy',
                handler: () => this.$router.push('/privacy-policy')
              },
              {
                text: 'Terms and conditions',
                handler: () => this.$router.push('/terms-and-conditions')
              }
            ],
          });
      await actionSheet.present();
    },
    async more() {
      const actionSheet = await actionSheetController
          .create({
            buttons: [
              {
                text: 'Logout',
                role: 'destructive',
                handler: this.confirm_logout,
              },
              {
                text: 'Delete account',
                role: 'destructive',
                handler: this.confirm_delete_account
              },
              {
                text: 'Cancel',
                role: 'cancel',
              },
            ],
          });
      await actionSheet.present();
    }
  }
}
</script>

<style scoped>
.user-container {
  display: flex;
  flex-direction: column;
}

ion-avatar {
  width: 80px;
  height: 80px;
}

.bottom-divider {
  border-bottom: 1px solid lightgrey;
}

.post-image {
  max-width: 5rem;
  border-radius: 5px !important;
  overflow: hidden;
}
</style>