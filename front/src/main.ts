import './assets/main.css'
import "tailwindcss";
import VueVideoPlayer from '@videojs-player/vue'
import 'video.js/dist/video-js.css'
import { createHead } from '@unhead/vue/client'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createYmaps } from 'vue-yandex-maps';

import App from './App.vue'
import router from './router'

const app = createApp(App)
const head = createHead()

app.use(head)
  .use(createPinia())
  .use(VueVideoPlayer)
  .use(router)
  .use(createYmaps({
    apikey: '3f8f0af1-723b-47db-b868-be798083bba6',
  }));

app.mount('#app')
