//Fbn65vLE84Ji1Le4hZaZmjXbsUHrvV64ZgLdml3qEcwIMr8z0cPj6dBL8fDy_TJE
var axios = require("axios");


let song='Gorgeous'
let artist='Kanye West'


axios.get("https://api.genius.com/search?q=Kendrick%20Lamar",{
    headers:{

        'Authorization': 'Bearer Fbn65vLE84Ji1Le4hZaZmjXbsUHrvV64ZgLdml3qEcwIMr8z0cPj6dBL8fDy_TJE',
        'Content-type' : 'application/json'
    }

}).then(response=>{
    console.log(response.data);
    response.data.response.hits.forEach(singolo=>{
        console.log(singolo);
    })
}).catch(err=>{
    console.log(err);
});
