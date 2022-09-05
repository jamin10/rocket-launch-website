function bookmarkLaunch(slug) {
    fetch('/bookmark-launch', {
        method: "POST", 
        body: JSON.stringify({ slug: slug }), 
    }).then((_res) => {
        window.location.href = "/upcoming-launches";
    });
}

function deleteLaunch(slug) {
    fetch('/delete-launch', {
        method: "POST", 
        body: JSON.stringify({ slug: slug }), 
    }).then((_res) => {
        window.location.href = "/bookmarked-upcoming";
    });
}