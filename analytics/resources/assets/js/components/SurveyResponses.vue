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
          </tr>
        </thead>
        <tbody>
          <tr v-for="survey_response in survey_responses">
            <td v-for="column in columns">
              {{ survey_response[column] }}
            </td>
            {{column}}
          </tr>
        </tbody>
      </table>
    </div>
    <div>
      <ul class="pagination">
        <li class="page-item"><a class="page-link" v-on:click="previous">Previous</a></li>
        <li class="page-item"><a class="page-link" v-on:click="next">Next</a></li>
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
        });
      },
      next(){
        this.currentPage += 1;
        this.fetch();
      },
      previous(){
        if (this.currentPage > 1){
          this.currentPage -= 1;
          this.fetch();
        }
      }
    }
  }
</script>
