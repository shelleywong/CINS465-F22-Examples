$(document).foundation()
// import axios, * as others from 'axios';

const QuestionList = {
  data() {
    return {
      questions: [],
      interval: null
    }
  },
  mounted(){
    axios.get('/question_json/')
    .then(function (response) {
      // handle success
      myapp.questions = response.data.questions;
      console.log(response);
    })
    .catch(function (error) {
      // handle error
      console.log(error);
    })
    this.interval = setInterval(() => {
      axios.get('/question_json/')
      .then(function (response) {
        // handle success
        myapp.questions = response.data.questions;
        console.log(response);
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
    }, 10000);
  },
  unmounted() {
    clearInterval(this.interval);
  }
}

myapp = Vue.createApp(QuestionList).mount('#question-list')
