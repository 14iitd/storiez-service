let pageCount = 0;

function addPage() {
    pageCount++;
    const pageContainer = document.createElement('div');
    pageContainer.className = 'page';
    pageContainer.id = `page${pageCount}`;

    pageContainer.innerHTML = `
        <h2>Page ${pageCount}</h2>
        <div>
            <label for="title${pageCount}">Page Title:</label>
            <input type="text" id="title${pageCount}" name="title${pageCount}" required>
        </div>
        <div>
            <label for="image${pageCount}">Image URL:</label>
            <input type="url" id="image${pageCount}" name="image${pageCount}" required>
        </div>
        <div>
            <label for="text${pageCount}">Story Text:</label>
            <textarea id="text${pageCount}" name="text${pageCount}" required></textarea>
        </div>
        <button type="button" class="remove-page" onclick="removePage(${pageCount})">Remove Page</button>
    `;

    document.getElementById('pages').appendChild(pageContainer);
}

function removePage(pageId) {
    const pageElement = document.getElementById(`page${pageId}`);
    pageElement.remove();
}

function generateStory() {
    let storyContent = '';
    for (let i = 1; i <= pageCount; i++) {
        if (document.getElementById(`page${i}`)) {
            const title = document.getElementById(`title${i}`).value;
            const image = document.getElementById(`image${i}`).value;
            const text = document.getElementById(`text${i}`).value;

            storyContent += `
            <amp-story-page id="page${i}">
                <amp-story-grid-layer template="fill">
                    <amp-img src="${image}" width="720" height="1280" layout="responsive"></amp-img>
                </amp-story-grid-layer>
                <amp-story-grid-layer template="vertical" style="background: rgba(0, 0, 0, 0.5); color: white; padding: 10px;">
                    <h1>${title}</h1>
                    <p>${text}</p>
                </amp-story-grid-layer>
            </amp-story-page>`;
        }
    }

    const ampStory = `
    <!doctype html>
    <html amp lang="en">
    <head>
        <meta charset="utf-8">
        <title>AMP Story</title>
        <link rel="canonical" href="self.html">
        <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
        <style amp-boilerplate>body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}</style><noscript><style amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}</style></noscript>
        <script async src="https://cdn.ampproject.org/v0.js"></script>
        <script async custom-element="amp-story" src="https://cdn.ampproject.org/v0/amp-story-1.0.js"></script>
        <style amp-custom>
            amp-story {
                font-family: 'Arial', sans-serif;
            }
            h1 {
                font-size: 2em;
                margin: 0.67em 0;
            }
            p {
                font-size: 1em;
            }
        </style>
    </head>
    <body>
        <amp-story standalone title="AMP Story" publisher="AMP Story Creator" publisher-logo-src="https://example.com/logo.png">
            ${storyContent}
        </amp-story>
    </body>
    </html>`;

    const previewFrame = document.getElementById('preview');
    const previewDoc = previewFrame.contentDocument || previewFrame.contentWindow.document;
    previewDoc.open();
    previewDoc.write(ampStory);
    previewDoc.close();
}

// Initialize with one page
addPage();
