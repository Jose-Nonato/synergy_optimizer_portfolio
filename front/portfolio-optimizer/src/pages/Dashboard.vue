<template>
  <div class="q-pa-lg">
    <q-table
    flat
    bordered
    :rows="tickers"
    :columns="cols"
    :visible-columns="visibleColumns"
    :filter="searchInput"
    >
    <template v-slot:top>
        <div class="text-subtitle1 q-pa-md">Recomendações de Ativos</div>
        <q-space />
        <q-input
          v-model="searchInput"
          class="q-pr-md"
          outlined
          dense
          placeholder="Procurar por"
        >
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
        <q-select
          v-model="visibleColumns"
          multiple
          outlined
          dense
          options-dense
          :display-value="$q.lang.table.columns"
          emit-value
          map-options
          :options="cols"
          option-value="name"
          options-cover
        />
      </template>
    </q-table>
  </div>
</template>
<script>
import { api } from 'src/boot/axios'
export default {
  name: 'DashboardAssets',
  data () {
    return {
      message: 'Dashboard',
      tickers: [],
      cols: [
        { name: 'papel', label: 'Papel', field: 'papel', align: 'left' },
        { name: 'cotacao', label: 'Cotação', field: 'cotacao', align: 'left', sortable: true },
        { name: 'pl', label: 'P/L', field: 'pl', align: 'left', sortable: true },
        { name: 'pvp', label: 'P/VP', field: 'pvp', align: 'left', sortable: true },
        { name: 'psr', label: 'PSR', field: 'psr', align: 'left', sortable: true },
        { name: 'dy', label: 'Div. Yield', field: 'dy', align: 'left', sortable: true },
        { name: 'pa', label: 'P. Ativo', field: 'pa', align: 'left', sortable: true },
        { name: 'pcg', label: 'P/Cap. Giro', field: 'pcg', align: 'left', sortable: true },
        { name: 'pebit', label: 'P/EBIT', field: 'pebit', align: 'left', sortable: true },
        { name: 'pacl', label: 'P/Ativ. Cir. Liq', field: 'pacl', align: 'left', sortable: true },
        { name: 'evebit', label: 'EV/EBIT', field: 'evebit', align: 'left', sortable: true },
        { name: 'evebitda', label: 'EV/EBITDA', field: 'evebitda', align: 'left', sortable: true },
        { name: 'mrgebit', label: 'Mrg Ebit', field: 'mrgebit', align: 'left', sortable: true },
        { name: 'mrgliq', label: 'Mrg Líq', field: 'mrgliq', align: 'left', sortable: true },
        { name: 'roic', label: 'ROIC', field: 'roic', align: 'left', sortable: true },
        { name: 'roe', label: 'ROE', field: 'roe', align: 'left', sortable: true },
        { name: 'liqc', label: 'Liq. Corr', field: 'liqc', align: 'left', sortable: true },
        { name: 'liq2m', label: 'Liq. 2 Meses', field: 'liq2m', align: 'left', sortable: true },
        { name: 'patrliq', label: 'Patrim. Líq.', field: 'patrliq', align: 'left', sortable: true },
        { name: 'divbpatr', label: 'Dív. Brut/Patrim', field: 'divbpatr', align: 'left', sortable: true },
        { name: 'c5y', label: 'Cresc. Rec. 5a', field: 'c5y', align: 'left', sortable: true }
      ],
      visibleColumns: ['papel', 'cotacao', 'pl', 'pvp', 'psr', 'dy', 'pa', 'pcg', 'pebit', 'pacl', 'evebit', 'evebitda', 'mrgebit', 'mrgliq', 'roic', 'roe', 'liqc', 'liq2m', 'patrliq', 'divbpatr', 'c5y'],
      searchInput: ''
    }
  },
  mounted () {
    this.get_data_tickers()
  },
  methods: {
    get_data_tickers () {
      api.get('/all-tickers')
        .then(response => {
          console.log(typeof response.data)
          console.log(typeof this.cols)
          this.tickers = response.data
        })
        .catch(error => {
          console.error('Erro ao pegar os dados de ticker:', error)
        })
    }
  }
}
</script>
