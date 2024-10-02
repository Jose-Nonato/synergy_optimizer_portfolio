<template>
  {{ client_name }}
</template>
<script>
import { api } from 'src/boot/axios'
export default {
  name: 'DashboardAssets',
  data () {
    return {
      message: 'Dashboard',
      client_name: ''
    }
  },
  mounted () {
    this.get_client_name()
  },
  methods: {
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
