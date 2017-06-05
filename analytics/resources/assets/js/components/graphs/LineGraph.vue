<template>
    <canvas ref="canvas"></canvas>
</template>

<script>

  export default{
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
      let options = {
        legend:{
          display: false
        }
      };
      if (this.yrewrites){
        options['scales'] = {
            yAxes: [{
                    ticks: {
                        max: Math.max(...Object.keys(self.yrewrites)),
                        callback: function(value, index, values) {
                          return (self.yrewrites[value]) ? self.yrewrites[value] : '';
                        }
                    }
                }
            ]
        }
      }

      if (this.ymax){
        options['scales'] = {
            yAxes: [{
                    ticks: {
                        max: this.ymax
                    }
                }
            ]
        }
      }

      if (this.ylabel){
        if (!options['scales']){
          options['scales'] = {};
        }
        if (!options['scales']['yAxes']){
          options['scales']['yAxes'] = [{}]
        }
        options['scales']['yAxes'][0]['scaleLabel'] = {
          display: true,
          labelString: this.ylabel,
        }
      }

      if (this.xlabel){
        if (!options['scales']){
          options['scales'] = {};
        }
        if (!options['scales']['xAxes']){
          options['scales']['xAxes'] = [{}]
        }
        options['scales']['xAxes'][0]['scaleLabel'] = {
          display: true,
          labelString: this.xlabel,
        }
      }

      let chartData = {
          labels: this.labels,
          datasets: [],
      };

      this.values.forEach((value, index, array) => {
        chartData.datasets.push({
          data: value ? value : [],
          backgroundColor: 'rgba(52, 152, 219, .5)',
          borderColor: 'rgba(34, 34, 17, .5)',
        });
      });
      new Chart.Line(this.$refs.canvas.getContext('2d'), {data: chartData, options: options});
    }
  }
</script>
