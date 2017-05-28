<template>
    <div>
    <div class="row">
        <div class="col-lg-6">
                <h1 class="page-header">
                    Dashboard
                    <small>Statistics Overview</small>
                </h1>
            </div>

        <div class="col-lg-6 text-right">
          <refresh></refresh>
        </div>
    </div>
        <div class="row">
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
import Refresh from './Refresh';
import SummaryItem from './SummaryItem';

  export default {
    components: { SummaryItem, Refresh},
    data(){
      return {
        summary: {}
      }
    },

    created(){
      axios.get('/charts/summary').then(response =>{
        this.summary = response.data;
      });
    }

  }
</script>
