import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import tailwindcss from '@tailwindcss/vite'

//const allowedHosts = ['meeting.mosckba.ru'];


// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    tailwindcss()
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    host: "0.0.0.0",
    port: 4173,
    proxy: {
      '/api': {
        target: 'http://meeting.mosckba.ru:8000',
        changeOrigin: true,
        secure: false
      }
    }
  },
  preview: {
    allowedHosts: ['meeting.mosckba.ru']
  },

  css: {
    preprocessorOptions: {
      scss: {
        api: 'modern-compiler',
      }
    }
  },
})
