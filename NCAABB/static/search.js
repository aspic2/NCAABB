var teamSearchBar = document.querySelector("#teamSearchBar");
var textInput = document.querySelector("#textInput");
var searchDropdown = document.querySelector("#searchDropdown");


teamSearchBar.addEventListener('input', getXHR);

function getXHR(){
  var xhr = new XMLHttpRequest();
  var urlPath = "/teams/_get/?query=" + encodeURI(textInput.value);
  console.log(urlPath);
  xhr.open("GET", urlPath, true);
  //clear contents, then replace with new contents
  searchDropdown.innerHTML = "";
  xhr.onload = function(e) {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        var suggestions = JSON.parse(xhr.responseText);
        if (suggestions){
          suggestions.forEach(function(val){
            var tag = "<p>" + val + "</p>";
            searchDropdown.insertAdjacentHTML('beforeend', tag);
          });
          //xhr.responseText
          addLIEventListeners();
        }      
      } else {
        console.error(xhr.statusText);
      }
    }
  };
  xhr.onerror = function (e) {
    console.error(xhr.statusText);
  };
  xhr.send(null);
}

function addLIEventListeners() {
  var items = searchDropdown.querySelectorAll("p");
  // items always returns True, so need to check length explicitly
  if (items){
    for (var i = 0; i < items.length; i++){
      items[i].addEventListener('click', function(item){
        textInput.value = this.textContent;
      });
    }
  }
}
