<template>
    <div>
        <div v-for="(el, key) in companys" :key="key">
            <a-card hoverable style="width: 100%; margin-top: 20px" @click="goToCompany(el.id)">
                <a-card-meta :title="el['Название']">
                    <template slot="description">
                    </template>
                </a-card-meta>
            </a-card>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      companys: []
    }
  },
  mounted() {
    axios.get("http://90.189.183.166:13451/api/companies")
      .then(response => {
        this.companys = response.data
      })
  },
  methods: {
      goToCompany(id) {
          this.$router.push({path: '/profile/detail/' + id})
      }
  },
};
</script>

<style scoped>

</style>