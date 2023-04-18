function updateImage() {
    chrome.storage.sync.get(['image_src'], function (data) {
        var src = data.image_src;
        var img = document.createElement('img');
            img.src = src;
            document.getElementById('canvas').appendChild(img);
    });
}    

document.addEventListener('DOMContentLoaded', updateImage);