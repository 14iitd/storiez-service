function generateForm() {
    const pages = document.getElementById('pages').value;
    let pagesForm = '';

    for (let i = 1; i <= pages; i++) {
        pagesForm += `
            <h2>Page ${i}</h2>
            <div class="form-group">
                <label for="page-title-${i}">Page Title:</label>
                <input type="text" id="page-title-${i}" name="page-title-${i}" required>
            </div>
            <div class="form-group">
                <label for="page-content-${i}">Page Content:</label>
                <textarea id="page-content-${i}" name="page-content-${i}" required></textarea>
            </div>
        `;
    }

    document.getElementById('pages-form').innerHTML = pagesForm;
    document.getElementById('generate-story').style.display = 'block';
}

function generateStory() {
    const title = document.getElementById('title').value;
    const pages = document.getElementById('pages').value;
    let storyContent = `
    <!doctype html>
    <html ⚡>
    <head>
      <meta charset="utf-8">
      <title>${title}</title>
      <link rel="canonical" href="self.html">
      <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
      <style amp-custom>
        body {
          font-family: Arial, sans-serif;
        }
      </style>
      <style amp-boilerplate>
        body {
          -webkit-animation: -amp-start 8s steps(1,end) 0s 1 normal both;
          -moz-animation: -amp-start 8s steps(1,end) 0s 1 normal both;
          -ms-animation: -amp-start 8s steps(1,end) 0s 1 normal both;
          animation: -amp-start 8s steps(1,end) 0s 1 normal both;
        }
        @-webkit-keyframes -amp-start {
          from {
            visibility: hidden;
          }
          to {
            visibility: visible;
          }
        }
        @-moz-keyframes -amp-start {
          from {
            visibility: hidden;
          }
          to {
            visibility: visible;
          }
        }
        @-ms-keyframes -amp-start {
          from {
            visibility: hidden;
          }
          to {
            visibility: visible;
          }
        }
        @-o-keyframes -amp-start {
          from {
            visibility: hidden;
          }
          to {
            visibility: visible;
          }
        }
        @keyframes -amp-start {
          from {
            visibility: hidden;
          }
          to {
            visibility: visible;
          }
        }
      </style>
      <noscript>
        <style amp-boilerplate>
          body {
            -webkit-animation: none;
            -moz-animation: none;
            -ms-animation: none;
            animation: none;
          }
        </style>
      </noscript>
      <script async src="https://cdn.ampproject.org/v0.js"></script>
      <script async custom-element="amp-story" src="https://cdn.ampproject.org/v0/amp-story-1.0.js"></script>
    </head>
    <body>
      <amp-story standalone>
        <amp-story-page id="cover">
          <amp-story-grid-layer template="fill">
            <h1>${title}</h1>
          </amp-story-grid-layer>
        </amp-story-page>
    `;

    for (let i = 1; i <= pages; i++) {
        const pageTitle = document.getElementById(`page-title-${i}`).value;
        const pageContent = document.getElementById(`page-content-${i}`).value;

        storyContent += `
        <amp-story-page id="page${i}">
          <amp-story-grid-layer template="fill">
            <h2>${pageTitle}</h2>
            <p>${pageContent}</p>
          </amp-story-grid-layer>
        </amp-story-page>
        `;
    }

    storyContent += `
      </amp-story>
    </body>
    </html>
    `;

    document.getElementById('output').textContent = storyContent;
}
