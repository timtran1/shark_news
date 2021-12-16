<template>
  <ion-app>
    <ion-router-outlet/>
  </ion-app>
</template>

<script>
import {IonApp, IonRouterOutlet} from '@ionic/vue';
import {defineComponent} from 'vue';
import {default as axios} from "axios";
import api from "./base/api";
import {App} from '@capacitor/app';

export default defineComponent({
  name: 'App',
  mixins: [api],
  components: {
    IonApp,
    IonRouterOutlet
  },
  created() {
    App.addListener('appStateChange', ({isActive}) => {
      console.log({isActive});
      if (!isActive) {
        axios.get(`${this.host}/session/end`, {headers: this.headers,})
        // app exited, rate post that was viewed
        if (this.$store.state.viewing_post_id) {
          const rating = Date.now() - this.$store.state.starting_viewing_timestamp
          if (this.$store.state.starting_viewing_timestamp > 0 && rating > 0) {
            axios.get(`${this.host}/post/rate/${this.$store.state.viewing_post_id}/${rating}`, {
              headers: this.headers,
            })
          }
        }
      } else {
        axios.get(`${this.host}/session/start`, {headers: this.headers,})
        // app re-entered, reset rating timer
        this.$store.state.starting_viewing_timestamp = Date.now()
      }
    });
  },
  watch: {
    $route(to, from) {
      if (!from) console.log(from)

      const track_rating_paths = [
        '/tabs/feed',
        '/post/view',
        '/post/discussion'
      ]

      if (track_rating_paths.some(path => to.fullPath.includes(path))) {
        console.log('start tracking rating')
        if (!this.$store.state.viewing_post_id && this.$route.params.id) {// /post/view and /post/discussion only, /tabs/feed will start tracking automatically from inside PostDisplayFeedUnit
          this.$store.state.viewing_post_id = parseInt(this.$route.params.id)
          this.$store.state.starting_viewing_timestamp = Date.now()
        }
      } else {
        console.log('stop tracking rating')
        // rate post that was viewed
        if (this.$store.state.viewing_post_id) {
          const rating = Date.now() - this.$store.state.starting_viewing_timestamp
          if (this.$store.state.starting_viewing_timestamp > 0 && rating > 0) {
            axios.get(`${this.host}/post/rate/${this.$store.state.viewing_post_id}/${rating}`, {
              headers: this.headers,
            })
          }

          this.$store.state.viewing_post_id = false
          this.$store.state.starting_viewing_timestamp = 0
        }
      }
    }
  },
});
</script>