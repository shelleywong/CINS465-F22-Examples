$(document).foundation()

document.querySelector('h1').addEventListener('click', function(){
  alert("Ouch! Stop poking me!");
});

const VueExamples = {
  data() {
    return {
      count: 0,
      welcome: true
    }
  }
}

myvueexamples = Vue.createApp(VueExamples).mount('#vue-examples')

const ListExample = {
  data() {
    return {
      items: [
        { message: 'CINS 465'},
        { message: 'Fall 2022'},
        { message: 'Hello World'}
      ]
    }
  }
}

mylistexample = Vue.createApp(ListExample).mount('#list-example')
