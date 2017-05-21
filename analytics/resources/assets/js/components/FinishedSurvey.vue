<template>
  <div>
    <div class="row">
      <div class="col-lg-12">
              <h1 class="page-header">
                  Charts
                  <small>Customers Finished the Survey</small>
              </h1>
        </div>
    </div>
    <div class="row">
        <div class="col-lg-12">
            <div class="panel panel-primary">
                <div class="panel-heading">
                    <h3 class="panel-title">PetSafe</h3>
                </div>
                <div class="panel-body">
                    <div class="well" v-if="info.petsafe && info.petsafe.Keys && info.petsafe.Proportion">
                      <line-graph :labels="info.petsafe.Keys" :values="[info.petsafe.Proportion]"></line-graph>
                    </div>
                    <div class="well" v-if="info.petsafe && info.petsafe.Keys && info.petsafe.Finished">
                      <bar-graph :labels="info.petsafe.Keys"
                      :values="[info.petsafe.Total, info.petsafe.Finished]"
                      :colors="['#D3C4BE', '#EBCFC4']"
                      :names="['Total', 'Finished']"></bar-graph>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="row">
        <div class="col-lg-12">
            <div class="panel panel-yellow">
                <div class="panel-heading">
                    <h3 class="panel-title">SportDOG</h3>
                </div>
                <div class="panel-body">
                    <div class="well" v-if="info.sportdog && info.sportdog.Keys && info.sportdog.Proportion">
                      <line-graph :labels="info.sportdog.Keys" :values="[info.sportdog.Proportion]"></line-graph>
                    </div>
                    <div class="well" v-if="info.sportdog && info.sportdog.Keys && info.sportdog.Finished">
                      <bar-graph :labels="info.sportdog.Keys"
                      :values="[info.sportdog.Total, info.sportdog.Finished]"
                      :colors="['#D3C4BE', '#F4DAC2']"
                      :names="['Total', 'Finished']"></bar-graph>
                    </div>
                </div>
            </div>
        </div>
    </div>

  </div>
</template>

<script>

import LineGraph from './graphs/LineGraph'
import BarGraph from './graphs/BarGraph'

  export default{
    components: { LineGraph, BarGraph },

    data(){
      return {
        info : {}
      }
    },
    created(){
      axios.get('/charts/finished').then(response =>{
        this.info = response.data
      });
    }
  }
</script>
