<template>
    <canvas ref="canvas"></canvas>
</template>

<script>
  import GraphAbstract from './GraphAbstract'
  export default{
    extends: GraphAbstract,
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
      return {
      }
    },
    mounted(){
      let self = this;

      let options = this.getChartOptions();
      if (!options['legend']){
        options['legend'] = {};
      }
      options['legend']['display'] = false;


      if (this.yrewrites) {
        options['scales']['yAxes'][0]['ticks'] = {
            max: Math.max(...Object.keys(self.yrewrites)),
            callback: function(value, index, values) {
              return (self.yrewrites[value]) ? self.yrewrites[value] : '';
            }
        }
      }

      if (this.ymax){
        options['scales']['yAxes'][0]['ticks'] = {
            max: this.ymax
        }
      }

      let chartData = this.getChartData();
      this.values.forEach((value, index, array) => {
        chartData.datasets.push({
          data: value ? value : [],
          backgroundColor: 'rgba(52, 152, 219, .5)',
          borderColor: 'rgba(34, 34, 17, .5)',
        });
      });
      new Chart.Line(this.getContext(), {data: chartData, options: options});
    },
  }
</script>
