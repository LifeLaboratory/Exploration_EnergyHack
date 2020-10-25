<template>
    <div>
        <div v-for="(el, key) in companys" :key="key">
            <a-card hoverable style="width: 100%; margin-top: 20px" @click="goToCompany(el.id)">
                <a-card-meta :title="el['Название']">
                    <template slot="description">
                    </template>
                </a-card-meta>
            </a-card>
            <br />
            <a-button type="primary" icon="download" :size="size" @click="getPods(el.id, el['Название'])">
              Отчет по подстанциям
            </a-button>
            <a-button type="primary" icon="download" :size="size" @click="getLEP(el.id, el['Название'])" style="margin-left: 10px">
              Отчет по ЛЭП
            </a-button>
            <a-button type="primary" icon="download" :size="size" @click="getWord(el.id, el['Название'])" style="margin-left: 10px">
              Итоговый отчет
            </a-button>
        </div>
    </div>
</template>
<script>
/*
отчет по подстанциям
отчет по леп
итоговый
*/
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
      getPods(id, name) {
        axios.get("http://90.189.183.166:13451/api/pc_report/"+id,
        {
          headers: {
            'Content-Type': 'application/json',
          },
          responseType: 'blob'
        })
          .then(response => {
            console.log(response.data)
            const url = window.URL.createObjectURL(new Blob([response.data]))
            const link = document.createElement('a')
            link.href = url
            link.setAttribute('download', name + ' Отчет по подстанциям.xlsx')
            document.body.appendChild(link)
            link.click()
          })
      },
      getLEP(id, name) {
        axios.get("http://90.189.183.166:13451/api/lep_report/"+id,
        {
          headers: {
            'Content-Type': 'application/json',
          },
          responseType: 'blob'
        })
          .then(response => {
            console.log(response.data)
            const url = window.URL.createObjectURL(new Blob([response.data]))
            const link = document.createElement('a')
            link.href = url
            link.setAttribute('download', name + ' Отчет по ЛЭП.xlsx')
            document.body.appendChild(link)
            link.click()
          })
      },
      getWord(id, name) {
        axios.get("http://90.189.183.166:13451/api/word_report/"+id,
        {
          headers: {
            'Content-Type': 'application/json',
          },
          responseType: 'blob'
        })
          .then(response => {
            console.log(response.data)
            const url = window.URL.createObjectURL(new Blob([response.data]))
            const link = document.createElement('a')
            link.href = url
            link.setAttribute('download', name + '.docx')
            document.body.appendChild(link)
            link.click()
          })
      },
      goToCompany(id) {
          this.$router.push({path: '/profile/detail/' + id})
      }
  },
};
</script>

<style scoped>

</style>