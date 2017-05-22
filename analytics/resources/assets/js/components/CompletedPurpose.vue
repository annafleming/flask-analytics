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
                    <div class="well" v-if="info.petsafe && info.petsafe.Keys && info.petsafe.CompletedPurpose">
                      <bar-graph :labels="info.sportdog.Keys" :values="[
                      {
                        data: info.petsafe.Total,
                        color: '#D3C4BE',
                        name: 'Total'
                      },{
                        data: info.petsafe.CompletedPurpose,
                        color: '#EBCFC4',
                        name: 'CompletedPurpose'
                      }]"></bar-graph>
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
                    <div class="well" v-if="info.sportdog && info.sportdog.Keys && info.sportdog.CompletedPurpose">
                      <bar-graph :labels="info.sportdog.Keys" :values="[
                      {
                        data: info.sportdog.Total,
                        color: '#D3C4BE',
                        name: 'Total'
                      },{
                        data: info.sportdog.CompletedPurpose,
                        color: '#EBCFC4',
                        name: 'CompletedPurpose'
                      }]"></bar-graph>
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
      axios.get('/charts/completed').then(response =>{
        this.info = response.data
      });
    }
  }
</script>
