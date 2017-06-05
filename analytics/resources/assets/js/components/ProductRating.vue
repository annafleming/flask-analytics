<template>
  <div>
    <div class="row">
      <div class="col-lg-12">
              <h1 class="page-header">
                  Charts
                  <small>Product Rating</small>
              </h1>
        </div>
    </div>
    <div class="row" v-if="state=='fail'">
      <missing></missing>
    </div>
    <div v-if="state=='success'">
    <div class="row">
        <div class="col-lg-6">
            <div class="panel panel-petsafe">
                <div class="panel-heading">
                    <h3 class="panel-title">PetSafe</h3>
                </div>
                <div class="panel-body">
                  <div class="row">
                    <div class="col-lg-12">
                    <div class="well" v-if="info.petsafe && info.petsafe.Keys && info.petsafe.Average">
                      <line-graph :labels="info.petsafe.Keys" :values="[info.petsafe.Average]" :ymax="10" ylabel="Rating"></line-graph>
                    </div>
                    </div>
                    </div>
                    <div class="row">
                    <div class="col-lg-12">
                    <div class="well" v-if="info.petsafe && info.petsafe.Keys">
                      <bar-graph :stacked="true" :labels="info.petsafe.Keys" ylabel="Reviews" :values="[
                      {
                        data: info.petsafe['Detractors'],
                        color: '#c74c3c',
                        name: 'Detractors'
                      },
                      {
                        data: info.petsafe['Passives'],
                        color: '#f1c40f',
                        name: 'Passives'
                      },
                      {
                        data: info.petsafe['Promoters'],
                        color: '#77933C',
                        name: 'Promoters'
                      }]"></bar-graph>
                    </div>
                  </div>
                  </div>
                </div>
            </div>
        </div>

        <div class="col-lg-6">
            <div class="panel panel-sportdog">
                <div class="panel-heading">
                    <h3 class="panel-title">SportDOG</h3>
                </div>
                <div class="panel-body">
                  <div class="row">
                    <div class="col-lg-12">
                    <div class="well" v-if="info.sportdog && info.sportdog.Keys && info.sportdog.Average">
                      <line-graph :labels="info.sportdog.Keys" :values="[info.sportdog.Average]" :ymax="10" ylabel="Rating"></line-graph>
                    </div>
                    </div>
                    </div>
                    <div class="row">
                    <div class="col-lg-12">
                    <div class="well" v-if="info.sportdog && info.sportdog.Keys">
                      <bar-graph :stacked="true" :labels="info.sportdog.Keys" ylabel="Reviews" :values="[
                      {
                        data: info.sportdog['Detractors'],
                        color: '#c74c3c',
                        name: 'Detractors'
                      },
                      {
                        data: info.sportdog['Passives'],
                        color: '#f1c40f',
                        name: 'Passives'
                      },
                      {
                        data: info.sportdog['Promoters'],
                        color: '#77933C',
                        name: 'Promoters'
                      }]"></bar-graph>
                </div>
              </div>
              </div>
                </div>
            </div>
        </div>
    </div>
  </div>

  </div>
</template>

<script>

import ChartAbstract from './ChartAbstract';
import LineGraph from './graphs/LineGraph'
import BarGraph from './graphs/BarGraph'

  export default {
    extends: ChartAbstract,
    components: { LineGraph, BarGraph},
    data(){
      return {
        apiRoute: '/charts/product_rating',
      }
    },
  }
</script>
