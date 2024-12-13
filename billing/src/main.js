import './index.css'

import { createApp } from 'vue'
import { AltrixUI, setConfig, frappeRequest } from 'frappe-ui'
import router from './router'
import App from './App.vue'

let app = createApp(App)

setConfig('resourceFetcher', frappeRequest)
app.use(AltrixUI)
app.use(router)

app.mount('#app')
