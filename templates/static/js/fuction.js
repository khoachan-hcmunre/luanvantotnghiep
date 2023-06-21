function clickroute(lati,long) {

    map = google.maps.Map(document.getElementById("map_canvas"));
   map.panTo(lati,long)
}