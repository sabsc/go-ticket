// Global container for our movie data
window.movies = {
    params: {}
};

// fetchData
function fetchData() {
    // $.get("/api/?" + $.param(window.winners.params))
    //     .done(function(data) {
    //         $('#raw-json').text(JSON.stringify(data, null, '  '));
    //         // Add data to global container
    //         window.winners.data = data;
    //         // Re-render the bar chart
    //         window.winners.bar.render();
    //         window.winners.map.render();
    //     })
    //     .fail(function(){
    //         console.log("Could not load data");
    //         alert("Could not load data");
    //     });

    $.get("/api/theaters/" + $.param(window.movies.params))
        .done(function(data) {
            window.movies.data=data.Data;
            // console.log(window.movies.data);
            // initMapFeatures();
            initMap();
        })
        .fail(function(){
            console.log("Could not load data");
            alert("Could not load data");
        });

    $.get("/api/movies/" + $.param(window.movies.params))
        .done(function(data) {
            // $('#movie-bar').text(JSON.stringify(data, null, '  '));
            window.movies.data=data.Data;
            initBar(window.movies);

        })
        .fail(function(){
            console.log("Could not load data");
            alert("Could not load data");
        });

}

// init wires up watchers on selections and fetches new data
function init(){
    // var countrySel = $('#sel-country');
    // var categorySel = $('#sel-category');
    // var genderSel = $('#sel-gender');
    //
    // function updateSelections() {
    //     var params = window.winners.params || {};
    //     params.country = countrySel.val();
    //     params.category = categorySel.val();
    //     params.gender = genderSel.val();
        fetchData();
    // }
    //
    // // Initialize bar chart and map
    // initBar(window.winners);
    // initMap(window.winners);
    //
    // countrySel.on('change', updateSelections);
    // categorySel.on('change', updateSelections);
    // genderSel.on('change', updateSelections);
    // updateSelections();
}


// Call init on DOMReady
$(init);
