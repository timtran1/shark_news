import {createApp} from 'vue'
import App from './App.vue'
import router from './router';
import init_store from './store/index'
import {IonicVue} from '@ionic/vue';
// import {Device} from '@capacitor/device';

/* Core CSS required for Ionic components to work properly */
import '@ionic/vue/css/core.css';

/* Basic CSS for apps built with Ionic */
import '@ionic/vue/css/normalize.css';
import '@ionic/vue/css/structure.css';
import '@ionic/vue/css/typography.css';

/* Optional CSS utils that can be commented out */
import '@ionic/vue/css/padding.css';
import '@ionic/vue/css/float-elements.css';
import '@ionic/vue/css/text-alignment.css';
import '@ionic/vue/css/text-transformation.css';
import '@ionic/vue/css/flex-utils.css';
import '@ionic/vue/css/display.css';

/* Theme variables */
import './theme/variables.css';


async function Application() {
    console.log('app reload')
    const store = await init_store()

    const app = createApp(App)
        .use(IonicVue)
        .use(router)
        .use(store)

    await router.isReady()
    app.mount('#app');
}

Application()