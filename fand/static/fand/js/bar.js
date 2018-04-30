
function initBar(config) {
    var svgContainer = d3.select("#movie-bar");

    // Create an object to export our methods on the config
    config.bar = {};

    // Start building our svg bar chart
    var svg = svgContainer.append("svg");
    var chart = svg.append("g");

    // Configure our SVG element to be the full width and 200px tall
    svg.attr('width', '100%')
        .attr('height', 500);

    // Get the width and height of the element containing our svg element
    var boundingRect = svgContainer.node().getBoundingClientRect();

    // Add margins so there is room to draw our axis
    var margin = {'left': 40, 'right': 0, 'top': 10, 'bottom': 220};

    // Hang on to the width and height values to use when generating the graph
    var width = boundingRect.width - (margin.left + margin.right);
    var height = boundingRect.height - (margin.top + margin.bottom);

    // Position the chart with the margin accounted for
    chart.attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
    console.log("test before render");
    console.log(config.data);

    // Render re-renders the bar chart
    config.bar.render = function () {
        // Get the updated countries data sorted by the number of winners

        //var movies = config.data.movies.sort(function(a, b) {
        var movies = config.data.sort(function(a, b) {
            return d3.descending(a.title, parseFloat(b.runtime));
        });

        //console.log(movies);

        // Create lists of country names and the winner counts so we can generate
        // d3 scales from the data.
        // We'll use the country names to create a band scale and the winner
        // counts to create a linear band.
        // https://github.com/d3/d3-scale
        // https://github.com/d3/d3-scale#band-scales
        // https://github.com/d3/d3-scale#linear-scales
        var cnames = movies.map(function(x) {return x.title});
        var winners = movies.map(function(x) {return parseFloat(x.runtime)});
        //console.log(winners);


        // Create our country name scale
        var nameScale = d3.scaleBand() // band scale
            .domain(cnames)            // of country names
            .range([0, width])         // ranging from 0 to the width of our container
            .paddingInner(0.1);        // with padding between the bands

        // Get the highest value from the winners data
        var maxWinner = d3.max(winners);

        // Create our winner count scale
        var winnerScale = d3.scaleLinear() // linear scale
            .domain([0, maxWinner])        // of a domain
            .range([height, 0])            // ranging from the height down to 0
            .nice();                       // rounding to a nice even number

        // Get the width of the bands from the scale
        var bandwidth = nameScale.bandwidth();

        // Remove the graph if it exists
        chart.selectAll("g").remove();

        // Create a group to hold our graph
        var graph = chart.append("g");

        // Create a group for our bars
        var bars = graph.append("g")
            .classed("bars", true)
            .attr('fill', '#90ccce');
        // Draw the bars

        bars.selectAll('rect.bar')
            .data(movies)
            .enter()
            .append('rect')
            .classed('bar', true)
            .attr('width', bandwidth)
            .attr('height', function(d) {
              console.log(d.runtime);
                return height - winnerScale(parseFloat(d.runtime));
            })
            .attr('x', function(d) {
                return nameScale(d.title);
            })
            .attr('y', function(d) {
                return winnerScale(parseFloat(d.runtime));
            });

        // Create a Y axis on the left side from our winner scale
        // If the largest value is greater than 10 only draw 10 tick marks
        // but if the value is less than 10, e.g. 3, only draw 3 tick marks
        var yAxis = d3.axisLeft(winnerScale)
            .ticks(Math.min(10, maxWinner));

        graph.append("g")
            .classed("y axis", true)
            .call(yAxis);

        // Create an X axis on the bottom to show the country names
        var xAxis = d3.axisBottom(nameScale)
            .tickSizeOuter(0);

        graph.append("g")
            .classed("x axis", true)
            .call(xAxis)
            .attr('transform', 'translate(0,' + height + ')')
            .selectAll("text")
            .attr('transform', 'rotate(-65)')
            .style('text-anchor', 'end')
            .attr('dx', '-.8em')
            .attr('dy', '.15em');
    }
    console.log("test after render");
    window.movies.bar.render();
}
