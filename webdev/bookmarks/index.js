document.addEventListener('DOMContentLoaded', function() {
    let siteNameInput = document.getElementById('siteName');
    let siteUrlInput = document.getElementById('siteUrl');
    let bookmarkForm = document.getElementById('bookmarkForm');
    let bookmarksList = document.getElementById('bookmarksList');

    let bookmarks = JSON.parse(localStorage.getItem('bookmarks')) || [];

    function saveBookmarks() {
        localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
    }

    function renderBookmarks() {
        bookmarksList.innerHTML = '';
        for (let i = 0; i < bookmarks.length; i++) {
            let bookmark = bookmarks[i];
            let bookmarkItem = document.createElement('li');
            bookmarkItem.className = 'bookmark-item';
            bookmarkItem.innerHTML = `
                <span>${bookmark.name} - <a href="${bookmark.url}" target="_blank">${bookmark.url}</a></span>
                <button class="delete-button" data-index="${i}">Delete</button>
            `;
            bookmarkItem.querySelector('.delete-button').addEventListener('click', function() {
                bookmarks.splice(i, 1);
                saveBookmarks();
                renderBookmarks();
            });
            bookmarksList.appendChild(bookmarkItem);
        }
    }

    bookmarkForm.addEventListener('submit', function(e) {
        e.preventDefault();
        let siteName = siteNameInput.value.trim();
        let siteUrl = siteUrlInput.value.trim();
        if (siteName && siteUrl) {
            bookmarks.push({ name: siteName, url: siteUrl });
            saveBookmarks();
            renderBookmarks();
            siteNameInput.value = '';
            siteUrlInput.value = '';
        }
    });

    renderBookmarks();
});