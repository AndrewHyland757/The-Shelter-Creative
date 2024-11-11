document.addEventListener("DOMContentLoaded", function () {
    const projectItems = document.querySelectorAll(".project-item");
    const projectsImgsContainer = document.querySelector(
      ".projects-imgs-container"
    );
    const originalImages = projectsImgsContainer.innerHTML; // Save the original images

    projectItems.forEach((item) => {
      // Retrieve the image URL from the hidden img element inside the current project-item
      const projectImageElement = item.querySelector(".list-image-url");
      const projectImage = projectImageElement ? projectImageElement.src : "";

      item.addEventListener("mouseenter", function () {
        // Only change the image if projectImage is not empty
        if (projectImage) {
          // Hide current images and change the container class
          projectsImgsContainer.innerHTML = "";
          projectsImgsContainer.classList.remove("projects-imgs-container");
          projectsImgsContainer.classList.add("project-img-container");

          // Create a new img element associated with the specific project
          const newImage = document.createElement("img");
          newImage.src = projectImage; // Set the image URL from the hidden img element
          newImage.alt = "Project Image";
          newImage.style.width = "100%"; // Style the new image
          newImage.style.height = "auto";
          newImage.style.objectFit = "cover"; // Ensure the image fits well

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