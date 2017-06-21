<template>
  <div>


  <h1>Survey responses for {{ $route.params.name }}</h1>
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
  </div>
</template>

<script>
  export default {
    data(){
      return {
        survey_responses : [],
        columns: [],
        column: '',
      }
    },
    mounted(){
      self = this;
      axios.get('/responses/fetch/'+this.$route.params.name).then(response => {
        self.survey_responses = response.data.survey_responses;
        self.columns = response.data.columns;
      });
    },
  }
</script>
