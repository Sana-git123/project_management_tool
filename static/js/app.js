const navItems = document.querySelectorAll(".nav-item");


navItems.forEach((item) => {
    item.addEventListener("click", () => {
        navItems.forEach((item) => {
            item.classList.remove("active");
        });
        item.classList.add("active");
    });
});



//  // Get the current path of the page
//  var currentPath = window.location.pathname;
//  // Get all navigation links
//  var navLinks = document.querySelectorAll('nav-item');
//  // Iterate through each navigation link
//  navLinks.forEach(function(link) {
//      // Check if the current path matches the link's href attribute
//      if (currentPath === link.getAttribute('href')) {
//          // Add the active class to the link's parent <li> element
//          link.parentElement.classList.add('active');
//      }
//  });