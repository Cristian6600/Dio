Vue.component('todo-item', {
  template: '\
    <li>\
      {{ title }}\
      <button v-on:click="$emit(\'remove\')">Remover</button>\
    </li>\
  ',
  props: ['title']
})
// -----###-------------
new Vue({
  el: '#app',
  data: {
    show: true,
    kword: '',
    full_name: '',
    lista_agregados: [],
    lista_lenguajes: [],
    nextTodoId: 1
  },
  methods: {
    BuscarLenguajes: function (full_name) {
      var self = this;
      axios.get('/api/lenguaje/search/?full_name=' + full_name)
        .then(function (response) {
          self.lista_lenguajes = response.data
        })
        .catch( function (error) {
          console.log(error);
        })
    },
    
    AgregarLenguaje: function () {
      this.lista_agregados.push({
        id_guia: this.kword,
        title: this.kword
      })
      this.kword = ''
    },

    
    RegistrarProgramador: function () {
      //
      var lista_id_lenguajes = []
      for (let i = 0; i < this.lista_agregados.length; i++) {
        lista_id_lenguajes.push(this.lista_agregados[i].id_guia)
      }
      //
      var data_programador = {
        'full_name': this.full_name,
        'guia': lista_id_lenguajes
      }

      axios.post('/api/programador/register/', data_programador)
        .then(function (response) {
          console.log(response)
        })
        .catch( function (error) {
          console.log(error);
        })
    }
  },
});