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
                      <line-graph :labels="info.petsafe.Keys"
                      :values="[info.petsafe.Average]"
                      ylabel="Rating"
                      :yrewrites="{
                        1: 'Very Bad',
                        2: 'Bad',
                        3: 'Fair',
                        4: 'Good',
                        5: 'Very Good'
                      }"></line-graph>
                    </div>
                    </div>
                    </div>
                    <div class="row">
                    <div class="col-lg-12">
                    <div class="well" v-if="info.petsafe && info.petsafe.Keys">
                      <bar-graph :stacked="true" :labels="info.petsafe.Keys" ylabel="Reviews" :values="[
                      {
                        data: info.petsafe['Very Bad'],
                        color: '#C0504D',
                        name: 'Very Bad'
                      },
                      {
                        data: info.petsafe['Bad'],
                        color: '#D99694',
                        name: 'Bad'
                      },
                      {
                        data: info.petsafe['Fair'],
                        color: '#FFC000',
                        name: 'Fair'
                      },
                      {
                        data: info.petsafe['Good'],
                        color: '#77933C',
                        name: 'Good'
                      },
                      {
                        data: info.petsafe['Very Good'],
                        color: '#4F6228',
                        name: 'Very Good'
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
                      <line-graph :labels="info.sportdog.Keys"
                      :values="[info.sportdog.Average]"
                      ylabel="Rating"
                      :yrewrites="{
                        1: 'Very Bad',
                        2: 'Bad',
                        3: 'Fair',
                        4: 'Good',
                        5: 'Very Good'
                      }"></line-graph>
                    </div>
                    </div>
                    </div>
                    <div class="row">
                    <div class="col-lg-12">
                    <div class="well" v-if="info.sportdog && info.sportdog.Keys">
                    <bar-graph :stacked="true" :labels="info.sportdog.Keys" ylabel="Reviews" :values="[
                    {
                      data: info.sportdog['Very Bad'],
                      color: '#C0504D',
                      name: 'Very Bad'
                    },
                    {
                      data: info.sportdog['Bad'],
                      color: '#D99694',
                      name: 'Bad'
                    },
                    {
                      data: info.sportdog['Fair'],
                      color: '#FFC000',
                      name: 'Fair'
                    },
                    {
                      data: info.sportdog['Good'],
                      color: '#77933C',
                      name: 'Good'
                    },
                    {
                      data: info.sportdog['Very Good'],
                      color: '#4F6228',
                      name: 'Very Good'
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
        apiRoute: '/charts/website_rating',
      }
    },
  }
</script>
