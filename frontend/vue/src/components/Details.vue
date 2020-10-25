<template>
  <div>
    <div v-if="data.length === 0"> 
      <br />
      <a-spin tip="Загрузка...">
        <div class="spin-content">
        </div>
      </a-spin>
    </div> 
    <div v-for="(we, y) in data" :key="y">
       <a-collapse style="margin-top: 20px">
         <a-collapse-panel :key="y" :header="getName(we['Тип_записи'],we['Название'])" :disabled="false">
              <a-collapse style="margin-top: 20px" v-for="(item, key) in we.children" :key="key">
                    <a-collapse-panel :key="key" :header="getName(item['Тип_записи'],item['Название'])" :disabled="false">
                    <a-collapse v-for="(ite, keyy) in item.children" :key="keyy+key" style="margin-top: 10px">
                        <a-collapse-panel :key="keyy+key" :header="getName(ite['Тип_записи'],ite['Название'] ? ite['Название'] : '')" :disabled="false">
                            <div v-for="(oo, ll) in ite" :key="ll" style="text-align: left">
                              <template v-if="ll != 'children' && ll != 'id' && ll.indexOf('-примечание') == -1">
                                <EditInput :item="ite" :text="oo" :k="ll" :path="y+'-'+key+'-'+keyy" @edited="makeEdit"/>
                                <br />
                              </template>
                            </div>
                            <a-collapse v-for="(it, keyyy) in ite.children" :key="keyy+key+keyyy" style="margin-top: 10px">
                                <a-collapse-panel :key="keyy+key+keyyy" :header="getName(it['Тип_записи'],it['Тип'])" :disabled="false">
                                  <div v-for="(o, l) in it" :key="l" style="text-align: left">
                                    <template v-if="l != 'children' && l != 'id' && l.indexOf('-примечание') == -1">
                                      <EditInput :item="it" :text="o" :k="l" :path="y+'-'+key+'-'+keyy+'-'+keyyy" @edited="makeEdit"/>
                                      <br />
                                    </template>
                                  </div>
                                </a-collapse-panel>
                            </a-collapse>
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
import EditInput from '@/components/InputText'
export default {
  data() {
    return {
      data: [],
      res: "",
      key: 0
    }
  },
  components: {
    EditInput
  },
  methods: {
    makeEdit(data) {
      console.log('w', data)
      const path = data.path.split('-')
      let d = this.data
      console.log(path)
      if (path.length == 4) {
        this.data[path[0]].children[path[1]].children[path[2]].children[path[3]][data.id] = data.value
      } else if (path.length == 3) {
        this.data[path[0]].children[path[1]].children[path[2]][data.id] = data.value
      }
      axios.post("http://90.189.183.166:13451/api/company_data/"+this.$route.params.id, this.data)
        .then(response => {
          console.log(response)
        })
    },
    edit() {
      alert('sad')
    },
    renderList(list) {
        let text = ""
        for (let el in list) {
            if (el !== "children" && list[el] !== null && el !== "id") {
                let e = el.toString()
                text += `<div><b>${e.replace("_", " ").replace("_", " ").replace("_", " ").replace("_", " ").replace("_", " ")}</b> - <input type='text' onchange='edit() value=${list[el]}/></div>`
                for (let i in list) {
                    if (e+"-примечание" === i) {
                        text += `<input type='text' /> <br />`
                    }
                }
                text += "<br />"
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