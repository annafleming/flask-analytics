<template>
  <div>
    <div v-for="(contents, index) in summary">
      <div class="well">
          <h3>Last 7 days</h3>
          <div class="row">
              <div class="col-lg-3 col-md-6">
                  <div class="panel panel-primary">
                      <div class="panel-heading">
                          <div class="row">
                              <div class="col-xs-3">
                                  <i class="fa fa-comments fa-5x"></i>
                              </div>
                              <div class="col-xs-9 text-right">
                                  <div class="huge">{{ contents['week']['reviews'] }}</div>
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
                                  <div class="huge">{{ contents['week']['promoters'] }}</div>
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
                                  <div class="huge">{{ contents['week']['passives'] }}</div>
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
                                  <div class="huge">{{ contents['week']['detractors'] }}</div>
                                  <div>Detractors</div>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>
      <div class="well">
          <h3>Last 30 days</h3>
          <div class="row">
              <div class="col-lg-3 col-md-6">
                  <div class="panel panel-primary">
                      <div class="panel-heading">
                          <div class="row">
                              <div class="col-xs-3">
                                  <i class="fa fa-comments fa-5x"></i>
                              </div>
                              <div class="col-xs-9 text-right">
                                  <div class="huge">{{ contents['month']['reviews'] }}</div>
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
                                  <div class="huge">{{ contents['month']['promoters'] }}</div>
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
                                  <div class="huge">{{ contents['month']['passives'] }}</div>
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
                                  <div class="huge">{{ contents['month']['detractors'] }}</div>
                                  <div>Detractors</div>
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
  export default {
    data(){
      return {
        summary: {}
      }
    },

    created(){
      axios.get('/charts/summary').then(response =>{
        this.summary = response.data
      });
    }

  }
</script>
