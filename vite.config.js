import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import imagemin from 'unplugin-imagemin/vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    imagemin({
      // Default mode sharp. support squoosh and sharp
      mode: 'sharp',
      beforeBundle: false,
      // Default configuration options for compressing different pictures
      compress: {
        jpg: {
          quality: 100,
        },
        jpeg: {
          quality: 100,
        },
        png: {
          quality: 100,
        },
        webp: {
          quality: 100,
        },
      },
      conversion: [
        { from: 'jpeg', to: 'webp' },
        { from: 'JPEG', to: 'webp' },
        { from: 'png', to: 'webp' },
        { from: 'PNG', to: 'webp' },
        { from: 'JPG', to: 'webp' },
        { from: 'jpg', to: 'webp' },
      ],
    }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('node_modules')) {
            return id
              .toString()
              .split('node_modules/')[1]
              .split('/')[0]
              .toString()
          }
        },
      },
    },
  },
})
