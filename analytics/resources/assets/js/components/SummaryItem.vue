<template>
  <div>
      <div class="well">
          <h3><slot></slot></h3>
          <div class="row">
              <div class="col-lg-12">
                <div class="panel panel-primary">
                    <div class="panel-heading">
                        <div class="row">
                            <div class="col-xs-3">
                                <i class="fa fa-comments fa-4x"></i>
                            </div>
                            <div class="col-xs-9 text-right">
                                <div><span class="huge">{{ summary['reviews'] }}</span></div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-xs-12 text-right">
                                <div>Reviews</div>
                            </div>
                        </div>
                    </div>
                </div>
              </div>
          </div>
          <div class="row">
              <div class="col-lg-4">
                <summary-panel text="Promoters" icon="fa-smile-o" :value="summary['promoters']" color="green"></summary-panel>
              </div>
              <div class="col-lg-4">
                <summary-panel text="Passives" icon="fa-meh-o" :value="summary['passives']" color="yellow"></summary-panel>
              </div>
              <div class="col-lg-4">
                <summary-panel text="Detractors" icon="fa-frown-o" :value="summary['detractors']" color="red"></summary-panel>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
  import SummaryPanel from './SummaryPanel'
  export default {
    components: { SummaryPanel },
    props: [ 'summary' ],
  }
</script>
