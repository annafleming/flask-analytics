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
    <div class="row" v-if="state=='fail'">
      <missing></missing>
    </div>
    <div v-if="state=='success'">
    <div class="row">
        <div class="col-lg-12">
            <div class="panel panel-primary">
                <div class="panel-heading">
                    <h3 class="panel-title">PetSafe</h3>
                </div>
                <div class="panel-body">
                  <div class="row">
                      <div class="col-lg-6">
                        <div class="well" v-if="info.petsafe">
                          <line-graph :labels="info.petsafe.Keys" :values="[info.petsafe.Proportion]"></line-graph>
                        </div>
                      </div>
                      <div class="col-lg-6">
                        <div class="well" v-if="info.petsafe">
                          <bar-graph :ystack="true" :labels="info.petsafe.Keys" :values="[
                          {
                            data: info.petsafe.Finished,
                            color: '#7DA3A1',
                            name: 'Finished'
                          },{
                            data: info.petsafe.Other,
                            color: '#D9B44A',
                            name: 'Total'
                          }]"></bar-graph>
                        </div>
                  </div>
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
                  <div class="row">
                      <div class="col-lg-6">
                        <div class="well" v-if="info.sportdog">
                          <line-graph :labels="info.sportdog.Keys" :values="[info.sportdog.Proportion]"></line-graph>
                        </div>
                      </div>
                      <div class="col-lg-6">
                        <div class="well" v-if="info.sportdog">
                          <bar-graph :ystack="true" :labels="info.sportdog.Keys" :values="[
                          {
                            data: info.sportdog.Finished,
                            color: '#F9DC24',
                            name: 'Finished'
                          },{
                            data: info.sportdog.Other,
                            color: '#83BA43',
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

import LineGraph from './graphs/LineGraph'
import BarGraph from './graphs/BarGraph'
import Missing from './Missing';

  export default{
    components: { LineGraph, BarGraph, Missing },

    data(){
      return {
        info : {},
        state: 'fetching',
      }
    },
    created(){
      axios.get('/charts/finished').then(response =>{
        if (response.data){
          this.info = response.data;
          this.state = 'success';
        }
        else{
          this.state = 'fail';
        }
      });
    },
  }
</script>
