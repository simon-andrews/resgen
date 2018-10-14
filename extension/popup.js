function click() {
  console.log('click!');
}

document.addEventListener('DOMContentLoaded', function () {
  var button = document.getElementById('genresume-button');
  button.addEventListener('click', click);
});
