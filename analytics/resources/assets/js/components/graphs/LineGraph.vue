<template>
    <canvas ref="canvas"></canvas>
</template>

<script>

  export default{
    props: [ 'labels', 'values'],
    data(){
      return {
      }
    },
    mounted(){
      let context = this.$refs.canvas.getContext('2d');
      var chartData = {
          labels: this.labels,
          datasets: [],
      };
      this.values.forEach((value, index, array) => {
        chartData.datasets.push({
          data: value ? value : [],
        });
      });
      new Chart.Line(context, {data: chartData, options:{legend:{display: false}}});
    }
  }
</script>
