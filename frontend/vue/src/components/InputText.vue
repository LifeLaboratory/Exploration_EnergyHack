<template>
    <div>
        {{label}}
        <input  v-model="value" :id="id" :path="path" @blur="handleBlur"/><div style="margin-bottom: 20px; margin-top: 10px" v-if="show"> Примечание <input  v-model="secondValue" :id="secondValueId" :path="path" @blur="SecondhandleBlur"/> </div>
    </div>
</template>
<script>
import axios from 'axios';
export default {
  props: ["text", "path", "k", "item"],
  data() {
      return {
          value: '',
          label: '',
          secondValue: '',
          secondValueId: '',
          id: '',
          show: false
      }
  },
  methods: {
      SecondhandleBlur(e) {
          this.$emit('edited', {
              value: this.secondValue,
              id: this.secondValueId,
              path: this.path
          })
      },
      handleBlur(e) {
          this.$emit('edited', {
              value: this.value,
              id: this.id,
              path: this.path
          })
      }
  },
  mounted() {
      this.label = this.k.replace('_', ' ').replace('_', ' ').replace('_', ' ').replace('_', ' ')
      this.id = this.k
      for (let key in this.item) {
          if (key === this.id + '-примечание') {
              console.log('asd')
              this.secondValue = this.item[key]
              this.secondValueId = key
              this.show = true
          }
      }
      this.value = this.text.replace('_').replace('_').replace('_').replace('_')
      console.log('1', this.path)
      console.log('kek', this.text)
  }
};
</script>

<style scoped>

</style>