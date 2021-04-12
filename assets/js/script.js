// const axios = require('Axios')

// function callApi() {
//     axios.get('https://jmjappmonitoring-back.azurewebsites.net/api/')
//         .then(function(response){
//             console.log(response);
//         });
// }
// function appendData(response) {
//     let mainContainer = document.getElementById("data");
//     for (let i = 0; i < data3.length; i++) {
//         let div = document.createElement("div");
//         div.innerHTML = response[i];
//         mainContainer.appendChild(div);
//     }

// }
document.querySelector("#search_box3").addEventListener("click", getDataFromCustomURL)

function appendData(data) {
    var mainContainer = document.getElementById("myData");
    if (data.length === 0) {
        console.log
        var div = document.createElement("div.costs");
        div.innerHTML ='No cost has been found';
        mainContainer.appendChild(div);
    }
    else {
        for (var i = 0; i < data.length; i++) {
            var div = document.createElement("div.costs");
            div.innerHTML ='\rCout total: '+  data[i].CoutTotal + ' Publication Date: '+ data[i].PublicationDate ;
            mainContainer.appendChild(div);
        }
    }
}

function removeData() {

    /*Tout effacer*/
    var data_div = document.getElementById("myData");

    // As long as <ul> has a child node, remove it
    while (data_div.hasChildNodes()) {  
        data_div.removeChild(data_div.firstChild);

    }
}

function getDataFromCustomURL() {

    removeData()

    var InputSubscriptionName = document.querySelector("#subscriptionname");
    const SubscriptionName_value = InputSubscriptionName.value;

    var InputServiceName = document.querySelector("#servicename");
    const ServiceName_value = InputServiceName.value



    //fetch(`http://localhost:4500/TOP?name=${console_id_value}&ranking=${ranking_id_value}`, {mode: 'cors'})
    //&PublicationDate=<valeur>
    if ( ServiceName_value == "") {
        var my_url = `http://jmjappmonitoring-back.azurewebsites.net/api/?SubscriptionName=${SubscriptionName_value}`
    } 
    else {
        var my_url = `http://jmjappmonitoring-back.azurewebsites.net/api/?SubscriptionName=${SubscriptionName_value}&ServiceName=${ServiceName_value}`
    }
    fetch(my_url , {mode: 'cors'})
    .then(function (response) {
        console.log(response)
        return response.json();
    })
    .then(function (data) {
        console.log("my data",data)
        appendData(data);
    })
    .catch(function (err) {
        console.log(err);
    });
}