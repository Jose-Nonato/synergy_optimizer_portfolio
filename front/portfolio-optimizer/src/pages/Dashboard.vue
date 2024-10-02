<template>
    {{ message }}
</template>
<script>
import { api } from 'src/boot/axios'
export default {
  name: 'DashboardAssets',
  data () {
    return {
      message: 'Dashboard'
    }
  },
  mounted () {
    this.teste()
  },
  methods: {
    teste () {
      api.get('/users/me')
        .then(response => {
          console.log(response)
        })
    }
  }
}
</script>
