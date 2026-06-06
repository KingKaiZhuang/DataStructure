import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { sqliteProgressPlugin } from './vite-plugin-sqlite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), sqliteProgressPlugin()],
})
