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
      axios.get('/charts/feedback_type').then(response =>{
        this.info = response.data
      });
    }
  }
</script>
