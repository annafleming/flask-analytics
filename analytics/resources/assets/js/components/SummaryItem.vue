<template>
  <div>
      <div class="well">
          <h3><slot></slot></h3>
          <div class="row">
              <div class="col-lg-3 col-md-6">
                <summary-panel text="Reviews" icon="fa-comments" :value="summary['reviews']" color="primary"></summary-panel>
              </div>
              <div class="col-lg-3 col-md-6">
                <summary-panel text="Promoters" icon="fa-smile-o" :value="summary['promoters']" color="green"></summary-panel>
              </div>
              <div class="col-lg-3 col-md-6">
                <summary-panel text="Passives" icon="fa-meh-o" :value="summary['passives']" color="yellow"></summary-panel>
              </div>
              <div class="col-lg-3 col-md-6">
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
