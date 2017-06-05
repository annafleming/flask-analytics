<template>
  <div>
    <div class="row">
      <div class="col-lg-12">
              <h1 class="page-header">
                  Charts
                  <small>Customers Completed Purpose of the Visit</small>
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
                        <div class="well" v-if="info.petsafe">
                          <line-graph :labels="info.petsafe.Keys" :values="[info.petsafe.Proportion]" :ymax="100"  ylabel="Reviews, %"></line-graph>
                        </div>
                      </div>
                  </div>
                  <div class="row">
                      <div class="col-lg-12">
                        <div class="well" v-if="info.petsafe">
                          <bar-graph :stacked="true" :labels="info.petsafe.Keys"  ylabel="Reviews" :values="[
                          {
                            data: info.petsafe.CompletedPurpose,
                            color: '#3498db',
                            name: 'Completed Purpose'
                          },{
                            data: info.petsafe.Other,
                            color: '#f1c40f',
                            name: 'Total'
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
                        <div class="well" v-if="info.sportdog">
                          <line-graph :labels="info.sportdog.Keys" :values="[info.sportdog.Proportion]"  ylabel="Reviews, %" :ymax="100"></line-graph>
                        </div>
                      </div>
                 </div>
                 <div class="row">
                      <div class="col-lg-12">
                        <div class="well" v-if="info.sportdog">
                          <bar-graph :stacked="true" :labels="info.sportdog.Keys"  ylabel="Reviews" :values="[
                          {
                            data: info.sportdog.CompletedPurpose,
                            color: '#3498db',
                            name: 'Completed Purpose'
                          },{
                            data: info.sportdog.Other,
                            color: '#f1c40f',
                            name: 'Total'
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
        apiRoute: '/charts/completed',
      }
    },
  }
</script>
