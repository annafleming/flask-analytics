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
      axios.get('/charts/finished').then(response =>{
        this.info = response.data
      });
    }
  }
</script>
