<template>
  <div class="col-lg-12">
    <div class="table-responsive">
      <table class="table table-bordered table-hover">
          <tbody>
            <tr v-for="(value, name) in response">
              <td>{{name}}</td>
              <td>{{value}}</td>
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
        response: []
      }
    },
    mounted(){
      self = this;
      let url = '/responses/fetch/'+this.$route.params.name+'/'+this.$route.params.id;
      axios.get(url).then(response => {
        this.response = response.data;
      });
    },
  }
</script>
