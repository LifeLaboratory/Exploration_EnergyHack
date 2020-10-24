<template>
  <div>
      <div v-for="(item, key) in data.children" :key="key">
          <a-collapse style="margin-top: 20px">
                <a-collapse-panel :key="key" :header="getName(item['Тип_записи'],item['Название'])" :disabled="false">
                <a-collapse v-for="(ite, keyy) in item.children" :key="keyy+key" style="margin-top: 10px">
                    <a-collapse-panel :key="keyy+key" :header="getName(ite['Тип_записи'],ite['Название'])" :disabled="false">
                        <div style="text-align: left" v-html="renderList(ite)" />
                        <a-collapse v-for="(it, keyyy) in ite.children" :key="keyy+key+keyyy" style="margin-top: 10px">
                            <a-collapse-panel :key="keyy+key+keyyy" :header="getName(it['Тип_записи'],it['Название'])" :disabled="false">
                               <div style="text-align: left" v-html="renderList(it)" />
                            </a-collapse-panel>
                        </a-collapse>
                    </a-collapse-panel>
                </a-collapse>
            </a-collapse-panel>
        </a-collapse>
      </div>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      data: {},
      res: "",
      key: 0
    }
  },
  methods: {
    renderList(list) {
        let text = ""
        for (let el in list) {
            if (el !== "children" && list[el] !== null && el !== "id") {
                let e = el.toString()
                text += `<div><b>${e.replace("_", " ")}</b> - ${list[el]} </div>`
            }
        }
        return text
        console.log(list)
    },
    getName(type, name) {
        return type + " - " + name
    },
    changeActivekey(key) {
      console.log(key);
    },
    makeCollspase(item) {
        this.res += `<a-collapse-panel key="${this.key}" header="${item["Название"]}>`
        this.key++

    }
  },
  mounted() {
    axios.get("http://90.189.183.166:13451/api/company_data/"+this.$route.params.id)
      .then(response => {
        const d = response.data
        this.data = d
      })
  }
};
</script>

<style scoped>
  .title {
    font-size: 20px;
    margin-right: 10px;
  }
  .card_list {
    text-align: center;
  }
  .card_file {
    margin-top: 10px
  }
</style>