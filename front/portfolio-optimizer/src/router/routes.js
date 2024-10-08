const routes = [
  { path: '/', name: 'login', component: () => import('pages/IndexPage.vue') },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('layouts/MainLayouts.vue'),
    children: [
      { path: '', name: 'home', component: () => import('pages/Dashboard.vue') },
      { path: '/detalhes/:ticker', name: 'DetailsTicker', component: () => import('pages/DetailsTicker.vue') }
    ]
  },
  { path: '/:catchAll(.*)*', component: () => import('pages/ErrorNotFound.vue') }
]

export default routes
