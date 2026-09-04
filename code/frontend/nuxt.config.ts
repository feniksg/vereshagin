// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  pages: true,

  css: [
    '@/assets/css/variables.scss'
  ],

  modules: [
   '@nuxt/image',
  ],

  app: {
    head: {
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0',
      title: 'Верещагин',
      link: [
        {
          rel: 'stylesheet',
          href: 'https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css',
          integrity : 'sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N',
          crossorigin: 'anonymous'
        },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap',
        },
      ],
      script: [
        {
          src: 'https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js'
        },
        {
          src: 'https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js'
        },
      ]
    }
  },

  compatibilityDate: '2024-07-05',
})