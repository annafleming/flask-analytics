<template>
    <canvas ref="canvas"></canvas>
</template>

<script>
  import GraphAbstract from './GraphAbstract'
  export default{
    extends: GraphAbstract,
    props: {
      stacked: {
        type: Boolean,
        default: false,
      },
    },

    data(){
      return {}
    },
    mounted(){
      let options = this.getChartOptions();
      options['scales']['yAxes'][0]['stacked'] = this.stacked;
      options['scales']['xAxes'][0]['stacked'] = this.stacked;

      let chartData = this.getChartData();

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

      new Chart(this.getContext(), {
        type: 'bar',
        data: chartData,
        options: options,
      });
    }
  }
</script>
