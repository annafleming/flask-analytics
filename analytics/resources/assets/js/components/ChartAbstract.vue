<template>
    <div>
    </div>
</template>

<script>

import Missing from './Missing';

  export default {
    components: { Missing },
    data(){
      return {
        summary: {},
        state: 'fetching',
        apiRoute: '',
      }
    },

    created(){
      this.fetch();
      Event.$on('refresh', () => this.fetch());
    },

    methods: {
      fetch(){
        axios.get(this.apiRoute).then(response =>{
          if (response.data){
            this.info = response.data;
            this.state = 'success';
          }
          else{
            this.state = 'fail';
          }
        });
      }
    }
  }
</script>
