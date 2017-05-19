<template>
  <div>
    {{ info }}
  </div>
</template>

<script>
  export default{
    data(){
      return {
        info : {}
      }
    },
    created(){
      axios.get('/charts/completed').then(response =>{
        this.info = response.data
      });
    }
  }
</script>
