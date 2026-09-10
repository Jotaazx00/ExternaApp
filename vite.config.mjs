import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: './',
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('@phosphor-icons')) return 'icons';
          if (id.includes('/three/')) return 'three';
          if (id.includes('/xlsx/')) return 'xlsx';
          if (id.includes('/react')) return 'react';
        },
      },
    },
  },
});
