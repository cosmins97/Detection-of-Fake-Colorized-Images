/* get image function */
function getImage(info, tab) {
    console.log(info.srcUrl  + " was clicked.");

    var image_src = info.srcUrl;
    // chrome.runtime.sendMessage({
    //     src: image_src
    // });
    chrome.storage.sync.set({ 'image_src': image_src });
}

/* on install */
chrome.runtime.onInstalled.addListener(function(info, tab) {
    console.log("installed :DDD");

    chrome.contextMenus.create({
        id: "fakecol-detect",
        title: "Detect fake colorization",
        contexts: ["image"]
    });
});

/* on click */
chrome.contextMenus.onClicked.addListener(getImage);
