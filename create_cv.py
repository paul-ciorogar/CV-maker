from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Create PDF
output_path = os.path.join(os.getcwd(), "Paul_Ciorogar_CV_20260806.pdf")
doc = SimpleDocTemplate(
    output_path,
    pagesize=letter,
    rightMargin=0.75*inch,
    leftMargin=0.75*inch,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch
)

# Styles
styles = getSampleStyleSheet()
story = []

# Custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor='#000000',
    spaceAfter=6,
    alignment=TA_LEFT
)

subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontSize=11,
    textColor='#666666',
    spaceAfter=12
)

section_style = ParagraphStyle(
    'Section',
    parent=styles['Heading2'],
    fontSize=14,
    textColor='#000000',
    spaceAfter=8,
    spaceBefore=12,
    leftIndent=0
)

job_title_style = ParagraphStyle(
    'JobTitle',
    parent=styles['Heading3'],
    fontSize=12,
    textColor='#000000',
    spaceAfter=2,
    spaceBefore=8
)

job_details_style = ParagraphStyle(
    'JobDetails',
    parent=styles['Normal'],
    fontSize=10,
    textColor='#666666',
    spaceAfter=6
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=10,
    textColor='#000000',
    alignment=TA_JUSTIFY,
    spaceAfter=6,
    leading=14
)

bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontSize=10,
    textColor='#000000',
    leftIndent=20,
    spaceAfter=4,
    leading=13
)

contact_style = ParagraphStyle(
    'Contact',
    parent=styles['Normal'],
    fontSize=9,
    textColor='#666666',
    spaceAfter=2
)

# Header
story.append(Paragraph("Paul Ciorogar", title_style))
story.append(Paragraph("Software Developer", subtitle_style))

# Contact Info
story.append(
    Paragraph("Sibiu, Romania | paulciorogar@gmail.com", contact_style))
story.append(Paragraph(
    "LinkedIn: linkedin.com/in/paul-ciorogar | GitHub: github.com/paul-ciorogar", contact_style))
story.append(Spacer(1, 12))

# Summary
story.append(Paragraph("SUMMARY", section_style))
story.append(Paragraph(
    "Self-taught software developer with 14+ years of professional experience "
    "Passionate about understanding how systems work from the ground up—this curiosity has driven me from "
    "web development to game development to compiler design, with each domain informing and "
    "strengthening my approach to software engineering.",
    body_style
))
story.append(Paragraph(
    "Currently developing a custom programming language (Suru) to deepen my understanding of language design and compiler "
    "implementation. I am technology agnostic and thrive on cross-pollinating ideas across domains: for example, "
    "applying game development rendering techniques to optimize CAD visualization algorithms in production systems.",
    body_style
))


# Experience
story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_style))

# Stefanini
story.append(Paragraph("Software Developer | Stefanini EMEA", job_title_style))
story.append(Paragraph(
    "October 2022 - December 2025 | Sibiu, Romania (Remote)", job_details_style))
story.append(Paragraph(
    "Contributed to the development of an internal CAD-like application for LNG (Liquefied Natural Gas) tank manufacturing "
    "on ships, working as part of a distributed team on both frontend (Windows desktop) and backend (.NET/SQL Server) components.",
    body_style
))
story.append(Paragraph("• Designed and implemented algorithms for rendering and manipulating 3D representations of LNG tank components, applying performance optimization techniques borrowed from game development to improve rendering efficiency", bullet_style))
story.append(Paragraph("• Developed material calculation algorithms that analyze 3D representations to generate accurate material requirements for tank manufacturing", bullet_style))
story.append(Paragraph("• Created space-filling optimization algorithms to determine optimal element placement for tank construction, reducing material waste", bullet_style))
story.append(Paragraph("• Collaborated directly with marine engineers to gather technical requirements and propose practical solutions for automated drawing generation for LNG tank part manufacturing", bullet_style))
story.append(Paragraph(
    "• Performed debugging, performance profiling, and refactoring of computationally intensive geometry processing code", bullet_style))
story.append(Paragraph(
    "• Contributed to both greenfield feature development and maintenance of existing critical systems", bullet_style))
story.append(Paragraph(
    "<b>Technical Environment:</b> .NET Core, C#, SQL Server, Windows Forms/WPF", bullet_style))
story.append(Spacer(1, 4))

# Page break
story.append(PageBreak())


# Consol
story.append(Paragraph("Software Engineer | Consol MENA Ltd.", job_title_style))
story.append(Paragraph(
    "November 2010 - November 2021 | Dubai, United Arab Emirates", job_details_style))
story.append(Paragraph(
    "Served as a core team member maintaining and evolving a large-scale enterprise insurance platform over 11 years, "
    "contributing to all phases of the software development lifecycle from requirements gathering to production support.",
    body_style
))
story.append(Paragraph("• Optimized critical reporting performance, reducing execution times from minutes to seconds across multiple reports over a 4-year improvement initiative. Notable achievement: reduced a complex insurance report from 15 minutes to under 15 seconds through a combination of algorithm redesign (delegating processing from ColdFusion to Java), SQL query optimization, and database architecture improvements using materialized views and temporary tables", bullet_style))
story.append(Paragraph("• Collaborated with business stakeholders to understand requirements, estimate project timelines, and architect solutions for complex insurance workflows", bullet_style))
story.append(Paragraph(
    "• Developed new features across the full stack while maintaining backward compatibility in a large, mature codebase", bullet_style))
story.append(Paragraph(
    "• Conducted code reviews and mentored team members on best practices and system architecture", bullet_style))
story.append(Paragraph(
    "• Managed release cycles and provided on-call production support, ensuring system reliability and rapid incident resolution", bullet_style))
story.append(Paragraph(
    "• Refactored legacy code to improve maintainability and performance without disrupting active business operations", bullet_style))
story.append(Paragraph(
    "• Built prototypes to validate technical approaches before full implementation", bullet_style))
story.append(Paragraph(
    "• Created and maintained technical documentation for complex system components", bullet_style))
story.append(Paragraph(
    "<b>Primary Stack:</b> ColdFusion 11, Microsoft SQL Server, JavaScript, HTML/CSS, TypeScript", bullet_style))
story.append(Paragraph(
    "<b>Frontend Frameworks:</b> Sencha Touch, ExtJS, jQuery, Bootstrap, AngularJS, Angular", bullet_style))
story.append(Paragraph(
    "<b>Mobile:</b> PhoneGap/Cordova for cross-platform mobile applications", bullet_style))
story.append(Paragraph(
    "<b>Backend & Databases:</b> Node.js, Java, C#, Oracle DB, MySQL, PHP, Perl, Groovy", bullet_style))
story.append(Paragraph(
    "<b>Tools & Infrastructure:</b> Git, Subversion, Ant, Docker, SASS", bullet_style))

# Technical Projects
story.append(Paragraph("TECHNICAL PROJECTS", section_style))
story.append(Paragraph(
    "<b>Suru Programming Language</b> | Personal Project | 2024-Present", job_title_style))
story.append(Paragraph(
    "• Designing and implementing a custom programming language from scratch to explore compiler theory and language design", bullet_style))
story.append(Paragraph(
    "• Building lexer, parser, and interpreter components in C#", bullet_style))
story.append(Paragraph(
    "• Available on GitHub: github.com/paul-ciorogar/suru-lang", bullet_style))
story.append(Spacer(1, 8))

# Build PDF
doc.build(story)
print(f"PDF created successfully: {output_path}")
