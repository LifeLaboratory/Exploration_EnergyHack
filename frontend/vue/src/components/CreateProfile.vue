<template>
  <div style="text-align: left">
    <div> <h2>Создание</h2> </div>
    <br />
    <div class="card_list">
      <div class="card_file">
        <a-upload
          action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
          :default-file-list="defaultFileList"
        >
          <span class="title">1. Назавние</span> <a-button> <a-icon type="upload" /> Загрузить </a-button> <span style='margin-left: 10px'><a href="">Пример файла</a></span>
        </a-upload>
      </div>

      <div class="card_file">
        <a-upload
          action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
          :default-file-list="defaultFileList"
        >
          <span class="title">2. Назавние</span> <a-button> <a-icon type="upload" /> Загрузить </a-button> <span style='margin-left: 10px'><a href="">Пример файла</a></span>
        </a-upload>
      </div>

      <div class="card_file">
        <a-upload
          action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
          :default-file-list="defaultFileList"
        >
          <span class="title">3. Назавние</span> <a-button> <a-icon type="upload" /> Загрузить </a-button> <span style='margin-left: 10px'><a href="">Пример файла</a></span>
        </a-upload>
      </div>

      <div class="card_file">
        <a-upload
          action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
          :default-file-list="defaultFileList"
        >
          <span class="title">4. Назавние</span> <a-button> <a-icon type="upload" /> Загрузить </a-button> <span style='margin-left: 10px'><a href="">Пример файла</a></span>
        </a-upload>
      </div>

      <div class="card_file">
        <a-upload
          action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
          :default-file-list="defaultFileList"
        >
          <span class="title">5. Назавние</span> <a-button> <a-icon type="upload" /> Загрузить </a-button> <span style='margin-left: 10px'><a href="">Пример файла</a></span>
        </a-upload>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      defaultFileList: []
    }
  },
  methods: {
    handleChange({ file, fileList }) {
      if (file.status !== 'uploading') {
        console.log(file, fileList);
      }
    },
  },
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