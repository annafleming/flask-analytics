<template>
  <div>
      <div class="well">
          <h3><slot></slot></h3>
          <div class="row">
              <div class="col-lg-3 col-md-6">
                  <div class="panel panel-primary">
                      <div class="panel-heading">
                          <div class="row">
                              <div class="col-xs-3">
                                  <i class="fa fa-comments fa-5x"></i>
                              </div>
                              <div class="col-xs-9 text-right">
                                  <div class="huge">{{ summary['reviews'] }}</div>
                                  <div>New Reviews</div>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
              <div class="col-lg-3 col-md-6">
                  <div class="panel panel-green">
                      <div class="panel-heading">
                          <div class="row">
                              <div class="col-xs-3">
                                  <i class="fa fa-thumbs-o-up fa-5x"></i>
                              </div>
                              <div class="col-xs-9 text-right">
                                  <div class="huge">{{ summary['promoters'] }}</div>
                                  <div>Promoters</div>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
              <div class="col-lg-3 col-md-6">
                  <div class="panel panel-yellow">
                      <div class="panel-heading">
                          <div class="row">
                              <div class="col-xs-3">
                                  <i class="fa fa-meh-o fa-5x"></i>
                              </div>
                              <div class="col-xs-9 text-right">
                                  <div class="huge">{{ summary['passives'] }}</div>
                                  <div>Passives</div>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
              <div class="col-lg-3 col-md-6">
                  <div class="panel panel-red">
                      <div class="panel-heading">
                          <div class="row">
                              <div class="col-xs-3">
                                  <i class="fa fa-thumbs-o-down fa-5x"></i>
                              </div>
                              <div class="col-xs-9 text-right">
                                  <div class="huge">{{ summary['detractors'] }}</div>
                                  <div>Detractors</div>
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
  export default {
    props: [ 'summary' ]
  }
</script>
