let pageCounter = 0;

function addPage() {
  pageCounter++;
  const pageId = `page${pageCounter}`;
  const page = document.createElement('div');
  page.className = 'story-page';
  page.id = pageId;

  page.innerHTML = `
    <h3>Page ${pageCounter}</h3>
    <button onclick="addElement('${pageId}', 'text')">Add Text</button>
    <button onclick="addElement('${pageId}', 'image')">Add Image</button>
    <div class="page-content"></div>
  `;

  document.getElementById('story-preview').appendChild(page);
}

function addElement(pageId, type) {
  const page = document.getElementById(pageId);
  const contentDiv = page.querySelector('.page-content');

  let element;
  if (type === 'text') {
    element = document.createElement('div');
    element.contentEditable = true;
    element.className = 'story-element text-element';
    element.innerText = 'Edit text...';
  } else if (type === 'image') {
    const url = prompt('Enter image URL:');
    element = document.createElement('img');
    element.src = url;
    element.className = 'story-element image-element';
  }

  contentDiv.appendChild(element);
}

function generateStory() {
  const title = prompt('Enter story title:');
  const publisher = prompt('Enter publisher name:');
  const logo = prompt('Enter publisher logo URL:');
  const poster = prompt('Enter poster image URL:');

  let storyHtml = `
<!doctype html>
<html ⚡>
<head>
  <meta charset="utf-8">
  <title>${title}</title>
  <link rel="canonical" href="self.html">
  <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
  <style amp-custom>
    /* Add your custom styles here */
  </style>
  <script async src="https://cdn.ampproject.org/v0.js"></script>
  <script async custom-element="amp-story" src="https://cdn.ampproject.org/v0/amp-story-1.0.js"></script>
</head>
<body>
  <amp-story standalone title="${title}" publisher="${publisher}" publisher-logo-src="${logo}" poster-portrait-src="${poster}">
`;

  const pages = document.querySelectorAll('.story-page');
  pages.forEach((page, index) => {
    storyHtml += `
    <amp-story-page id="page${index + 1}">
      <amp-story-grid-layer template="fill">
    `;

    const elements = page.querySelectorAll('.story-element');
    elements.forEach(element => {
      if (element.classList.contains('text-element')) {
        storyHtml += `<p>${element.innerText}</p>`;
      } else if (element.classList.contains('image-element')) {
        storyHtml += `<amp-img src="${element.src}" width="720" height="1280" layout="responsive"></amp-img>`;
      }
    });

    storyHtml += `
      </amp-story-grid-layer>
    </amp-story-page>
    `;
  });

  storyHtml += `
  </amp-story>
</body>
</html>
`;

  document.getElementById('storyOutput').textContent = storyHtml;
}
