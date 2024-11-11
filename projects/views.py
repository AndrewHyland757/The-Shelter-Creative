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
    the HTML with image URLs, video URL, and other placeholders replaced.
    """
    company = section.project.company
    main_service_name = section.project.main_service.service_name

    project_description_1 = section.project_description_1 if section.project_description_1 else ''
    project_description_2 = section.project_description_2 if section.project_description_2 else ''

    
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

    # Add alt value to images
    for desc_field, placeholder in image_descriptions:
        if desc_field:
            description = desc_field
        else:
            description = f"{company}: {main_service_name} by The Shelter Creative" 
        section_html_with_images = section_html_with_images.replace(placeholder, description)

    # Replace video URL if video_file is not null
    if section.video_file:
        video_url = section.video_file.url  # Get the video URL
        section_html_with_images = section_html_with_images.replace('{{ video_url }}', video_url)

    # Add text to html where applicable
    section_html_with_content = (
        section_html_with_images
        .replace('{{ project_description_1 }}', project_description_1)
        .replace('{{ project_description_2 }}', project_description_2)
        .replace('{{ services }}', services_list)
        .replace('{{ project_company }}', company)
        .replace('{{ project_main_service }}', main_service_name)
)

    return section_html_with_content



def change_color(section, page_position, section_css):
    """
    Function to change the header color if required.
    """
    position = page_position
    new_color = section.new_header_color
    new_color_tablet = section.new_header_color_tablet
    new_color_mobile = section.new_header_color_mobile

    # Base styles (Desktop)
    if new_color:
        new_color_hover = section.new_header_color_hover or new_color
        section_css += f"""
        .fp-viewing-{position} .logo,
        .fp-viewing-{position} .sublogo,
        .fp-viewing-{position} .header-right button {{
            color: {new_color};
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

    # Tablet styles (if specified)
    if new_color_tablet:
        new_color_hover_tablet = section.new_header_color_hover_tablet or new_color_tablet
        section_css += f"""
        @media only screen and (max-width: 1024px) {{
            .fp-viewing-{position} .logo,
            .fp-viewing-{position} .sublogo,
            .fp-viewing-{position} .header-right button {{
                color: {new_color_tablet};
            }}
            .fp-viewing-{position} .logo:hover,
            .fp-viewing-{position} .logo:active,
            .fp-viewing-{position} .sublogo--email:hover,
            .fp-viewing-{position} .sublogo--email:active,
            .fp-viewing-{position} .header-right button:hover,
            .fp-viewing-{position} .header-right button:active {{
                color: {new_color_hover_tablet};
            }}
        }}
        """

    # Mobile styles (if specified)
    if new_color_mobile:
        new_color_hover_mobile = section.new_header_color_hover_mobile or new_color_mobile
        section_css += f"""
        @media only screen and (max-width: 767px) {{
            .fp-viewing-{position} .logo,
            .fp-viewing-{position} .sublogo,
            .fp-viewing-{position} .header-right button {{
                color: {new_color_mobile};
            }}
            .fp-viewing-{position} .logo:hover,
            .fp-viewing-{position} .logo:active,
            .fp-viewing-{position} .sublogo--email:hover,
            .fp-viewing-{position} .sublogo--email:active,
            .fp-viewing-{position} .header-right button:hover,
            .fp-viewing-{position} .header-right button:active {{
                color: {new_color_hover_mobile};
            }}
        }}
        """

    return section_css

    return section_css
    


def change_text_color(section, page_position, section_css):
    """
    Function to change the company/service text color at bottom of section.
    """
    position = page_position
    new_color = section.new_text_color
    new_color_tablet = section.new_text_color_tablet
    new_color_mobile = section.new_text_color_mobile
    
    # Base styles
    section_css += f"""
    .fp-viewing-{position} .company p,
    .fp-viewing-{position} .main-service p,
    .fp-viewing-{position} .line {{
        color: {new_color};
        border-color: {new_color};
    }}
    """

    # Tablet styles (if specified)
    if new_color_tablet:
        section_css += f"""
        @media only screen and (max-width: 1024px) {{
            .fp-viewing-{position} .company p,
            .fp-viewing-{position} .main-service p,
            .fp-viewing-{position} .line {{
                color: {new_color_tablet};
                border-color: {new_color_tablet};
            }}
        }}
        """

    # Mobile styles (if specified)
    if new_color_mobile:
        section_css += f"""
        @media only screen and (max-width: 767px) {{
            .fp-viewing-{position} .company p,
            .fp-viewing-{position} .main-service p,
            .fp-viewing-{position} .line {{
                color: {new_color_mobile};
                border-color: {new_color_mobile};
            }}
        }}
        """

    return section_css

 

def project(request, project_slug):
    """
    Renders an individual project.
    """
    projects = Project.objects.all()
    project = get_object_or_404(Project, slug=project_slug)
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
    section_9_html_content = None
    section_9_css = None
    section_10_html_content = None
    section_10_css = None
    
   
    # Process Section if they exist.

    if project_page.section_1:
        
        section_1 = project_page.section_1
        section_1_html_content = get_section_html_content(section_1)
        section_1_css = get_section_css(section_1)
    if section_1.change_header_color:
        section_1_css = change_color(section_1, "1", section_1_css)
    if section_1.change_text_color:
        section_1_css = change_text_color(section_1, "1", section_1_css)

    if project_page.section_2:
        section_2 = project_page.section_2
        section_2_html_content = get_section_html_content(section_2)
        section_2_css = get_section_css(section_2)
        if section_2.change_header_color:
            section_2_css = change_color(section_2, "2", section_2_css)
        if section_2.change_text_color:
            section_2_css = change_text_color(section_2, "2", section_2_css)

    if project_page.section_3:
        section_3 = project_page.section_3
        section_3_html_content = get_section_html_content(section_3)
        section_3_css = get_section_css(section_3)
        if section_3.change_header_color:
            section_3_css = change_color(section_3, "3", section_3_css)
        if section_3.change_text_color:
            section_3_css = change_text_color(section_3, "3", section_3_css)

    if project_page.section_4:
        section_4 = project_page.section_4
        section_4_html_content = get_section_html_content(section_4)
        section_4_css = get_section_css(section_4)
        if section_4.change_header_color:
            section_4_css = change_color(section_4, "4", section_4_css)
        if section_4.change_text_color:
            section_4_css = change_text_color(section_4, "4", section_4_css)

    if project_page.section_5:
        section_5 = project_page.section_5
        section_5_html_content = get_section_html_content(section_5)
        section_5_css = get_section_css(section_5)
        if section_5.change_header_color:
            section_5_css = change_color(section_5, "5", section_5_css)
        if section_5.change_text_color:
            section_5_css = change_text_color(section_5, "5", section_5_css)

    if project_page.section_6:
        section_6 = project_page.section_6
        section_6_html_content = get_section_html_content(section_6)
        section_6_css = get_section_css(section_6)
        if section_6.change_header_color:
            section_6_css = change_color(section_6, "6", section_6_css)
        if section_6.change_text_color:
            section_6_css = change_text_color(section_6, "6", section_6_css)

    if project_page.section_7:
        section_7 = project_page.section_7
        section_7_html_content = get_section_html_content(section_7)
        section_7_css = get_section_css(section_7)
        if section_7.change_header_color:
            section_7_css = change_color(section_7, "7", section_7_css)
        if section_7.change_text_color:
            section_7_css = change_text_color(section_7, "7", section_7_css)

    if project_page.section_8:
        section_8 = project_page.section_8
        section_8_html_content = get_section_html_content(section_8)
        section_8_css = get_section_css(section_8)
        if section_8.change_header_color:
            section_8_css = change_color(section_8, "8", section_8_css)
        if section_8.change_text_color:
            section_8_css = change_text_color(section_8, "8", section_8_css)

    if project_page.section_9:
        section_9 = project_page.section_9
        section_9_html_content = get_section_html_content(section_9)
        section_9_css = get_section_css(section_9)
        if section_9.change_header_color:
            section_9_css = change_color(section_9, "9", section_9_css)
        if section_9.change_text_color:
            section_9_css = change_text_color(section_9, "9", section_9_css)
    
    if project_page.section_10:
        section_10 = project_page.section_10
        section_10_html_content = get_section_html_content(section_10)
        section_10_css = get_section_css(section_10)
        if section_10.change_header_color:
            section_10_css = change_color(section_10, "10", section_10_css)
        if section_10.change_text_color:
            section_10_css = change_text_color(section_10, "10", section_10_css)

    

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
        'section_9_html_content': section_9_html_content,
        'section_9_css': section_9_css,
        'section_10_html_content': section_10_html_content,
        'section_10_css': section_10_css,
    }

    template = "projects/project.html"
    
    return render(request, template, context)
