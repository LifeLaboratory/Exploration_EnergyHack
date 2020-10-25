import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'ant-design-vue/dist/antd.css'
import { 
  Layout,
  Menu,
  Icon,
  PageHeader,
  Button,
  Upload,
  Collapse,
  Spin,
  Card
 } from 'ant-design-vue'

Vue.use(Spin)
Vue.use(Collapse)
Vue.use(Layout)
Vue.use(Menu)
Vue.use(Icon)
Vue.use(PageHeader)
Vue.use(Upload)
Vue.use(Button)
Vue.use(Card)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
