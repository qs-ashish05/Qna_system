// In popup.js
document.getElementById('btn').addEventListener('click', function() {
    chrome.tabs.update({ url: chrome.extension.getURL('output.html') });
  });