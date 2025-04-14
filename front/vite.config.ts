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
    host: "meeting.mosckba.ru",
    port: 80,
    strictPort: true, // Fail if port is already in use
    cors: true, // Enable CORS
    hmr: {
      // Try to fix HMR issues in Docker
      clientPort: 80,
      host: '0.0.0.0',
    }
  },
  preview: {
    // Also configure preview server
    port: 80,
    host: "meeting.mosckba.ru"
  },

  css: {
    preprocessorOptions: {
      scss: {
        api: 'modern-compiler',
      }
    }
  },
})
