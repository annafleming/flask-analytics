<template>
    <div>
    </div>
</template>

<script>

  export default {
    props: {
      labels: Array,
      values: Array,
      yrewrites: {
        type: Object,
        required: false
      },
      ymax:{
        required: false
      },
      ylabel:{
        required: false
      },
      xlabel:{
        required: false
      }
    },
    data(){
      return {}
    },

    methods: {
      getContext(){
        return this.$refs.canvas.getContext('2d');
      },
      getChartData(){
        return {
            labels: this.labels,
            datasets: [],
        };
      },
      getChartOptions(){
        return {
          scales: {
            xAxes:[{
              scaleLabel: {
                display: this.xlabel ? true : false,
                labelString: this.xlabel ? this.xlabel : '',
              }
            }],
            yAxes:[{
              scaleLabel: {
                display: this.ylabel ? true : false,
                labelString: this.ylabel ? this.ylabel : '',
              }
            }],
          }
        };
      }
    }
  }
</script>
