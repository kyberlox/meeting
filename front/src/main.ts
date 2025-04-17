import './assets/main.css'
import "tailwindcss";
// import VueVideoPlayer from '@videojs-player/vue'
// import 'video.js/dist/video-js.css'
import { createHead } from '@unhead/vue/client'

import Toast, { type PluginOptions } from "vue-toastification";
import "vue-toastification/dist/index.css";

import { createApp } from 'vue'
import { createYmaps } from 'vue-yandex-maps';

import App from './App.vue'
import router from './router'

const app = createApp(App)
const head = createHead()

const options: PluginOptions = {
  // You can set your default options here
};

app.use(head)
  // .use(VueVideoPlayer)
  .use(router)
  .use(Toast, options)
  .use(createYmaps({
    apikey: '3f8f0af1-723b-47db-b868-be798083bba6',
  }));

app.mount('#app')
