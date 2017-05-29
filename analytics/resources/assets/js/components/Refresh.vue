<template>
  <div class="row">
      <div class="col-lg-12 text-right refresh">
        <span>{{ updatedMessage }}</span>
        <button type="button" class="btn btn-success" v-on:click="refresh">{{ text }}</button>
      </div>
  </div>
</template>

<script>
  export default {
    data(){
      return {
        updated: '',
        text: 'Refresh',
      }
    },
    created(){
      axios.get('/refresh/last_updated').then(response => {
        this.updated = response.data;
        Event.$emit('refresh');
      });
    },
    methods: {
      refresh(){
        this.text = 'In Progress...';
        axios.get('/refresh').then(response => {
          this.text = 'Refresh';
          this.updated = response.data;
          Event.$emit('refresh');
        });
      }
    },
    computed:{
      updatedMessage(){
        return (this.updated) ? `Updated ${Moment(this.updated, 'X').fromNow()}` : '';
      }
    }
  }
</script>
