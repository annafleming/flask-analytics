<template>
  <div>
    <div class="row">
      <div class="col-lg-12">
              <h1 class="page-header">
                  Charts
                  <small>Website Rating</small>
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
                    <div class="well" v-if="info.petsafe && info.petsafe.Keys && info.petsafe.Average">
                      <line-graph :labels="info.petsafe.Keys"
                      :values="[info.petsafe.Average]"
                      :yrewrites="{
                        1: 'Very Bad',
                        2: 'Bad',
                        3: 'Fair',
                        4: 'Good',
                        5: 'Very Good'
                      }"></line-graph>
                    </div>
                    <!-- <div class="well" v-if="info.petsafe && info.petsafe.Keys && info.petsafe.Finished">
                      <bar-graph :labels="info.petsafe.Keys" :values="[
                      {
                        data: info.petsafe.Total,
                        color: '#D3C4BE',
                        name: 'Total'
                      },{
                        data: info.petsafe.Finished,
                        color: '#F4DAC2',
                        name: 'Finished'
                      }]"></bar-graph>
                    </div> -->
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
                    <div class="well" v-if="info.sportdog && info.sportdog.Keys && info.sportdog.Average">
                      <line-graph :labels="info.sportdog.Keys"
                      :values="[info.sportdog.Average]"
                      :yrewrites="{
                        1: 'Very Bad',
                        2: 'Bad',
                        3: 'Fair',
                        4: 'Good',
                        5: 'Very Good'
                      }"></line-graph>
                    </div>
                    <!-- <div class="well" v-if="info.sportdog && info.sportdog.Keys && info.sportdog.Finished">
                      <bar-graph :labels="info.sportdog.Keys" :values="[
                      {
                        data: info.sportdog.Total,
                        color: '#D3C4BE',
                        name: 'Total'
                      },{
                        data: info.sportdog.Finished,
                        color: '#EBCFC4',
                        name: 'Finished'
                      }]"></bar-graph>
                    </div> -->
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
      axios.get('/charts/website_rating').then(response =>{
        this.info = response.data
      });
    },
  }
</script>
