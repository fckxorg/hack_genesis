fetch('/get/data').then(
    function (response) {
        if (response.status !== 200) {
            console.log("Максим пидор, ничего не прислал((( Status: " + response.status);
            return;
        }

        response.json().then(
            function (data) {
                console.log(data);

                document.getElementById("slogan").innerHTML = data.slogan;
                document.getElementById("motivation").innerHTML = data.motivation;

                let companyNames = document.getElementsByClassName("company-name");
                console.log(companyNames);
                for (let i = 0; i < companyNames.length; i += 2) {
                    companyNames[i].innerHTML = data.cards[i/2].name;
                    companyNames[i + 1].innerHTML = data.cards[i/2].name;
                }

                let percentBlocks = document.getElementsByClassName("percent-num");
                for (let i = 0; i < percentBlocks.length; ++i) {
                    // let percentNum = '+' + data.cards[i].profit_prediction + '%';
                    // console.log(percentNum);
                    percentBlocks[i].innerText = '+' + data.cards[i].profit_prediction + '%';
                }

                let timeBlocks = document.getElementsByClassName("time");
                for (let i = 0; i < timeBlocks.length; ++i) {
                    timeBlocks[i].innerText = data.cards[i].term;
                }

                let amountBlocks = document.getElementsByClassName("amount");
                for (let i = 0; i < amountBlocks.length; ++i) {
                    amountBlocks[i].innerText = data.cards[i].investments_sum + " р";
                }

                let logoBlocks = document.getElementsByClassName("level");
                for (let i = 0; i < logoBlocks.length; ++i) {
                    amountBlocks[i].style.backgroundImage = "url(\"static/css/" + data.cards[i].logo + "\")";
                }

                // let graphicBlocks = document.getElementsByClassName("graphic");
                // for (let i = 0; i < graphicBlocks.length; ++i) {
                //     graphicBlocks[i].style.backgroundImage = "url(\"static/css/" + data.cards[i].logo + "\")";
                // }
            }
        );
    }
).catch(function (error) {
    console.log("Fetch error :-S", error);
});