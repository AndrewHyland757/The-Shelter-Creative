# Table Of Content

-   [Front End Design](#front-end-design)
    -   [User Stories](#user-stories)
    -   [Site Goals](#site-goals)
    -   [Scope](#scope)
-   [Design](#design)
    -   [Colour Scheme](#colour-scheme)
    -   [Database Schema](#Database-Schema)
    -   [Fonts](#Fonts)
    -   [Wireframes](#Wireframes)
    -   [Agile Methodology](#Agile-Methodology)
         -   [Overview](#overview)
         -   [EPICS(Milestones)](#epicsmilestones)
         -   [User Stories issues](#user-stories-issues)
         -   [MoSCoW prioritization](#moscow-prioritization)
         -   [GitHub Projects](#github-projects)
-   [Features](#features)
    -   [Navbar](#Navbar)
    -   [Footer](#Footer)
    -   [Home](#Home)
        -   [Hero Section](#hero-section)
        -   [Search Form](#search-form)
        -   [Product Card](#product-card)
    -   [Profile Page](#profile-page)
    -   [Sign In Page](#sign-in-page)
    -   [Sign Up Page](#sign-up-page)
    -   [Sign Out Confirmation](#sign-out-confirmation)
    -   [Password reset](#password-reset)
    -   [Password reset email sent](#password-reset-email-sent)
    -   [Enter a new password](#enter-a-new-password)
    -   [Password Reset Completed](#password-reset-completed)
    -   [Error Pages](#error-pages)
-   [Future Features](#future-features)
-   [Marketing](#marketing)
-   [Search Engine Optimization SEO](#search-engine-optimization-seo)
-   [Testing](#testing)
-   [Bugs](#Bugs)





## Role **: Full-Stack Developer  
**Responsibilities**:
- Design of the front-end for mobile and desktop using Figma.
- Development the front-end.
- Development of the back-end template database using Django.
- Image Curation & image optimization including editing and resizing images. 
- Deployment
- SEO implementation 


## Scope

### Business Goals

 The main objective of the website is to highlight the client's work and boost engagement in order to attract potential future business opportunities.
 This is to be achieved by:

- A design and website personality that reflects the clients values and appeals to the target demographic.
As the business is involved in branding, a strong empahsis was put on the visual elements of the website and also influnced functionality.

- The presentation of the clients previous work. The showcasing and curation of images and videos were of primary importance.
- A website that is easy and intuitive to navigate.
- The ability for users to access essential information such as, contact information, services offered, and past projects.

- Incorporating SEO features into the website.

A secondary goal is to increase engagement expand the clients network and scope in the industry. 


### Target Audience

- Brands and clients in various industries, including fashion, retail, beauty, travel, and luxury lifestyle.
- People working in creative production, photography, branding, fashion, visual media and content creation.


### User Experience - Requirements and Expectations
- A user-friendly website that balances information with an aesthetic that is appealing and modern.
- A mobile-friendly website
- A way to view the clients work.
- Information about the clients business.
- A way to make contact.
- A way to easily access social media accounts from the website.

### General User Needs
1. As a user, I can intuitively navigate through the website so that I can easily access key information and view desired content.
2. As a user, I can find essential information about the company, such as: services offered, contact info & social media links.
3. As a user, I can view the clients work clearly.
3. As a user, I can see a list of the clients past projects.
4. As a user, I can explore each project further and see services offered, project description and releated images and videos.



## Front End Design

Given the company's expertise in branding, the website's design and functionality were meticulously crafted with visual communication as a primary driver. 
Every design element was intentionally selected to create a cohesive, compelling narrative that resonates with the target audience and showcases the company's creative capabilities.

### Brief
- A design communicates the brand value and appeals to the target audience.
- A website personality and tone that is neutral, bold, confident, modern and that quitely reflects luxury and sophistication.
- A website that is easy to navigate and locate necessary information for optimal user experience.

### Execution



#### Images & Videos

- As images are the primary content of the website much care was given them.
- Art direction was implemented using the <picture> element to provide multiple versions of an image for different screen sizes and in controlling the exact crop of an image. 

#### Templates

- A selection of templates were created to faciliate image selection and variety. 
- These included various image grids and full screen arrangments.
- This provided a fast was to upload the projects to the webite and prevented repetition. 
- These grids were uploaded to the website database, when the could be further cusomiised for each section if needed.




#### Text Colours & Background Colours
- Pure white (#FFFFFF) is utilized as the main background colour.
- The info modal as well as the favicon and open graph image utilise (#948A7A) as a background-color. 
This muted, warm gray-brown evokes feelings of calmness, stability and good legibility, making it an ideal choice.
- The default text color is an off-black (#1E1C1C), which is applied to all text elements throughout the website.
- An off-white (#F2F0EF) is used for text elements that appear over dark images and videos, ensuring optimal legibility and contrast.
- A colour gradient chart was used to generate shades for hoover colours.


![Color palette](static/images/readme_images/colour_palette_the_shelter_creative.png)



#### Typography Selection

The typography choices for the website were carefully considered to align with the brief of creating a modern yet refined and luxurious tone.


 [Big Noodle Too](https://www.myfonts.com/collections/big-noodle-too-font-sentinel-type?gad_source=1&gclid=Cj0KCQiA_9u5BhCUARIsABbMSPspweB8dLDucMRA3ii2S5-KCBvfQFYDur-5oPWZg2d6gYnDGusHoKUaApQXEALw_wcB) from myfonts.com is used on the logo. The client had already used this font before for the company logo.


Sans-serif for Headings and Navigation: 
[Helvetica Now ](https://www.myfonts.com/collections/helvetica-now-variable-font-monotype-imaging?gad_source=1&gclid=Cj0KCQiA_9u5BhCUARIsABbMSPt9lteUZbeU0eapbzvWRKqirrfeP-TPfpJa1AQDZUr3y596Hq5TbyIaAqzbEALw_wcB) from myfonts.com, was selected for headings and navigation elements in the header. This modern update of the classic Helvetica offers improved legibility and a fresh aesthetic, perfectly complementing the website's contemporary design12. 

[Reckless Neue Book ](https://displaay.net/typeface/reckless-collection/reckless-neue/) from Displaay Type Foundry, was chosen for the primary body text. Its elevated x-height enhances readability while imparting a contemporary and refined feel, aligning well with the desired website personality3.

This combination of sans-serif for headings and serif for body text creates a balanced visual hierarchy, marrying modern design sensibilities with a touch of classic elegance. The contrast between the two typefaces adds visual interest while maintaining a cohesive and sophisticated overall appearance.
<br>
<br>
![Image of fonts](static/images/readme_images/fonts.png)

## UX 

### Full-Page Scrolling

 Full-Page Scrolling was decided on to be used as the scrolling pattern and is a core element of the website. This was implemented using Fullpage.js. 
This provides an immersive and curated experience allowing users to focus on one image at a time minimising distractions from surrounding content and traditional scrolling. 
This turned out particularly effective in showcasing the clients work which primarialy deals in photography, branding and creative production.

### Enhanced User Experience

- Open Graph (OG) meta tags improve social media sharing by providing rich previews with accurate titles, descriptions, and images when the site is shared on platforms like Facebook or LinkedIn.
- Favicon implementation across various devices and sizes enhances brand recognition and improves the site's visual appearance in browser tabs and bookmarks.
- Font preloading optimizes page load times by prioritizing the loading of critical fonts, reducing layout shifts and improving perceived performance.
- Manifest file enhances the user experience by providing a more app-like feel to the website and improving its integration with mobile devices.


## Features

### 404 Error Page


A custom 404 page was implemented to handle and site errors.
<br>

![404 page](static/images/readme_images/404.png)


### Logo Design

#### Key Objectives and Features:
- Display the company's name prominently
- Maintain brand continuity
- Create a modern and sophisticated visual identity
- Ensure versatility across various applications



#### Execution
- Typography: After thorough consultations with the client regarding typography options, we ultimately decided to retain the original font, Big Noodle Too, in all uppercase. This choice honors the company's heritage, as it has been in use since the brand's inception. The selected font aligns perfectly with the overall tone and aesthetic of the website, providing a seamless visual experience.

- Sub-logo: To enhance the logo's impact, I proposed the addition of a sub-logo specifically for the website, to be placed beneath the main company logo. For the sub-logo, we chose Helvetica Now, a contemporary serif font that complements the primary logo while adding a fresh, modern touch. This combination creates a unique visual hierarchy, blending the refined sophistication of the main logo with the modern industrial feel of the sub-logo.


The contrast between the two typefaces adds depth and interest to the overall design, making it more memorable and visually appealing. The final logo design successfully balances tradition with innovation, creating a distinctive and versatile visual identity that effectively represents the company's brand across all platforms. It acts as a stamping mark on all pages of the website, reinforcing brand recognition and leaving a lasting impression on visitors.

![Logo](static/images/readme_images/logo.png)

### Landing Page

#### Key Objectives and Features:
- Capture user attention & generate intrigue to encourage further exploration of the website.
- Foster an emotional connection with the user.
- Aligne with the overall brand identity, including color schemes and style. 
 
 #### Execution

- An appropriate image was selected to accomplish the necessary criteria..
- The decision was made to omit common features of a landing page, such as a CTA (Call-to-Action) button and text, in order to preserve the desired tone and personality.

![Landing Page ](static/images/readme_images/landing.png)

### Header

#### Key Objectives and Features:
- Provide navigation links to the info and projects modal pages.
- Showcase brand identity through strategic logo placement
- Impact. Develop a distinctive, non-conventional header design therfore not using standard templates
- Maintain visual hierarchy that prioritizes main content of the page


#### Execution
The header design deliberately deviated from conventional layouts by positioning the logo at the extreme left and navigation elements to the right. This unconventional approach achieved multiple design objectives:
- Bold Visual Statement: The asymmetrical layout creates a striking, original composition that immediately communicates the website's innovative and creative personality.
- Visual Hierarchy: The sparse, minimalist design allows imagery to become the focal point, drawing users' attention to the core visual content.
- Functional Elegance: Despite its unconventional placement, the navigation remains intuitive and easily accessible, balancing aesthetic innovation with user experience.
- The header is implemented as an absolute element and, using fullpage.js anchoring, allows for easy colour transitionss between sections.

The strategic header design reflects a thoughtful approach to layout, where form follows function while simultaneously making a bold visual statement that aligns with the website's contemporary and refined aesthetic.

![Header](static/images/readme_images/header.png)


### Info modal


The website features a unique approach to presenting essential information through an info modal, accessible via the header's info link. This design choice reimagines the traditional footer and about section, consolidating them into a single, easily accessible interface.

#### Key Objectives and Features:
- Comprehensive Company Overview: Offers concise yet informative details about the company's mission, values, and core competencies.
- Display essential information including: social media profile links, contact information, service offerings and a client roster.

#### Execution


- Intergration of a customised Bootstrap 4 modal.
- A custom layout was designed for the info page, keeping the 'about' text to the left and the essential information to the right in a column. This design creates a clean, refined, and easily legible layout that maintains visual hierarchy while achieving a balanced, asymmetric composition.


#### User Experience:
- Always readily available, eliminating the need for scrolling to access a footer
- Provides a fresh, intriguing alternative to conventional website layouts
- Efficient Information Architecture: Streamlines the user's journey to key information, improving overall site navigation and engagement


![Screenshot of info modal](static/images/readme_images/info.png)



### Projects Modal

The website features access to the companies past work accessible via the header's projects link.

#### Key Objectives and Features:

- Present all projects in a clear, visually appealing manner
- Each project entry acts as a clickable link for further exploration
- Displays the client company name and primary service provided


#### Execution

- Intergration of a customised Bootstrap 4 modal.
- A custom layout was designed for the projects modal. 
- Dynamic Visual Representation. Desktop consistes of two colums, on the left consisting of a scrollable links to each project, and on the right a dynamic image container which containes a shows a collage of three project images which is replaced by a project image whien the project link is hoovered on. This is implemented by a custom Javascript script.
- Responsive Design. Mobile consists of the project list in one column, each like being a 4:5 aspect image with project name and service.



#### User Experience:
- Provides visual context for each project, aiding in quick recognition and interest generation and streamlines the user's journey from curiosity to detailed project exploration.
- Offers an intuitive, organised and engaging way to browse through the company's work
- Encourages exploration by combining textual information with visual elements


![Screenshot of info modal](static/images/readme_images/projects.png)

### Home Page

As users scroll beyond the landing page, the rest of the homepage offers a gallery-like experience through one-page scrolling, showcasing a selection of the client's portfolio that includes both images and videos. This seamless journey loops back to the landing page at the end, creating a cohesive browsing experience.

#### Key Objectives and Features:
##### 
- Foster interest by providing a visually engaging presentation of a selection of the companies work.
- Context about each section - having the project name and main service visible.
- A section that offers insight into the way the way the company works. 
 
#### Execution
- Templates were created to allow for images to be presented in a variety of manners. then with the client it was decided on waht images to use for the home page and in wht configuration. 
- Section 3 on the home page consists of three slides with text and act as an insight to the companies processes. 
- Responsive Design: the poicture element was used to ensure that layouts adapt seamlessly to various screen sizes and to control art direction.


#####  Enhanced User Experience:
- Immersive Scrolling: The full-page scrolling design provides users with an immersive, curated experience that allows them to fully appreciate the media content.
- Encouragement for Exploration: Combines textual information with visual elements to motivate further site exploration.



This thoughtfully designed homepage not only showcases the client’s portfolio effectively but also enhances user interaction and satisfaction, making it a compelling entry point for visitors.



![Homepage](static/images/readme_images/homepage.png)


## Back-End Design

This database is a comprehensive Django project management system designed to create flexible, multi-section project pages with robust content management capabilities. It consists of five core models.

![Image of database](static/images/readme_images/database.png)

### Service Model

The Service model is a foundational component that catalogues all available services. Its structure allows for connection to each project instance in two ways:<br>
- As a main service (ForeignKey in the Project model)
- As secondary services (ManyToMany relationship in the Project model)


### Template Model
The Template model serves as a repository for reusable section layouts. Each template includes:
- A unique name for easy identification
- HTML content defining the structure
- Optional CSS content for styling
- A description to aid in template selection
This model promotes consistency across project pages while allowing for customization when needed.

### Project Model
The Project model is the core entity, containing essential project information:
- Company name
- A unique slug for URL generation
- Main service (ForeignKey to Service model)
- Secondary services (ManyToMany relationship with Service model)
- List position for ordering projects in the Projects Modal
- An optional image for list display in the Projects Modal

This model effectively organizes key project details and establishes relationships with services.

### Project Page model
The ProjectPage model acts as an aggregator, bringing together up to ten sections for a comprehensive project presentation. It:
- Links to a specific project
- Contains references to multiple Section instances (up to 10)
- Provides a method to generate a unique URL for each project page

### Section Model
This comprehensive model encapsulates all the essential content required to construct a dynamic and customizable section for a project page quickly.
Its structure includes:
- Template Integration: It incorporates a reference to a pre-defined template from the template model, offering a foundation for consistent design.
- Custom Styling Options: For enhanced flexibility, the model allows for the inclusion of custom HTML and CSS, enabling unique section designs when needed.
- Content Management: Includes all the media and texts needed, including a video file field an multipe image fields including tablet and mobile sizes.
- Colour Customization Functionality: Includes options to modify the color of the company-service text and header text of each section and on various screen sizes.

The Section model is a highly flexible component for building project pages. It includes:
- Reference to a specific project
- Option to use a predefined template or custom HTML/CSS
- Fields for project descriptions ( if texts are needed in the section )
- Customizable color options for header and text elements, with responsive design support
- Capability to include up to seven images with descriptions, each with tablet and mobile versions
- An optional video field

This model allows for rich, quick, customized content creation for each project section.


### get_unique_image_name ( function ) 
Generates unique names for images uploaded to Cloudinary by using the project's company name and slug. All images contain the 
company's name and the client/project the images relates to. This saves time when uploading images, ensures consistent file names and improves SEO. 

### get_project_image_upload_to ( function )  
Determines the upload path for project images in Cloudinary, creating folders dynamically based on the project's slug. If no slug exists, it defaults to a standard folder.
These functions facilitate effective asset management in Cloudinary by organizing images into relevant folders and ensuring that file names are unique, preventing overwrites during uploads.

## Logic
The views.py file in the projects app contains the code to process the backend data and connect it to the frontend. 

### get_section_css(section): 
This function retrieves the custom CSS for a section, either from a custom property or from the associated template.

### get_section_html_content(section): 
This function generates the HTML content for a section. It replaces placeholders like image URLs, descriptions, video URLs, and text descriptions with actual data from the section or project. The content includes dynamic fields such as project descriptions and associated services.

### change_color(section, page_position, section_css) and change_text_color(section, page_position, section_css): 
These functions modify the CSS styles for specific section elements, such as header colors or text color, depending on user-defined settings for desktop, tablet, and mobile views.

### Main View Function (project):

This function processes a single project page identified by the project_slug. It retrieves the corresponding Project and ProjectPage objects.
It then checks each section (from section_1 to section_10) of the project page. If a section exists, the corresponding HTML content and CSS are generated and processed for any color changes.
The sections' content and CSS are stored in variables, which are passed to the template for rendering.
The overall goal of this view is to dynamically generate and render a project page with customizable content (HTML and CSS), where each section can have unique styles, images, and textual content tailored to the specific project being viewed.]



## Search Engine Optimization SEO and Marketing

### SEO

- Descriptive meta tags are dynamically added to every page.
- Page titles are dynamically added to every page.
- Semantic HTML elements were implemented throughout the site.
- Image file names contain the company and related client.
- Image descriptions: Images uploaded to the database have a "alt" value field. If left blank, an automatically generated "alt" value containing the company's name and client's name is generated.
- A sitemap was generated using [xml-sitemaps](https://www.xml-sitemaps.com/). A url path was created fot the [sitemap](https://www.thesheltercreative.com/sitemap.xml) and then registered in Google Console.
- A robots.txt file was created at the root level of the project. This file tells search engine crawlers which URLs they can access on the website.









## Manual Testing of User Stories

<mark>WAS = Works as expected</mark>

### 1. General User Needs

**Goal** | **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ | ------------ |
Intuitively navigate through the website homepage | Test all sections on different screen sizes and browsers | Section render correctly | WAS |
Find essential information about the company | Test the info link on different screen sizes | Content of the modal is presented | WAS |
View the company'y projects | Test link to projects modal on different screen sizes | Content of the modal is presented | WAS |
View further details on each project | Click on project link in the project modal | Related project is shown | WAS |

## Code Validation
All of my code has been validated using an online validator specific to the language, all code now passes with zero errors. 

- [W3C Markup Validation Service](https://validator.w3.org/) 
    - Used to validate all HTML code written and used in this webpage.
   
    
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate all CSS code written and used in this webpage.
    - No errors shown. 


- [JSHint](https://jshint.com/)
    - Used to validate JS code
    - No errors shown.

- [Code Institute Python Linter](https://pep8ci.herokuapp.com/)
    - Used to test my code for any issues or errors.
    - Some lines in views.py that contained messages were left longer.


- Lighthouse Google Developer Tools
    - In addition to this I have also used online Lighthouse to test the accessibility of my website:

![Image of lighthouse validation](static/images/readme_images/lighthouse.png)

## Bugs and Fixes

### Browser Compatabilites

Videos in Safari covered the brand-service container, where the company name and main service are displayed. This issue occurred because Safari cannot render a video with text in front of it (using a higher z-index).

The issue was resolved by adding a Safari-specific container in the HTML, visible only for Safari browsers. This container rendered the video as a background image. For all other browsers, this approach does not work, so the normal implementation using a <video> element was used.

### Static Files Issues

White noise is used to serve static files. This caused a problem if there were old files in the staticfiles folder from previous clooect static commands which had been deleted. This was 
solved by changing the setting STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage" to STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage".
This compresses static files but doesn't create a manifest which is more forgiving in dealing with deleted files. 


