var TechFrontend = document.getElementById("tech-frontend");
var TechFrontendBox = document.getElementById("tech-frontend-box");
var TechBackend = document.getElementById("tech-backend");
var TechBackendBox = document.getElementById("tech-backend-box");
var TechDb = document.getElementById("tech-db");
var TechDbBox = document.getElementById("tech-db-box");
var TechCloud = document.getElementById("tech-cloud");
var TechCloudBox = document.getElementById("tech-cloud-box");

function addHoverListener(elementToHover, elementToModify) {
  const isSmallScreen = window.matchMedia('(max-width: 991px)').matches;
  console.log(window.matchMedia('(max-width: 991px)').matches)
  if (isSmallScreen) {
    elementToHover.addEventListener('click', function() {
      if (elementToModify.classList.contains('hide')) {
        elementToModify.classList.add('hide');
      } else {
        elementToModify.classList.remove('hide');
      }
    });
  } else {
    elementToHover.addEventListener('mouseenter', function() {
      elementToModify.classList.remove('hide');
    });

    elementToHover.addEventListener('mouseleave', function() {
      elementToModify.classList.add('hide');
    });
  }
}

addHoverListener(TechFrontend, TechFrontendBox)
addHoverListener(TechFrontendBox, TechFrontendBox)
addHoverListener(TechBackend, TechBackendBox)
addHoverListener(TechBackendBox, TechBackendBox)
addHoverListener(TechDb, TechDbBox)
addHoverListener(TechDbBox, TechDbBox)
addHoverListener(TechCloud, TechCloudBox)
addHoverListener(TechCloudBox, TechCloudBox)