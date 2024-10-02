<template>
    <q-layout view="hHh lpR fFf">
        <q-toolbar class="header">
            <div class="fit row wrap justify-around items-center content-center">
                <img src="../assets/logo_header.png" alt="logo" width="50rem">
                <q-btn-toggle
                    v-model="model"
                    flat
                    stretch
                    toggle-color="grey"
                    :options="options"
                    @click="navigateTo(model)"
                />
                <p>Bem vindo,<br/><span class="text-weight-medium">{{ client_name }}</span>!</p>
            </div>
        </q-toolbar>
        <q-page-container>
            <router-view />
        </q-page-container>
    </q-layout>
</template>
<script>
import { api } from 'src/boot/axios'
export default {
  name: 'MainLayout',
  data () {
    return {
      model: 'home',
      client_name: '',
      options: [
        { label: 'INICIO', value: 'home' },
        { label: 'CARTEIRAS', value: 'carteira' }
      ]
    }
  },
  mounted () {
    this.get_client_name()
  },
  methods: {
    navigateTo (page) {
      this.$router.push(page)
    },
    get_client_name () {
      api.get('/users/me')
        .then(response => {
          this.client_name = response.data.name
        })
        .catch(error => {
          console.error('Error ao capturar nome do banco', error)
        })
    }
  }
}
</script>
<style scoped>
.header {
    background: linear-gradient(to left, #464B9B, #8185C6);
    padding: 5px;
    color: #fff;
}
</style>
