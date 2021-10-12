<template>

  <div class="comment-wrapper" :class="{isChild: $props.is_child}">
    <ion-row @click.stop="hide">
      <ion-col size="10">
        <div></div>
        <ion-button color="medium" size="small" fill="clear">
          <ion-img :src="host + $props.comment.user.image" class="user-avatar"/>
          <span class="user-name">{{ $props.comment.user.name }}</span>
        </ion-button>
      </ion-col>
      <ion-col size="2">
        <ion-button color="medium" size="small" fill="clear">
          <ion-icon v-if="!hidden" :icon="chevronDownOutline" slot="end"/>
          <ion-icon v-else :icon="chevronBackOutline" slot="end"/>
        </ion-button>
      </ion-col>
    </ion-row>

    <ion-row v-show="!hidden" class="ion-padding-start">
      <ion-col size="6">
        {{ comment.content }}
      </ion-col>
      <ion-col size="2" class="ion-no-padding">
        <ion-button color="medium" size="small" fill="clear" class="ion-no-margin" @click.stop="more">
          <ion-icon :icon="ellipsisHorizontalOutline" slot="end"/>
        </ion-button>
      </ion-col>
      <ion-col size="2" class="ion-no-padding">
        <ion-button color="medium" size="small" fill="clear" class="ion-no-margin" @click.stop="reply">
          Reply
        </ion-button>
      </ion-col>
      <ion-col size="2" class="ion-no-padding">
        <ion-button :fill="like_fill" color="medium" size="small" class="ion-no-margin" @click.stop="like">
          <ion-img :src="require('@/assets/shark.svg')" class="comment-like-icon"/>
          {{ comment.likes }}
        </ion-button>
      </ion-col>
    </ion-row>

    <div v-show="!hidden">
      <div v-for="child in comment.children" :key="child.id" class="ion-padding-start">
        <comment :comment="child" :is_child="true" @reply="reply" @more="more" :post="$props.post"
                 :parent_comment="$props.comment"></comment>
      </div>
    </div>
  </div>

</template>

<script>
import {
  IonRow,
  IonCol,
  IonIcon,
  IonImg,
  IonButton,
} from '@ionic/vue';
import {
  chevronDownOutline,
  chevronBackOutline,
  ellipsisHorizontalOutline
} from 'ionicons/icons';
import {default as axios} from "axios";
import api from "../base/api";


export default {
  name: "Comment",
  mixins: [api],
  emits: ['reply', 'more'],
  components: {
    IonRow,
    IonCol,
    IonIcon,
    IonImg,
    IonButton,
  },
  props: {
    comment: Object,
    is_child: Boolean
  },
  data() {
    return {
      chevronDownOutline,
      chevronBackOutline,
      ellipsisHorizontalOutline,
      hidden: false,
    }
  },
  computed: {
    like_fill() {
      return this.$props.comment.liked ? 'outline' : 'clear'
    }
  },
  methods: {
    hide() {
      this.hidden = !this.hidden
    },
    like() {
      if (!this.uid) {
        this.$router.push('/auth')
        return
      }

      axios.get(`${this.host}/comment/like/${this.$props.comment.id}`, {
        headers: this.headers
      })
      this.$props.comment.liked = !this.$props.comment.liked
      if (this.$props.comment.liked) this.$props.comment.likes++
      else this.$props.comment.likes--
    },
    reply(parent) {
      if (parent.id) this.$emit('reply', parent)
      else this.$emit('reply', this.$props.comment)
    },
    more(parent) {
      if (parent.id) this.$emit('more', parent)
      else this.$emit('more', this.$props.comment)
    },
  }
}
</script>

<style scoped>
span {
  color: #8c8c8c;
  font-size: 0.8rem;
}
</style>

<style>
.user-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 5px;
}

.isChild {
  border-left: 1px solid lightgrey;
}

.comment-like-icon {
  height: 20px;
  margin-right: 3px;
}
</style>