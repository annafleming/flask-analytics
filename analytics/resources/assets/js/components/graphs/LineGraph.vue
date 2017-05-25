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

      let chartData = {
          labels: this.labels,
          datasets: [],
      };

      this.values.forEach((value, index, array) => {
        chartData.datasets.push({
          data: value ? value : [],
        });
      });
      new Chart.Line(this.$refs.canvas.getContext('2d'), {data: chartData, options: options});
    }
  }
</script>
