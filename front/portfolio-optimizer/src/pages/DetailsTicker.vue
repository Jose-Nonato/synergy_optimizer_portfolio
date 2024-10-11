<template>
  <div class="q-pa-lg">
    <q-btn color="primary" outline icon="arrow_back" label="Voltar" @click="goBack" />
    <div class="q-pt-lg">
      <p class="text-h4">Dados da Empresa</p>
      <div v-if="data.length">
        <p class="text-h5">{{ data[0]['Papel'] }} ({{ data[0]['Empresa'] }})</p>
        <p>Setor: {{ data[0]['Setor'] }} | Subsetor: {{ data[0]['Subsetor'] }}</p>
        <div>
          <q-list bordered class="row">
            <div class="col-6">
              <q-item>
                <q-item-section>PL: </q-item-section>
                <q-item-section>{{ data[0]['PL'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>PVP: </q-item-section>
                <q-item-section>{{ data[0]['PVP'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>PEBIT: </q-item-section>
                <q-item-section>{{ data[0]['PEBIT'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>PSR: </q-item-section>
                <q-item-section>{{ data[0]['PSR'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Cap de Giro: </q-item-section>
                <q-item-section>{{ data[0]['PCap_Giro'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Dividendos: </q-item-section>
                <q-item-section>{{ data[0]['Div_Yield'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Crescimento 5 anos: </q-item-section>
                <q-item-section>{{ data[0]['Cres_Rec_5a'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Margem Bruta: </q-item-section>
                <q-item-section>{{ data[0]['Marg_Bruta'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Margem Líquida: </q-item-section>
                <q-item-section>{{ data[0]['Marg_Liquida'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>EBIT Ativo: </q-item-section>
                <q-item-section>{{ data[0]['EBIT_Ativo'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>ROIC: </q-item-section>
                <q-item-section>{{ data[0]['ROIC'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>ROE: </q-item-section>
                <q-item-section>{{ data[0]['ROE'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Dívida Bruta: </q-item-section>
                <q-item-section>R$ {{ format_price(data[0]['Div_Bruta'], 2) }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Dívida Líquida: </q-item-section>
                <q-item-section>R$ {{ format_price(data[0]['Div_Liquida'], 2) }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Patrimônio Líquido: </q-item-section>
                <q-item-section>R$ {{ format_price(data[0]['Patrim_Liq'], 2) }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Receita Líquida 12m: </q-item-section>
                <q-item-section>R$ {{ format_price(data[0]['Receita_Liquida_12m'], 2) }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Lucro Líquido 12m: </q-item-section>
                <q-item-section>R$ {{ format_price(data[0]['Lucro_Liquido_12m'], 2) }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Receita Líquida 3m: </q-item-section>
                <q-item-section>R$ {{ format_price(data[0]['Receita_Liquida_3m'], 2) }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Lucro Líquido 3m: </q-item-section>
                <q-item-section>R$ {{ format_price(data[0]['Lucro_Liquido_3m'], 2) }}</q-item-section>
              </q-item>
            </div>
            <div  class="col-6">
              <q-item>
                <q-item-section>Cotação: </q-item-section>
                <q-item-section>R$ {{ format_price(data[0]['Cotacao'], 2) }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Data da Ultima Cotação: </q-item-section>
                <q-item-section>{{ data[0]['Data_ult_cot'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Valor de Mercado: </q-item-section>
                <q-item-section>R$ {{ format_price(data[0]['Valor_de_mercado'], 2) }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Valor da Firma: </q-item-section>
                <q-item-section>R$ {{ format_price(data[0]['Valor_da_firma'], 2) }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Ultimo Balanço Processado: </q-item-section>
                <q-item-section>{{ data[0]['Ult_balanco_processado'] }}</q-item-section>
              </q-item>
              <q-item>
                <q-item-section>Número de Ações: </q-item-section>
                <q-item-section>{{ data[0]['Nro_Acoes'] }}</q-item-section>
              </q-item>
            </div>
          </q-list>
        </div>
      </div>
      <div class="q-pt-lg">
        <p class="text-subtitle1 text-weight-medium">Ultimas Noticias</p>
        <div class="full-width row wrap justify-between items-start content-start" v-if="news.length">
          <div class="q-pt-sm" v-for="noticia in news" :key="noticia.uuid">
            <q-card style="width: 25rem; height: 5rem">
              <q-item>
                <q-item-section avatar>
                  <q-avatar>
                    <img :src="noticia['thumbnail']['resolutions'][1]['url']">
                  </q-avatar>
                </q-item-section>
                <q-item-section>
                  <q-item-label><a :href="noticia['link']" target="_blank" class="hook">{{ noticia['title'] }}</a></q-item-label>
                  <q-item-label caption>{{ noticia['publisher'] }}</q-item-label>
                </q-item-section>
              </q-item>
            </q-card>
          </div>
        </div>
        <div v-else>
          <p>Nenhuma noticia para este ativo!</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { api } from 'src/boot/axios'
export default {
  name: 'DetailsTicker',
  data () {
    return {
      data: [],
      news: []
    }
  },
  mounted () {
    this.get_ticker_info()
    this.get_news()
  },
  methods: {
    get_ticker_info () {
      const ticker = this.$route.params.ticker
      api.get('/get-paper', { params: { ticker } })
        .then(response => {
          this.data = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    get_news () {
      const ticker = this.$route.params.ticker
      api.get('/ticket-news', { params: { ticker } })
        .then(response => {
          this.news = response.data
        })
        .catch(error => {
          console.error(error)
        })
    },
    format_price (value, quantity) {
      const val = parseInt(value).toFixed(quantity).replace('.', ',')
      if (isNaN(val)) {
        return '-'
      }
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.')
    },
    goBack () {
      this.$router.go(-1)
    }
  }
}
</script>
<style scoped>
.hook {
  text-decoration: none;
  color: black;
  cursor: pointer;
}
</style>
