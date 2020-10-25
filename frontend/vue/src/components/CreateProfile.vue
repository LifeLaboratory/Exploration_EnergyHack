<template>
  <div>
    <div style="font-size: 30px">Загрузите файл в формате .xlsx</div>
    <br />
    <a-upload
      list-type="picture"
      action="http://90.189.183.166:13451/api/upload_data"
      :preview-file="previewFile"
    >
      <a-button> <a-icon type="upload" /> Загрузить </a-button>
    </a-upload>
  </div>
</template>
<script>
export default {
  methods: {
    previewFile(file) {
      console.log('Your upload file:', file);
      // Your process logic. Here we just mock to the same file
      return fetch('http://90.189.183.166:13451/api/upload_data', {
        method: 'POST',
        body: file,
      })
        .then(res => res.json())
        .then(({ thumbnail }) => thumbnail);
    },
  },
};
</script>