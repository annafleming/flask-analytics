<template>
  <div :class="panelClasses">
      <div class="panel-heading">
          <div class="row">
              <div class="col-xs-3">
                  <i :class="classes"></i>
              </div>
              <div class="col-xs-9 text-right">
                  <div class="huge">{{ value }}</div>
              </div>
          </div>
          <div class="row">
              <div class="col-xs-12 text-right">
                  <div>{{ text }}</div>
              </div>
          </div>
      </div>
  </div>

</template>

<script>
  export default {
    props: [ 'text', 'value', 'icon', 'color'],
    computed: {
      classes(){
        return `fa ${ this.icon } fa-4x`;
      },
      panelClasses(){
        return `panel panel-${ this.color }`;
      }
    }
  }
</script>
