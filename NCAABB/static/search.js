var teamSearchBar = document.querySelector("#teamSearchBar");
var textInput = document.querySelector("#textInput");
var searchDropdown = document.querySelector("#searchDropdown");


teamSearchBar.addEventListener('input', getXHR);

function getXHR(){
  var xhr = new XMLHttpRequest();
  var urlPath = "/teams/_get/?query=" + encodeURI(textInput.value);
  xhr.open("GET", urlPath, true);
  console.log("just Opened xhr");
  //clear contents before replacing with new contents
  searchDropdown.innerHTML = "";
  console.log("about to load xhr!");
  xhr.onload = function(e) {
    console.log("Just loaded xhr");
    if (xhr.readyState == 4) {
      console.log("Ready status === 4!");
      if (xhr.status == 200) {
        console.log("status === 200!");
        var suggestions = JSON.parse(xhr.responseText);
        if (suggestions){
          suggestions.forEach(function(val){
            var tag = '<li class="list-group-item-action">' + val + '</li>';
            searchDropdown.insertAdjacentHTML('beforeend', tag);
          });
          //xhr.responseText
          addLIEventListeners();
        }
      } else {

        console.log(xhr.statusText);
        console.log(xhr.status);
      }
    }
  };
  xhr.onerror = function (e) {
    console.log("error!");
    console.log(e);
    console.log(xhr.status);
    console.log(xhr.responseText);
  };
  xhr.send(null);
}

function addLIEventListeners() {
  var items = searchDropdown.querySelectorAll("li");
  // items always returns True, so need to check length explicitly
  if (items){
    for (var i = 0; i < items.length; i++){
      items[i].addEventListener('click', function(item){
        textInput.value = this.textContent;
      });
    }
  }
}
