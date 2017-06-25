<template>
  <div class="row">
      <div class="col-lg-12 text-right refresh">
        <span>{{ updatedMessage }}</span>
        <button type="button" class="btn btn-update" v-on:click="refresh">{{ text }}</button>
      </div>
  </div>
</template>

<script>
  export default {
    data(){
      return {
        updated: '',
        text: 'Update',
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
        axios.get('/refresh/').then(response => {
          this.text = 'Update';
          this.updated = response.data;
          Event.$emit('refresh');
        }).catch(e => {
          this.text = 'Update';
          alert('Failed to update data. Please, try again later.');
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
