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
      axios.get('/charts/product_rating').then(response =>{
        this.info = response.data
      });
    }
  }
</script>
