<template>
  <h1>Survey responses for {{ $route.params.name }}</h1>
</template>

<script>
  export default {
    data(){
      return {
        data : ''
      }
    },
    mounted(){
      axios.get('/responses/fetch/'+this.$route.params.name).then(response => {
        this.data = response.data;
      });
    },
  }
</script>
