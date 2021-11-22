new Vue({
  el: '#app',
  delimiters: ['{$', '$}'],
  data: {
    full_name: '',
    ocupation: '',
    age: 20,
    kword: '',
    lista_agregados: [],
    lista_lenguajes: '',
  },
  watch: {
    kword: function (val) {
      this.BuscarLenguajes(val);
    }
  },
  methods: {
    BuscarLenguajes: function (kword) {
      var self = this;
      axios.get('/api/lenguaje/search/?kword=' + kword)
        .then(function (response) {
          self.lista_lenguajes = response.data
        })
        .catch( function (error) {
          console.log(error);
        })
    },
});