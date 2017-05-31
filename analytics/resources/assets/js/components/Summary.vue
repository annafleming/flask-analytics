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
                <div class="panel panel-petsafe">
                    <div class="panel-heading">
                        <h3 class="panel-title">PetSafe</h3>
                    </div>
                    <div class="panel-body" v-if="info.petsafe && info.petsafe.week">
                        <summary-item :summary="info.petsafe.week" header>Last 7 days</summary-item>
                    </div>

                    <div class="panel-body" v-if="info.petsafe && info.petsafe.month">
                        <summary-item :summary="info.petsafe.month">Last 30 days</summary-item>
                    </div>
                </div>
            </div>

            <div class="col-lg-6">
                <div class="panel panel-sportdog">
                    <div class="panel-heading">
                        <h3 class="panel-title">SportDOG</h3>
                    </div>
                    <div class="panel-body" v-if="info.sportdog && info.sportdog.week">
                        <summary-item :summary="info.sportdog.week" header>Last 7 days</summary-item>
                    </div>

                    <div class="panel-body" v-if="info.sportdog && info.sportdog.month">
                        <summary-item :summary="info.sportdog.month">Last 30 days</summary-item>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import SummaryItem from './SummaryItem';
import ChartAbstract from './ChartAbstract';

  export default {
    extends: ChartAbstract,
    components: { SummaryItem},
    data(){
      return {
        apiRoute: '/charts/summary',
      }
    },
  }
</script>
