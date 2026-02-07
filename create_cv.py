from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

fileName = "/home/paul/Documents/Paul_Ciorogar_CV_2026.pdf"

# Create PDF
doc = SimpleDocTemplate(
    fileName,
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
    "LinkedIn: linkedin.com/in/paul-ciorogar | GitHub: github.com/paul-ciorogar | LeetCode: leetcode.com/paulciorogar", contact_style))
story.append(Spacer(1, 12))

# Summary
story.append(Paragraph("SUMMARY", section_style))
story.append(Paragraph(
    "Self-taught software developer with 14+ years of professional experience building scalable backend systems, "
    "optimizing performance-critical algorithms, and solving complex technical challenges. Passionate about understanding "
    "how systems work from the ground up—this curiosity has driven me from web development to game development to compiler "
    "design, with each domain informing and strengthening my approach to software engineering.",
    body_style
))
story.append(Paragraph(
    "Currently developing a custom programming language (Suru) to deepen my understanding of language design and compiler "
    "implementation. I thrive on cross-pollinating ideas across domains: for example, applying game development rendering "
    "techniques to optimize CAD visualization algorithms in production systems.",
    body_style
))
story.append(Paragraph(
    "Strong foundation in .NET ecosystems, database optimization, algorithm design, and delivering maintainable solutions "
    "for complex business requirements. Equally comfortable working independently or collaborating with engineering teams to "
    "translate requirements into robust technical implementations.",
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
    "<b>Technical Environment:</b> .NET Core, C#, SQL Server, Windows Forms/WPF, computational geometry, algorithm optimization", bullet_style))
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
story.append(Paragraph("• <b>Optimized critical reporting performance</b>, reducing execution times from minutes to seconds across multiple reports over a 4-year improvement initiative. Notable achievement: reduced a complex insurance report from 15 minutes to under 15 seconds through a combination of algorithm redesign (delegating processing from ColdFusion to Java), SQL query optimization, and database architecture improvements using materialized views and temporary tables", bullet_style))
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
    "<b>Primary Stack:</b> ColdFusion 11, Microsoft SQL Server, JavaScript, HTML/CSS", bullet_style))
story.append(Paragraph(
    "<b>Frontend Frameworks:</b> Sencha Touch, ExtJS, jQuery, Bootstrap, AngularJS, Angular, TypeScript", bullet_style))
story.append(Paragraph(
    "<b>Mobile:</b> PhoneGap/Cordova for cross-platform mobile applications", bullet_style))
story.append(Paragraph(
    "<b>Backend & Databases:</b> Node.js, Java, C#, Oracle DB, MySQL, PHP, Perl, Groovy", bullet_style))
story.append(Paragraph(
    "<b>Tools & Infrastructure:</b> Git, Subversion, Ant, Docker, SASS", bullet_style))

# Page break
story.append(PageBreak())

# Technical Projects
story.append(Paragraph("TECHNICAL PROJECTS", section_style))
story.append(Paragraph(
    "<b>Suru Programming Language</b> | Personal Project | 2024-Present", job_title_style))
story.append(Paragraph(
    "• Designing and implementing a custom programming language from scratch to explore compiler theory and language design", bullet_style))
story.append(Paragraph(
    "• Building lexer, parser, and interpreter components in Rust", bullet_style))
story.append(Paragraph(
    "• Available on GitHub: github.com/paul-ciorogar/suru-lang", bullet_style))
story.append(Spacer(1, 8))

# Skills
story.append(Paragraph("TECHNICAL SKILLS", section_style))
story.append(Paragraph("<b>Core Competencies:</b>", body_style))
story.append(Paragraph(
    "• Backend Development: .NET Core, C#, SQL Server, database optimization", bullet_style))
story.append(Paragraph(
    "• Algorithm Design: computational geometry, optimization algorithms, performance tuning", bullet_style))
story.append(Paragraph(
    "• Full-Stack Development: JavaScript/TypeScript, modern web frameworks, REST APIs", bullet_style))
story.append(Paragraph(
    "• Software Engineering: object-oriented design, debugging, refactoring, code review", bullet_style))
story.append(Paragraph(
    "• Domain Knowledge: insurance systems, CAD/manufacturing workflows, enterprise applications", bullet_style))
story.append(Spacer(1, 6))

story.append(Paragraph("<b>Technical Breadth:</b>", body_style))
story.append(Paragraph(
    "• <b>Languages:</b> C#, JavaScript/TypeScript, SQL, Java, Rust, C/C++, Python, PHP, Perl", bullet_style))
story.append(Paragraph(
    "• <b>Frameworks:</b> .NET Core, Angular, Node.js, ExtJS, Bootstrap", bullet_style))
story.append(
    Paragraph("• <b>Databases:</b> SQL Server, Oracle, MySQL", bullet_style))
story.append(Paragraph(
    "• <b>Tools:</b> Git, Docker, Visual Studio, debugging/profiling tools", bullet_style))
story.append(Paragraph(
    "• <b>Cross-domain experience:</b> web development, game development concepts, compiler development", bullet_style))
story.append(Spacer(1, 8))

# Certifications
story.append(Paragraph("CERTIFICATIONS & LEARNING", section_style))
story.append(Paragraph("• Master C Language Pointers", bullet_style))
story.append(Paragraph("• Object-Oriented Programming with C#", bullet_style))
story.append(Paragraph(
    "• Docker for Developers: Create and Manage Docker Containers", bullet_style))
story.append(Paragraph("• Learning Python", bullet_style))
story.append(Paragraph("• AWS Essential Training for Developers", bullet_style))

# Build PDF
doc.build(story)
print("PDF created successfully: ", fileName)
