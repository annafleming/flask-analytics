<template>
    <canvas></canvas>
</template>

<script>

  export default{
    props: [ 'labels', 'values'],
    data(){
      return {
      }
    },
    mounted(){
      let context = this.$el.getContext('2d');
      var chartData = {
          labels: this.labels,
          datasets: [
              {
                  data: this.values,
              }
          ]
      };

      new Chart.Line(context, {data: chartData, options:{legend:{display: false}}});
    }
  }
</script>
