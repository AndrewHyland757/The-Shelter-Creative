from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Project, ProjectPage, Section, Template


def get_section_css(section):
    if section.use_custom_css:
        section_css = section.custom_css
    else:
        section_css = section.template.css_content if section.template else ''

    return section_css


def get_section_html_content(section):
    """
    Retrieves a Section instance for the given project_page and returns 
    the HTML with image URLs and other placeholders replaced.
    """
    company = section.project.company
    main_service_name = section.project.main_service.service_name


    project_description_1 = section.project_description_bold if section.project_description_1 else ''
    project_description_2 = section.project_description if section.project_description_2 else ''

    
    services = section.project.services.all()
    if services:  # Check if services exists and is not empty
        services_list = ''.join(f'<p class="service">{service.service_name}</p>' for service in services)
        
    else:
        services_list = ''

    # Determine which HTML to use
    if section.use_custom_html:
        section_html = section.custom_html
    else:
        section_html = section.template.html_content if section.template else ''

    # Start with original HTML
    section_html_with_images = section_html

    # List of image attributes and corresponding placeholder names
    images = [
        (section.img_1, '{{ img_1_url }}'),
        (section.img_1_tablet, '{{ img_1_url_tablet }}'),
        (section.img_1_mobile, '{{ img_1_url_mobile }}'),

        (section.img_2, '{{ img_2_url }}'),
        (section.img_2_tablet, '{{ img_2_url_tablet }}'),
        (section.img_2_mobile, '{{ img_2_url_mobile }}'),

        (section.img_3, '{{ img_3_url }}'),
        (section.img_3_tablet, '{{ img_3_url_tablet }}'),
        (section.img_3_mobile, '{{ img_3_url_mobile }}'),

        (section.img_4, '{{ img_4_url }}'),
        (section.img_4_tablet, '{{ img_4_url_tablet }}'),
        (section.img_4_mobile, '{{ img_4_url_mobile }}'),

        (section.img_5, '{{ img_5_url }}'),
        (section.img_5_tablet, '{{ img_5_url_tablet }}'),
        (section.img_5_mobile, '{{ img_5_url_mobile }}'),

        (section.img_6, '{{ img_6_url }}'),
        (section.img_6_tablet, '{{ img_6_url_tablet }}'),
        (section.img_6_mobile, '{{ img_6_url_mobile }}'),

        (section.img_7, '{{ img_7_url }}'),
        (section.img_7_tablet, '{{ img_7_url_tablet }}'),
        (section.img_7_mobile, '{{ img_7_url_mobile }}'),

    ]

    for img_field, placeholder in images:
        if img_field:
            img_url = img_field.url  # Convert ImageFieldFile to URL string
            section_html_with_images = section_html_with_images.replace(placeholder, img_url)
    


    image_descriptions = [
        (section.img_1_description, '{{ img_1_description }}'),
        (section.img_2_description, '{{ img_2_description }}'),
        (section.img_3_description, '{{ img_3_description }}'),
        (section.img_4_description, '{{ img_4_description }}'),
        (section.img_5_description, '{{ img_5_description }}'),
        (section.img_6_description, '{{ img_6_description }}'),
        (section.img_7_description, '{{ img_7_description }}'),
    ]


    for desc_field, placeholder in image_descriptions:
        if desc_field:
            description = desc_field
        else:
            description = f"{company}: {main_service_name} by The Shelter Creative" 
        section_html_with_images = section_html_with_images.replace(placeholder, description)

    if section.project_description_1:
        section_html_with_content = section_html_with_images.replace('{{ project_description_1 }}', project_description_1)
    if section.project_description_2:
        section_html_with_content = section_html_with_images.replace('{{ project_description_2 }}', project_description_2)
    else:
        section_html_with_content = section_html_with_images

    return section_html_with_content



def change_color(section, page_position, section_css):
    """
    Function to change the header color if required.
    """
    position = page_position
    new_color = section.new_header_color

    # Check if a new hove color is set
    if section.new_header_color_hover:
        new_color_hover = section.new_header_color_hover
    else:
        new_color_hover = new_color
    
    section_css += f"""
    .fp-viewing-{position} .logo,
    .fp-viewing-{position} .sublogo,
    .fp-viewing-{position} .header-right button {{
        color: {new_color} !important;
    }}
    .fp-viewing-{position} .logo:hover,
    .fp-viewing-{position} .logo:active,
    .fp-viewing-{position} .sublogo--email:hover,
    .fp-viewing-{position} .sublogo--email:active,
    .fp-viewing-{position} .header-right button:hover,
    .fp-viewing-{position} .header-right button:active {{
        color: {new_color_hover};
    }}
    """
    return section_css
 

def project(request, project_id):
    """
    Renders an individual project.
    """
    projects = Project.objects.all()
    project = get_object_or_404(Project, id=project_id)
    project_page = get_object_or_404(ProjectPage, project=project)

    # Initialize variables for Sections HTML and CSS content.
    section_1_html_content = None
    section_1_css = None
    section_2_html_content = None
    section_2_css = None
    section_3_html_content = None
    section_3_css = None
    section_4_html_content = None
    section_4_css = None
    section_5_html_content = None
    section_5_css = None
    section_6_html_content = None
    section_6_css = None
    section_7_html_content = None
    section_7_css = None
    section_8_html_content = None
    section_8_css = None
    
   
   # Process Section if they exist.

    if project_page.section_1:
        section_1 = project_page.section_1
        section_1_html_content = get_section_html_content(section_1)
        section_1_css = get_section_css(section_1)
        # Calls the change_color function if change_color is True
        if section_1.change_header_color:
            section_1_css = change_color(section_1, "1", section_1_css)
            print(section_1_css)  # Check the output


        
    if project_page.section_2:
        section_2 = project_page.section_2
        section_2_html_content = get_section_html_content(section_2)
        section_2_css = get_section_css(section_2)
        # Calls the change_color function if change_color is True
        if section_2.change_header_color:
            section_2_css = change_color(section_2, "2", section_2_css)

    if project_page.section_3:
        section_3 = project_page.section_3
        section_3_html_content = get_section_html_content(section_3)
        section_3_css = get_section_css(section_3)
        # Calls the change_color function if change_color is True
        if section_3.change_header_color:
            section_3_css = change_color(section_3, "3", section_3_css)

    if project_page.section_4:
        section_4 = project_page.section_4
        section_4_html_content = get_section_html_content(section_4)
        section_4_css = get_section_css(section_4)
        # Calls the change_color function if change_color is True
        if section_4.change_header_color:
            section_4_css = change_color(section_4, "4", section_4_css)

    if project_page.section_5:
        section_5 = project_page.section_5
        section_5_html_content = get_section_html_content(section_5)
        section_5_css = get_section_css(section_5)
        # Calls the change_color function if change_color is True
        if section_5.change_header_color:
            section_5_css = change_color(section_5, "5", section_5_css)

    if project_page.section_6:
        section_6 = project_page.section_6
        section_6_html_content = get_section_html_content(section_6)
        section_6_css = get_section_css(section_6)
        # Calls the change_color function if change_color is True
        if section_6.change_header_color:
            section_6_css = change_color(section_6, "6", section_6_css)

    if project_page.section_7:
        section_7 = project_page.section_7
        section_7_html_content = get_section_html_content(section_7)
        section_7_css = get_section_css(section_7)
        # Calls the change_color function if change_color is True
        if section_7.change_header_color:
            section_7_css = change_color(section_7, "7", section_7_css)

    if project_page.section_8:
        section_8 = project_page.section_8
        section_8_html_content = get_section_html_content(section_8)
        section_8_css = get_section_css(section_8)
        # Calls the change_color function if change_color is True
        if section_8.change_header_color:
            section_8_css = change_color(section_8, "8", section_8_css)
    

    context = {
        "projects": projects,
        "project": project,
        "project_page": project_page,
        'section_1_html_content': section_1_html_content,
        'section_1_css': section_1_css,
        'section_2_html_content': section_2_html_content,
        'section_2_css': section_2_css,
        'section_3_html_content': section_3_html_content,
        'section_3_css': section_3_css,
        'section_4_html_content': section_4_html_content,
        'section_4_css': section_4_css,
        'section_5_html_content': section_5_html_content,
        'section_5_css': section_5_css,
        'section_6_html_content': section_6_html_content,
        'section_6_css': section_6_css,
        'section_7_html_content': section_7_html_content,
        'section_7_css': section_7_css,
        'section_8_html_content': section_8_html_content,
        'section_8_css': section_8_css,
    }

    template = "projects/project.html"
    
    return render(request, template, context)