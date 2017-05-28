<template>
  <button type="button" class="btn btn-link navbar-brand" v-on:click="refresh">{{ text }}</button>
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
