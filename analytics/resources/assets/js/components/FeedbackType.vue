<template>
  <div>
    <div class="row">
      <div class="col-lg-12">
              <h1 class="page-header">
                  Charts
                  <small>Website vs Product Feedback</small>
              </h1>
        </div>
    </div>
    <div class="row" v-if="state=='fail'">
      <missing></missing>
    </div>
    <div v-if="state=='success'">
    <div class="row">
        <div class="col-lg-6">
            <div class="panel panel-primary">
                <div class="panel-heading">
                    <h3 class="panel-title">PetSafe</h3>
                </div>
                <div class="panel-body">
                  <div class="well" v-if="info.petsafe">
                    <bar-graph :labels="info.petsafe.Keys" :values="[
                    {
                      data: info.petsafe['Products'],
                      color: '#7DA3A1',
                      name: 'Products'
                    },{
                      data: info.petsafe['Website Experience'],
                      color: '#D9B44A',
                      name: 'Website Experience'
                    }]"></bar-graph>
                  </div>
                </div>
            </div>
        </div>
        <div class="col-lg-6">
            <div class="panel panel-yellow">
                <div class="panel-heading">
                    <h3 class="panel-title">SportDOG</h3>
                </div>
                <div class="panel-body">
                  <div class="well" v-if="info.sportdog">
                    <bar-graph :labels="info.sportdog.Keys" :values="[
                    {
                      data: info.sportdog['Products'],
                      color: '#7DA3A1',
                      name: 'Products'
                    },{
                      data: info.sportdog['Website Experience'],
                      color: '#D9B44A',
                      name: 'Website Experience'
                    }]"></bar-graph>
                  </div>
                </div>
            </div>
        </div>
    </div>
</div>
  </div>
</template>

<script>
import BarGraph from './graphs/BarGraph';
import Missing from './Missing';

  export default{
    components: { BarGraph, Missing },

    data(){
      return {
        info : {},
        state: 'fetching',
      }
    },
    created(){
      this.fetch();
      Event.$on('refresh', () => this.fetch());
    },

    methods: {
      fetch(){
        axios.get('/charts/feedback_type').then(response =>{
          if (response.data){
            this.info = response.data;
            this.state = 'success';
          }
          else{
            this.state = 'fail';
          }
        });
      }
    }
  }
</script>
