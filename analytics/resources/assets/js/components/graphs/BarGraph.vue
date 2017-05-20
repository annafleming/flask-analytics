<template>
    <canvas ref="canvas"></canvas>
</template>

<script>

  export default{
    props: [ 'labels', 'values', 'colors', 'names'],
    data(){
      return {
      }
    },
    mounted(){
      let context = this.$refs.canvas.getContext('2d');
      var chartData = {
          labels: this.labels,
          datasets: []
      };

      this.values.forEach((element, index, array) => {
        chartData.datasets.push({
          data: element,
          backgroundColor: this.colors[index],
          label: this.names[index],
        });
      });

      new Chart(context, {
        type: 'bar',
        data: chartData,
        });
    }
  }
</script>
