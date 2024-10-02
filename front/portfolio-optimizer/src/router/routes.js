const routes = [
  { path: '/', name: 'login', component: () => import('pages/IndexPage.vue') },
  { path: '/dashboard', name: 'dashboard', component: () => import('pages/Dashboard.vue') },
  { path: '/:catchAll(.*)*', component: () => import('pages/ErrorNotFound.vue') }
]

export default routes
