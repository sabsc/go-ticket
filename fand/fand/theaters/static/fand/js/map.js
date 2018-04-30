//map.js
// function initMap(config){
// // Add our map namespace object to the config with a bool to mark whether
//     // the map data has been loaded
//     config.map = {loaded: false};
//
//     var svgContainer = d3.select("#nobel-map");
//
//     // Start building our svg map
//     var proj = d3.geoEquirectangular();
//     var svg = svgContainer.append("svg");
//     var chart = svg.append("g");
//
//     // Configure our SVG element to be the full width and 200px tall
//     svg.attr('width', '100%')
//         .attr('height', 400);
//
//     // Get the width and height of the element containing our svg element
//     var boundingRect = svgContainer.node().getBoundingClientRect();
//
//     // Hang on to the width and height values to use when generating the map
//     var width = boundingRect.width;
//     var height = boundingRect.height;
//
//
//     // Adjust projection to fill width / height of the container div
//     proj.translate([width / 2, height / 2])
//         .scale(width / (2 * Math.PI));
//
//     // Add graticule lines via a path generator
//     var pathGenerator = d3.geoPath()
//         .projection(proj);
//
//     var graticule = d3.geoGraticule()
//         .step([10, 10]);
//
//     var lines = svg.selectAll('path.graticule')
//         .data([graticule()])
//         .enter()
//         .append('path')
//         .classed('graticule', true)
//         .attr('d', pathGenerator);
//
//
//     // Load the topojson to load in the world map; copied from topojson repo doc
//     d3.json("/static/winners/data/world-110m.json").then(function (jsonData){
//         var world = topojson.feature(jsonData, jsonData.objects.countries);
//         proj.fitSize([width, height], world);
//         svg.append("path")
//             .datum(world)
//             .attr("d", d3.geoPath().projection(proj));
//         config.map.loaded = true;
//         config.map.render();
//     });
//
//
//     // Helper function to turn lat/lng into a point in x/y coords
//    function getProjPoint(data) {
//        return proj([data.lng, data.lat])
//    }
//
// // Add a render method back to the config object
//   config.map.render = function() {
//       // If the map isn't loaded or we don't have data return early
//       if (!config.map.loaded || !config.data) return
//
//       var data = config.data
//
//       // Add circles to the map for winning countries
//       svg.selectAll("circle.winners").remove();
//        var circle = svg.selectAll("circle.winners").data(config.data.countries);
//
//        // Create a scale of winner counts so that our map shows consistent
//        // circle sizes for the country with the most results and the country
//        // with the least results.
//        // Get an array of all the winner counts
//        var winnerCounts = data.countries.map(function (d) {return d.winners});
//        // Get the largest value from the counts
//        var maxWinner = d3.max(winnerCounts);
//        // Create a linear scale using the smallest and largest values
//        // mapping them to values from 3-30 (the pixel ranges for our circle radius)
//        var winnerScale = d3.scaleLinear()
//            .domain([0, maxWinner])
//            .range([3, 30]);
//
//            circle.enter()
//                    .append("circle")
//                    .classed("winners", true)
//                    .attr("r", function(d) {return winnerScale(d.winners)}) // dynamic radius from winner count scale
//                    .attr("cx", function(d) {return getProjPoint(d)[0]}) // x position from our projection point
//                    .attr("cy", function(d) {return getProjPoint(d)[1]}); // y position from our projection point
//
//   }
// }
