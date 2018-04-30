// function fetchData() {
//   $.get("/movies/api/theaters/")
//       .done(function(data) {
//           $('#raw-json').text(JSON.stringify(data, null, '  '));
//           window.movies.data=data.Data;
//           //console.log(window.movies.data);
//           initMapFeatures();
//       })
//       .fail(function(){
//           console.log("Could not load data");
//           alert("Could not load data");
//       });
// }
// var locs = [];
//
// function initMapFeatures(){
//   // console.log("Test");
//   for (t=0; t<window.movies.data.length; t++) {
//     var name = window.movies.data[t];
//     var theaterName = name.theaterName;
//     var lat = name.lat;
//     var lng = name.lng;
//     // var address = theater.addressOne;
//     // var city = theater.city;
//
//     var newLoc = {'name':theaterName, 'position':new google.maps.LatLng(lat,lng), 'type':"loc"}
//     // console.log(newLoc);
//
//     //info for infoWindow
//     // var theaterName = name.theaterName;
//     // var infoWindow = new google.maps.InfoWindow({
//       // maxWidth: 300
//     // });
//     locs.push(newLoc);
//
//   //create a new map marker and add it to the map
//   // var pos = {lat: parseFloat(latitude), lng: parseFloat(longitude)};
//   }
// }
// console.log(locs);

function initMap() {


  var styledMapType = new google.maps.StyledMapType(
    [
      {
          "featureType": "administrative",
          "elementType": "labels.text.fill",
          "stylers": [
              {
                  "color": "#2c212f"
              },
              {
                  "lightness": "20"
              }
          ]
      },
      {
          "featureType": "administrative.province",
          "elementType": "geometry.stroke",
          "stylers": [
              {
                  "visibility": "off"
              }
          ]
      },
      {
          "featureType": "landscape",
          "elementType": "geometry",
          "stylers": [
              {
                  "lightness": "0"
              },
              {
                  "saturation": "0"
              },
              {
                  "color": "#f5f5f2"
              },
              {
                  "gamma": "1"
              }
          ]
      },
      {
          "featureType": "landscape.man_made",
          "elementType": "all",
          "stylers": [
              {
                  "lightness": "-3"
              },
              {
                  "gamma": "1.00"
              }
          ]
      },
      {
          "featureType": "landscape.natural.terrain",
          "elementType": "all",
          "stylers": [
              {
                  "visibility": "off"
              }
          ]
      },
      {
          "featureType": "poi",
          "elementType": "all",
          "stylers": [
              {
                  "visibility": "off"
              }
          ]
      },
      {
          "featureType": "poi.park",
          "elementType": "geometry.fill",
          "stylers": [
              {
                  "visibility": "off"
              },
              {
                  "saturation": "-60"
              }
          ]
      },
      {
          "featureType": "road",
          "elementType": "all",
          "stylers": [
              {
                  "saturation": -100
              },
              {
                  "lightness": 45
              },
              {
                  "visibility": "simplified"
              }
          ]
      },
      {
          "featureType": "road.highway",
          "elementType": "all",
          "stylers": [
              {
                  "visibility": "simplified"
              }
          ]
      },
      {
          "featureType": "road.highway",
          "elementType": "geometry.fill",
          "stylers": [
              {
                  "color": "#bf422e"
              },
              {
                  "visibility": "simplified"
              },
              {
                  "lightness": "60"
              }
          ]
      },
      {
          "featureType": "road.highway",
          "elementType": "labels.text",
          "stylers": [
              {
                  "color": "#2c212f"
              },
              {
                  "lightness": "20"
              }
          ]
      },
      {
          "featureType": "road.arterial",
          "elementType": "labels.text.fill",
          "stylers": [
              {
                  "color": "#787878"
              }
          ]
      },
      {
          "featureType": "road.arterial",
          "elementType": "labels.icon",
          "stylers": [
              {
                  "visibility": "off"
              }
          ]
      },
      {
          "featureType": "transit",
          "elementType": "all",
          "stylers": [
              {
                  "visibility": "simplified"
              }
          ]
      },
      {
          "featureType": "transit.station.airport",
          "elementType": "labels.icon",
          "stylers": [
              {
                  "hue": "#0a00ff"
              },
              {
                  "saturation": "-77"
              },
              {
                  "gamma": "0.57"
              },
              {
                  "lightness": "0"
              }
          ]
      },
      {
          "featureType": "transit.station.rail",
          "elementType": "labels.text.fill",
          "stylers": [
              {
                  "color": "#43321e"
              }
          ]
      },
      {
          "featureType": "transit.station.rail",
          "elementType": "labels.icon",
          "stylers": [
              {
                  "hue": "#ff6c00"
              },
              {
                  "lightness": "4"
              },
              {
                  "gamma": "0.75"
              },
              {
                  "saturation": "-68"
              }
          ]
      },
      {
          "featureType": "water",
          "elementType": "all",
          "stylers": [
              {
                  "color": "#eaf6f8"
              },
              {
                  "visibility": "on"
              }
          ]
      },
      {
          "featureType": "water",
          "elementType": "geometry.fill",
          "stylers": [
              {
                  "color": "#c7eced"
              }
          ]
      },
      {
          "featureType": "water",
          "elementType": "labels.text.fill",
          "stylers": [
              {
                  "lightness": "-49"
              },
              {
                  "saturation": "-53"
              },
              {
                  "gamma": "0.79"
              }
          ]
      }
    ])

  var morris = {lat: 35.8235, lng: -78.8256};

  var icons = {

      loc: {
          icon: {
              path: 'M 100, 100 m -75, 0 a 75,75 0 1,0 150,0 a 75,75 0 1,0 -150,0',
              fillColor: '#e24b1d',
              fillOpacity: 0.8,
              scale: .1,
              strokeColor: '#ffffff',
              strokeWeight: 2
          }
      }
  };

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: morris
  });
  map.mapTypes.set('styled_map', styledMapType);
  map.setMapTypeId('styled_map');

  for (t=0; t<window.movies.data.length; t++) {
    var name = window.movies.data[t];
    var theaterName = name.theaterName;
    var address = name.addressOne;
    var zip = name.zip;
    var phone = name.phone;
    var city = name.city;
    var lat = name.lat;
    var lng = name.lng;

    let marker = new google.maps.Marker({
        position: new google.maps.LatLng(lat,lng),
        icon: icons.loc.icon,
        title: theaterName,
        // map: map
    });


    let contentString =
      '<strong>'+theaterName+'</strong><br>'+
      address+'<br>'+
      ''+city+' NC, '+zip+'<br>'+phone;

    let infowindow = new google.maps.InfoWindow({
      content: contentString
        // content: marker.title
    });

    marker.addListener('mouseover', function() {
        infowindow.open(map, marker);
    });

    marker.addListener('mouseout', function(){
        infowindow.close();
    });

    marker.addListener('click', function() {
        map.setZoom(15);
        map.setCenter(marker.getPosition());
    });
    marker.setMap(map);
  }


}
