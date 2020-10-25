fetch('/get/data').then(
    function (response) {
        if (response.status !== 200) {
            console.log("Максим пидор, ничего не прислал((( Status: " + response.status);
            return;
        }

        response.json().then(
            function (data) {
                console.log(data);

                document.getElementById("slogan").write(data.slogan);
                document.getElementById("motivation").write(data.motivation);
            }
        );
    }
).catch(function (error) {
    console.log("Fetch error :-S", error);
});