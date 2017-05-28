<template>
  <button type="button" class="btn btn-lg btn-info" v-on:click="refresh">{{ text }}</button>
</template>

<script>
  export default {
    data(){
      return {
        text: 'Refresh'
      }
    },
    methods: {
      refresh(){
        this.text = 'In Progress...';
        axios.get('/refresh').then(response => {
          this.text = 'Refresh';
        });
      }
    }
  }
</script>
