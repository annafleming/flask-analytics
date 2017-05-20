<template>
  <div>
    <canvas :id="id"></canvas>
  </div>
</template>

<script>

  export default{
    props: [ 'labels', 'values', 'id'],
    data(){
      return {
      }
    },
    mounted(){
      let context = document.querySelector('#'+ this.id).getContext('2d');
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
