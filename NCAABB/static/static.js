var dynamicATag = document.querySelector(".inputSearch");
var teamSearchButton = document.querySelector("#teamSearchButton");

dynamicATag.addEventListener('click', update);

function updateLink(item) {
  item.href += item;

}
