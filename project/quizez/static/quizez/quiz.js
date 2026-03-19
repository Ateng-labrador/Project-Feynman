console.log('hello world quiz')
const url = window.location.href
console.log(url)

const quizBox = document.getElementById('quiz-box')
let data 

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        // console.log(response)
        data = response.data
        data.forEach(el => {
            let questionText = ""
            let answers = []
            let solutions = []
            for (const [key, value] of Object.entries(el)){
                if(key == "solution"){
                    solutions = value
                }
                else{
                    questionText = key
                    answers = value
                }
            }
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${questionText}</b>
                    </div>
                `
                answers.forEach(ans => {
                    quizBox.innerHTML += `
                        <div>
                            <input type="radio" class="ans" name="${questionText}" value="${ans}">
                            <label>${ans}</label>
                        </div>
                    `
                })
                solutions.forEach(sol => {
                    quizBox.innerHTML += `
                        <div><p>${sol}</p></div>
                    `
                })
        });
    },
    error: function(error){
        console.log(error)
    }
    
})
