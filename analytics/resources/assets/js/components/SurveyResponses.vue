<template>
  <div>


  <h1>Survey responses for {{ $route.params.name }}</h1>
  <div class="col-lg-12 text-right">
    <span class="badge badge-default">Page {{ currentPage }}</span>
  </div>
  <div class="col-lg-12">
  <div class="table-responsive">
    <table class="table table-bordered table-hover">
        <thead>
          <tr>
            <th v-for="column in columns">
              {{ column }}
            </th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="survey_response in survey_responses">
            <td v-for="column in columns">
              {{ survey_response[column] }}
            </td>
            <td>
              <router-link :to="{ path: $route.params.name+'/'+survey_response['_id']['$oid'] }">View</router-link></td>
            {{column}}
          </tr>
        </tbody>
      </table>
    </div>
    <div>
      <ul class="pagination">
        <li v-bind:class="[{ 'disabled': currentPage == 1 }, 'page-item']"><a class="page-link" v-on:click="previous">Previous</a></li>
        <li v-bind:class="[{ 'disabled': currentPage == totalPages }, 'page-item']"><a class="page-link" v-on:click="next">Next</a></li>
      </ul>
    </div>
  </div>
</div>
</template>

<script>
  export default {
    data(){
      return {
        survey_responses : [],
        columns: [],
        column: '',
        currentPage: 1,
        limit: 5,
        total: 1
      }
    },
    mounted(){
      this.fetch();
    },
    methods:{
      fetch(){
        self = this;
        let url = '/responses/fetch/'+this.$route.params.name+'?page='+this.currentPage+'&limit='+this.limit;
        axios.get(url).then(response => {
          self.survey_responses = response.data.survey_responses;
          self.columns = response.data.columns;
          this.total = response.data.total;
        });
      },
      next(){
        if (this.currentPage < this.totalPages){
          this.currentPage += 1;
          this.fetch();
        }
      },
      previous(){
        if (this.currentPage > 1){
          this.currentPage -= 1;
          this.fetch();
        }
      }
    },
    computed:{
      totalPages(){
        return Math.ceil(this.total/this.limit);
      }
    },
    watch: {
      '$route.params.name'(newId, oldId) {
          this.fetch();
        }
    }
  }
</script>
