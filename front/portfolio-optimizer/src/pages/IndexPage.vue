<template>
  <div class="q-pa-md">
    <img src="../assets/logo_preta.jpg" alt="Logo de fundo escuro" width="15%"/>
  </div>
  <div class="row justify-around items-center" style="height: 85vh;">
    <div class="q-pr-lg">
      <q-card class="q-pa-lg">
        <q-form
          @submit="onSubmit"
          @reset="onReset"
        >
          <p class="text-h4 text-weight-medium">LOGIN</p>
          <q-input
            outlined
            label="Email"
            type="email"
            v-model="user"
            class="q-pb-lg"
            :rules="[val => val && val.length > 0 || 'Por favor, digite alguma coisa!']"
          />
          <q-input
            outlined
            label="Senha"
            type="password"
            v-model="password"
            class="q-pb-lg"
            :rules="[val => val && val.length > 0 || 'Por favor, digite alguma coisa!']"
          />
          <a href="#">Esqueceu sua senha?</a>
          <q-btn class="full-width q-mt-md" label="ENTRAR" type="submit" color="primary"/>
          <p class="q-pt-md">Não possui conta ? <a href="#" class="text-weight-medium">Entre em contato com o suporte</a></p>
        </q-form>
      </q-card>
    </div>
    <div class="q-pr-lg">
      <img src="../assets/ilustracao.jpg" alt="Ilustração" width="500rem"/>
    </div>
  </div>
</template>
<script>
import { ref } from 'vue'
export default {
  setup () {
    const user = ref(null)
    const password = ref(null)
    return {
      user,
      password,

      onSubmit () {
        alert('Formulário enviado!')
      },
      onReset () {
        user.value = null
        password.value = null
      }
    }
  }
}
</script>
<style scoped>
a {
  text-decoration: none;
  color: #595BD4;
}
</style>
