<template>
  <h1>{{ heading }}</h1>
</template>

<script>
  export default {
    data(){
      return {
        heading : ''
      }
    },
    mounted(){
      axios.get('/responses/fetch/'+this.$route.params.name).then(response => {
        this.heading = response.data;
      });
    },
  }
</script>
