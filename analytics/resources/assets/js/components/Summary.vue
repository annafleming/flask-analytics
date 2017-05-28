<template>
    <div>
    <div class="row">
        <div class="col-lg-12">
                <h1 class="page-header">
                    Dashboard
                    <small>Statistics Overview</small>
                </h1>
        </div>
    </div>
      <div class="row" v-if="state=='fail'">
        <missing></missing>
      </div>
        <div class="row" v-if="state=='success'">
            <div class="col-lg-6">
                <div class="panel panel-primary">
                    <div class="panel-heading">
                        <h3 class="panel-title">PetSafe</h3>
                    </div>
                    <div class="panel-body" v-if="summary.petsafe && summary.petsafe.week">
                        <summary-item :summary="summary.petsafe.week" header>Last 7 days</summary-item>
                    </div>

                    <div class="panel-body" v-if="summary.petsafe && summary.petsafe.month">
                        <summary-item :summary="summary.petsafe.month">Last 30 days</summary-item>
                    </div>
                </div>
            </div>

            <div class="col-lg-6">
                <div class="panel panel-yellow">
                    <div class="panel-heading">
                        <h3 class="panel-title">SportDOG</h3>
                    </div>
                    <div class="panel-body" v-if="summary.sportdog && summary.sportdog.week">
                        <summary-item :summary="summary.sportdog.week" header>Last 7 days</summary-item>
                    </div>

                    <div class="panel-body" v-if="summary.sportdog && summary.sportdog.month">
                        <summary-item :summary="summary.sportdog.month">Last 30 days</summary-item>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import SummaryItem from './SummaryItem';
import Missing from './Missing';

  export default {
    components: { SummaryItem, Missing},
    data(){
      return {
        summary: {},
        state: 'fetching',
      }
    },

    created(){
      axios.get('/charts/summary').then(response =>{
        if (response.data){
          this.summary = response.data;
          this.state = 'success';
          console.log('success');
        }
        else{
          this.state = 'fail';
          console.log('fail');
        }

      });
    }

  }
</script>
