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
    <div class="row">
        <div class="col-lg-12">
            <div class="panel panel-primary">
                <div class="panel-heading">
                    <h3 class="panel-title">PetSafe</h3>
                </div>
                <div class="panel-body">
                    <div class="well" v-if="info.petsafe && info.petsafe.Keys && info.petsafe.Average">
                      <line-graph :labels="info.petsafe.Keys" :values="[info.petsafe.Average]" :ymax="10"></line-graph>
                    </div>
                    <div class="well" v-if="info.petsafe && info.petsafe.Keys">
                      <bar-graph :ystack="true" :labels="info.petsafe.Keys" :values="[
                      {
                        data: info.petsafe['Detractors'],
                        color: '#C0504D',
                        name: 'Detractors'
                      },
                      {
                        data: info.petsafe['Passives'],
                        color: '#FFC000',
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

    <div class="row">
        <div class="col-lg-12">
            <div class="panel panel-yellow">
                <div class="panel-heading">
                    <h3 class="panel-title">SportDOG</h3>
                </div>
                <!-- <div class="panel-body"> -->
                    <div class="well" v-if="info.sportdog && info.sportdog.Keys && info.sportdog.Average">
                      <line-graph :labels="info.sportdog.Keys" :values="[info.sportdog.Average]" :ymax="10"></line-graph>
                    </div>
                    <div class="well" v-if="info.sportdog && info.sportdog.Keys">
                      <bar-graph :ystack="true" :labels="info.sportdog.Keys" :values="[
                      {
                        data: info.sportdog['Detractors'],
                        color: '#C0504D',
                        name: 'Detractors'
                      },
                      {
                        data: info.sportdog['Passives'],
                        color: '#FFC000',
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
      axios.get('/charts/product_rating').then(response =>{
        this.info = response.data
      });
    },
  }
</script>
