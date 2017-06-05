<template>
    <canvas ref="canvas"></canvas>
</template>

<script>

  export default{
    props: {
      labels: Array,
      values: Array,
      stacked: {
        type: Boolean,
        default: false,
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
      let options = {
        scales: {
            yAxes: [{
                stacked: this.stacked,
            }],
            xAxes: [{
                stacked: this.stacked,
            }]
        }
      };

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

      let context = this.$refs.canvas.getContext('2d');
      var chartData = {
          labels: this.labels,
          datasets: []
      };

      this.values.forEach((values, index, array) => {
        let dataset = {
          data: values.data,
        };
        if (values['color']){
          dataset['backgroundColor'] = values['color'];
        }
        if (values['name']){
          dataset['label'] = values['name'];
        }
        chartData.datasets.push(dataset);
      });

      new Chart(context, {
        type: 'bar',
        data: chartData,
        options: options,
      });
    }
  }
</script>
