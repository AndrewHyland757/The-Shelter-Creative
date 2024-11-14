// Handles image changes on the project modal list

document.addEventListener("DOMContentLoaded", function () {
    const projectItems = document.querySelectorAll(".project-item");
    const projectsImgsContainer = document.querySelector(
      ".projects-imgs-container"
    );
    const originalImages = projectsImgsContainer.innerHTML;

    projectItems.forEach((item) => {
      const projectImageElement = item.querySelector(".list-image-url");
      const projectImage = projectImageElement ? projectImageElement.src : "";

      item.addEventListener("mouseenter", function () {
        if (projectImage) {
          projectsImgsContainer.innerHTML = "";
          projectsImgsContainer.classList.remove("projects-imgs-container");
          projectsImgsContainer.classList.add("project-img-container");

          // Create a new img element associated with the specific project
          const newImage = document.createElement("img");
          newImage.src = projectImage; 
          newImage.alt = "Project Image";
          newImage.style.width = "100%";
          newImage.style.height = "auto";
          newImage.style.objectFit = "cover";

          // Add the new image to the container
          projectsImgsContainer.appendChild(newImage);
        }
      });

      item.addEventListener("mouseleave", function () {
        // Restore the original images and change the container class back
        projectsImgsContainer.innerHTML = originalImages;
        projectsImgsContainer.classList.remove("project-img-container");
        projectsImgsContainer.classList.add("projects-imgs-container");
      });
    });
  });