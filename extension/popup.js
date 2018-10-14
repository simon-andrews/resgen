function doStuffWithDom(domContent) {
  console.log('I received the following DOM content: ' + domContent);
}

document.addEventListener('DOMContentLoaded', function () {
  var button = document.getElementById('genresume-button');
  button.addEventListener('click', function (tab) {
    chrome.tabs.query({active: true, currentWindow: true}, function (openTabs) {
      var tab = openTabs[0]; //this should work like 99.9% of the time, but not guaranteed
      chrome.tabs.sendMessage(tab.id, {text: 'report_back'}, doStuffWithDom);
    });
  });
});
