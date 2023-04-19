function updateImage() {
    chrome.storage.sync.get(['image_src'], function (data) {
        /* update image in popup page */
        var src = data.image_src;
        var img = document.createElement('img');
        img.src = src;
        document.getElementById('canvas').appendChild(img);

        /* send url to python script */
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://localhost:5000/?src=\"" + src + "\"", true);
        xhr.send();

        // const dict_values = {'src': src};
        // const s = JSON.stringify(dict_values);

        // $.ajax({
        //     url:"/analyze",
        //     type:"POST",
        //     contentType: "application/json",
        //     data: JSON.stringify(s)});
    });
}    

document.addEventListener('DOMContentLoaded', updateImage);