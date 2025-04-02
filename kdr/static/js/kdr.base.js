function getCurrentAsideNavbarState() {
    const stateOnCookie = document.cookie
        .split("; ")
        .find((row) => row.startsWith("showAsideNavbar="))
        ?.split("=")[1]

    return stateOnCookie ? stateOnCookie : "true"
}

function showAsideNavbar() {
    document.getElementById("aside-navbar-button").ariaExpanded = "true";
    document.cookie = "showAsideNavbar=true; path=/";

    if(!document.getElementById("aside-navbar").classList.contains('show')) {
        document.getElementById("aside-navbar").classList.add('show');
        document.getElementById("aside-navbar-button-icon-hide").classList.add('show');
        document.getElementById("aside-navbar-button-icon-show").classList.remove('show');
    }
}

function hideAsideNavbar() {
    document.getElementById("aside-navbar-button").ariaExpanded = "false";
    document.cookie = "showAsideNavbar=false; path=/";

    if(document.getElementById("aside-navbar").classList.contains('show')) {
        document.getElementById("aside-navbar").classList.remove('show');
        document.getElementById("aside-navbar-button-icon-hide").classList.remove('show');
        document.getElementById("aside-navbar-button-icon-show").classList.add('show');
    }
}

function loadCurrentAsideNavbarState() {
    getCurrentAsideNavbarState() == "true" ?
        showAsideNavbar() :
        hideAsideNavbar()
}

function addOnClickEventToAsideNavbar() {
    document.getElementById("aside-navbar-button").addEventListener("click", () => {
        getCurrentAsideNavbarState() == "true" ?
            hideAsideNavbar() :
            showAsideNavbar()
    })
}

addOnClickEventToAsideNavbar();