<template>
  <ion-page>
    <ion-content :fullscreen="true" class="ion-padding">

      <div v-if="uid">

        <div v-if="user" class="user-container ion-justify-content-center ion-align-items-center ion-padding">
          <ion-avatar class="ion-text-center">
            <ion-img :src="host + user.image"/>
          </ion-avatar>
          <ion-text color="primary">
              <h5 class="ion-text-center">{{ user.name }}</h5>
          </ion-text>
          <ion-button class="ion-text-center" color="danger" size="small" fill="outline" @click="logout">Log out
          </ion-button>

        </div>
        <div class="bottom-divider"></div>
        <ion-list v-if="user">
          <ion-list-header>Posts</ion-list-header>

          <ion-item v-for="post in user.posts" :key="post.id" @click="open_post(post.id)">

            <ion-img class="post-image" :src="post.image" slot="start"/>
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
  IonText
  // IonLabel
} from '@ionic/vue';
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
    PostSummary
  },
  props: {
    user_id: Number
  },
  data() {
    return {
      user: null
    }
  },
  created() {
    if (this.uid) {
      axios.get(`${this.host}/profile/${this.uid}`)
          .then(res => {
            this.user = res.data.user
          })
    }
  },
  watch: {
    uid(new_uid, old_uid) {
      console.log(new_uid, old_uid)
      if (new_uid) {
        axios.get(`${this.host}/profile/${this.uid}`)
            .then(res => {
              this.user = res.data.user
            })
      }
    }
  },
  methods: {
    async logout() {
      const token = await init_user()
      this.$store.commit('set_token', token)
      this.$store.commit('set_uid', 0)
      this.$router.replace('/tabs/feed')
    },
    open_post(id) {
      this.$router.push(`/post/view/${id}`)
    },
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