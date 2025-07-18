"""
Front page content components for the Lotto6aus49 application.

This module contains all front page specific components including:
- Hero sections
- Feature grids
- Analysis previews
- Service sections
- News sections
"""

import reflex as rx
import reflex_clerk_api as reclerk


def front_page_hero_section() -> rx.Component:
    """
    Main hero section with primary heading and value proposition.
    
    Uses content from 01_front_page_index_text.md for the welcome message
    and key benefits. Includes conditional CTA based on auth status.
    """
    return rx.section(
        rx.container(
            rx.vstack(
                # Main heading
                rx.heading(
                    "Willkommen bei der modernsten LOTTO 6aus49 Analyse-Plattform!",
                    size="9",
                    weight="bold",
                    text_align="center",
                    color="gray.800",
                    max_width="800px",
                ),
                
                # Subtitle/description
                rx.text(
                    "Entdecken Sie die Macht der Datenanalyse für das deutsche Lotto 6aus49. "
                    "Unsere innovative Plattform bietet Ihnen professionelle Werkzeuge zur Analyse "
                    "historischer Lottozahlen, intelligente Simulationen und fortschrittliche "
                    "Machine Learning-Algorithmen für fundierte Vorhersagen.",
                    size="5",
                    text_align="center",
                    color="gray.600",
                    max_width="700px",
                    line_height="1.6",
                ),
                
                # CTA Buttons - conditional based on auth status
                rx.hstack(
                    reclerk.signed_out(
                        rx.hstack(
                            rx.link(
                                rx.button(
                                    "🚀 Jetzt kostenlos registrieren!",
                                    size="4",
                                    bg="blue.500",
                                    color="white",
                                    _hover={"bg": "blue.600"},
                                    padding="1.5em 2em",
                                ),
                                href="/registrieren",
                            ),
                            rx.link(
                                rx.button(
                                    "📊 Öffentliche Analysen ansehen",
                                    size="4",
                                    variant="outline",
                                    color="blue.500",
                                    border_color="blue.500",
                                    _hover={"bg": "blue.50"},
                                    padding="1.5em 2em",
                                ),
                                href="#public-analysis",
                            ),
                            spacing="4",
                            flex_direction=["column", "column", "row"],
                        )
                    ),
                    reclerk.signed_in(
                        rx.hstack(
                            rx.link(
                                rx.button(
                                    "🎯 Zum Dashboard",
                                    size="4",
                                    bg="green.500",
                                    color="white",
                                    _hover={"bg": "green.600"},
                                    padding="1.5em 2em",
                                ),
                                href="/dashboard",
                            ),
                            rx.link(
                                rx.button(
                                    "🔍 Neue Analyse starten",
                                    size="4",
                                    variant="outline",
                                    color="green.500",
                                    border_color="green.500",
                                    _hover={"bg": "green.50"},
                                    padding="1.5em 2em",
                                ),
                                href="/analyse",
                            ),
                            spacing="4",
                            flex_direction=["column", "column", "row"],
                        )
                    ),
                    justify="center",
                ),
                
                spacing="6",
                align="center",
                padding_y="4em",
                max_width="900px",
                margin="0 auto",
            ),
        ),
        bg="linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%)",
        width="100%",
    )


def front_page_frequency_analysis_preview() -> rx.Component:
    """
    Preview section showing frequency analysis with placeholder chart.
    
    Features top numbers display and a placeholder bar chart as shown
    in the design sketch.
    """
    return rx.section(
        rx.container(
            rx.vstack(
                # Section heading
                rx.heading(
                    "📊 Aktuelle Häufigkeitsanalyse",
                    size="7",
                    weight="bold",
                    text_align="center",
                    color="gray.800",
                ),
                
                rx.text(
                    "Die meistgezogenen Zahlen der letzten 100 Ziehungen",
                    size="4",
                    text_align="center",
                    color="gray.600",
                ),
                
                # Content grid: Top Numbers + Chart
                rx.grid(
                    # Top Numbers Section
                    rx.card(
                        rx.vstack(
                            rx.heading("Top Zahlen", size="5", color="blue.600"),
                            rx.grid(
                                # Placeholder top numbers
                                *[
                                    rx.box(
                                        rx.text(
                                            str(num),
                                            size="4",
                                            weight="bold",
                                            color="white",
                                        ),
                                        bg="blue.500",
                                        border_radius="50%",
                                        width="3em",
                                        height="3em",
                                        display="flex",
                                        align_items="center",
                                        justify_content="center",
                                    ) for num in [7, 12, 16, 19, 30, 36]
                                ],
                                columns="3",
                                spacing="3",
                                justify="center",
                            ),
                            spacing="4",
                            align="center",
                        ),
                        size="3",
                    ),
                    
                    # Chart Placeholder Section
                    rx.card(
                        rx.vstack(
                            rx.heading("Häufigkeits-Diagramm", size="5", color="green.600"),
                            rx.box(
                                rx.text(
                                    "📊 Interaktives Balkendiagramm",
                                    size="3",
                                    color="gray.500",
                                ),
                                bg="gray.50",
                                border="2px dashed",
                                border_color="gray.300",
                                border_radius="md",
                                padding="4em 2em",
                                text_align="center",
                                width="100%",
                                min_height="200px",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                            ),
                            spacing="4",
                            align="center",
                        ),
                        size="3",
                    ),
                    
                    columns="2",  # Responsive: 2 columns
                    spacing="6",
                    width="100%",
                ),
                
                # Link to full analysis
                reclerk.signed_out(
                    rx.link(
                        rx.button(
                            "🔍 Vollständige Analyse anzeigen (Registrierung erforderlich)",
                            variant="outline",
                            size="3",
                            color="blue.500",
                            border_color="blue.500",
                            _hover={"bg": "blue.50"},
                        ),
                        href="/registrieren",
                    )
                ),
                reclerk.signed_in(
                    rx.link(
                        rx.button(
                            "🔍 Zur detaillierten Häufigkeitsanalyse",
                            variant="solid",
                            size="3",
                            bg="blue.500",
                            color="white",
                            _hover={"bg": "blue.600"},
                        ),
                        href="/analysen/haeufigkeit",
                    )
                ),
                
                spacing="6",
                align="center",
                padding_y="4em",
            ),
        ),
        id="public-analysis",
    )


def front_page_collapsible_info() -> rx.Component:
    """
    Collapsible section with detailed platform information.
    
    Uses content from 01_front_page_index_text.md in an expandable format
    as shown in the design sketch.
    """
    return rx.section(
        rx.container(
            rx.vstack(
                # Collapsible content about LottoAmSamstag
                rx.accordion.root(
                    rx.accordion.item(
                        rx.accordion.trigger(
                            rx.hstack(
                                rx.heading(
                                    "🎯 Was erwartet Sie bei LottoAmSamstag?",
                                    size="6",
                                    color="blue.600",
                                    weight="bold",
                                ),
                                rx.icon("chevron-down", size=20, color="blue.600"),
                                justify="between",
                                align="center",
                                width="100%",
                                cursor="pointer",
                                _hover={"color": "blue.700"},
                            ),
                            padding="1em",
                            bg="blue.50",
                            border_radius="md",
                            border="1px solid",
                            border_color="blue.200",
                        ),
                        rx.accordion.content(
                        rx.vstack(
                            # Public Features
                            rx.box(
                                rx.heading("Für alle Besucher verfügbar:", size="5", color="gray.700", margin_bottom="3"),
                                rx.unordered_list(
                                    rx.list_item("Aktuelle Häufigkeitsanalyse der meistgezogenen Zahlen"),
                                    rx.list_item("Interaktive Diagramme und Visualisierungen"),
                                    rx.list_item("Übersicht über die neuesten Ziehungsergebnisse"),
                                    rx.list_item("Grundlegende Statistiken und Trends"),
                                    color="gray.600",
                                    spacing="2",
                                ),
                            ),
                            
                            # Premium Features
                            rx.box(
                                rx.heading("Exklusiv für registrierte Nutzer:", size="5", color="green.700", margin_bottom="3"),
                                
                                # Dashboard
                                rx.box(
                                    rx.heading("📊 Persönliches Dashboard", size="4", color="green.600"),
                                    rx.text("Ihr zentraler Bereich für alle Analysefunktionen mit personalisierter Übersicht über Ihre Aktivitäten und Favoriten.", color="gray.600"),
                                    margin_bottom="4",
                                ),
                                
                                # Analysis Tools
                                rx.box(
                                    rx.heading("🔍 Erweiterte Analyse-Tools", size="4", color="green.600"),
                                    rx.unordered_list(
                                        rx.list_item("Häufigkeitsanalyse: Identifizieren Sie die meistgezogenen Zahlen verschiedener Zeiträume"),
                                        rx.list_item("Seltene Zahlen: Entdecken Sie unterrepräsentierte Nummern mit Potenzial"),
                                        rx.list_item("Überfällige Zahlen: Analysieren Sie Zahlen, die schon lange nicht mehr gezogen wurden"),
                                        rx.list_item("Musteranalyse: Erkennen Sie wiederkehrende Zahlenkombinationen und Sequenzen"),
                                        color="gray.600",
                                        spacing="1",
                                    ),
                                    margin_bottom="4",
                                ),
                                
                                # Simulations
                                rx.box(
                                    rx.heading("🎲 Intelligente Simulationen", size="4", color="green.600"),
                                    rx.unordered_list(
                                        rx.list_item("Frequenz-basierte Zahlengenerierung"),
                                        rx.list_item("Überfälligkeits-Simulationen"),
                                        rx.list_item("Zufalls-Algorithmen"),
                                        rx.list_item("Kombinierte Strategien für optimierte Ergebnisse"),
                                        color="gray.600",
                                        spacing="1",
                                    ),
                                    margin_bottom="4",
                                ),
                                
                                # ML Features
                                rx.box(
                                    rx.heading("🤖 Machine Learning Vorhersagen", size="4", color="green.600"),
                                    rx.unordered_list(
                                        rx.list_item("KI-gestützte Zahlenprognosen"),
                                        rx.list_item("Mustererkennung in historischen Daten"),
                                        rx.list_item("Predictive Analytics für zukünftige Ziehungen"),
                                        rx.list_item("Personalisierte Empfehlungen"),
                                        color="gray.600",
                                        spacing="1",
                                    ),
                                    margin_bottom="4",
                                ),
                                
                                # Data Management
                                rx.box(
                                    rx.heading("📈 Datenmanagement", size="4", color="green.600"),
                                    rx.unordered_list(
                                        rx.list_item("CSV-Import historischer Ziehungsdaten"),
                                        rx.list_item("Persönliche Statistiken und Verlauf"),
                                        rx.list_item("Export-Funktionen für Ihre Analysen"),
                                        rx.list_item("Favoriten-Management"),
                                        color="gray.600",
                                        spacing="1",
                                    ),
                                ),
                            ),
                            
                            spacing="6",
                        ),
                        padding="2em",
                        bg="white",
                        border="1px solid",
                        border_color="gray.200",
                        border_radius="md",
                        margin_top="0",
                    ),
                    value="info",
                ),
                collapsible=True,
                width="100%",
            ),
                
                spacing="4",
                padding_y="3em",
            ),
        ),
    )


def front_page_services_grid() -> rx.Component:
    """
    Services grid section as shown in design sketch.
    
    Two service cards highlighting key platform features.
    """
    return rx.section(
        rx.container(
            rx.vstack(
                rx.heading(
                    "🌟 Unsere Hauptservices",
                    size="7",
                    weight="bold",
                    text_align="center",
                    color="gray.800",
                ),
                
                rx.grid(
                    # Service 1 - Analysis
                    rx.card(
                        rx.vstack(
                            rx.icon("bar-chart-4", size=40, color="blue.500"),
                            rx.heading("Professionelle Analyse", size="5", color="blue.600"),
                            rx.text(
                                "Modernste Algorithmen für die Analyse historischer Lottozahlen. "
                                "Identifizieren Sie Patterns, Trends und statistische Anomalien.",
                                text_align="center",
                                color="gray.600",
                                line_height="1.5",
                            ),
                            rx.unordered_list(
                                rx.list_item("Häufigkeitsanalyse"),
                                rx.list_item("Überfällige Zahlen"),
                                rx.list_item("Musteranalyse"),
                                rx.list_item("Statistische Visualisierung"),
                                color="gray.600",
                                text_align="left",
                            ),
                            spacing="4",
                            align="center",
                        ),
                        size="3",
                        _hover={"transform": "translateY(-5px)", "box_shadow": "lg"},
                        transition="all 0.3s ease",
                    ),
                    
                    # Service 2 - Simulations
                    rx.card(
                        rx.vstack(
                            rx.icon("dice-6", size=40, color="green.500"),
                            rx.heading("Intelligente Simulationen", size="5", color="green.600"),
                            rx.text(
                                "KI-gestützte Simulationen und Vorhersagemodelle für optimierte "
                                "Lotto-Strategien basierend auf wissenschaftlichen Methoden.",
                                text_align="center",
                                color="gray.600",
                                line_height="1.5",
                            ),
                            rx.unordered_list(
                                rx.list_item("Monte Carlo Simulationen"),
                                rx.list_item("Frequenz-basierte Generierung"),
                                rx.list_item("Machine Learning Prognosen"),
                                rx.list_item("Kombinierte Strategien"),
                                color="gray.600",
                                text_align="left",
                            ),
                            spacing="4",
                            align="center",
                        ),
                        size="3",
                        _hover={"transform": "translateY(-5px)", "box_shadow": "lg"},
                        transition="all 0.3s ease",
                    ),
                    
                    columns="2",
                    spacing="6",
                    width="100%",
                ),
                
                spacing="6",
                padding_y="4em",
            ),
        ),
        bg="gray.50",
    )


def front_page_news_section() -> rx.Component:
    """
    News section with placeholder news items as shown in design.
    
    Four news items in a grid layout for latest updates and announcements.
    """
    return rx.section(
        rx.container(
            rx.vstack(
                rx.heading(
                    "📰 Neueste Updates",
                    size="7",
                    weight="bold",
                    text_align="center",
                    color="gray.800",
                ),
                
                rx.grid(
                    # News Item 1
                    rx.card(
                        rx.vstack(
                            rx.heading("Neue ML-Algorithmen", size="4", color="blue.600"),
                            rx.text(
                                "Unsere neuesten Machine Learning-Modelle bieten noch präzisere Vorhersagen...",
                                color="gray.600",
                                size="3",
                            ),
                            rx.text("15. Juli 2025", size="2", color="gray.500"),
                            spacing="2",
                            align="start",
                        ),
                        size="2",
                    ),
                    
                    # News Item 2
                    rx.card(
                        rx.vstack(
                            rx.heading("Dashboard Update", size="4", color="green.600"),
                            rx.text(
                                "Das Benutzer-Dashboard wurde mit neuen Funktionen erweitert...",
                                color="gray.600",
                                size="3",
                            ),
                            rx.text("12. Juli 2025", size="2", color="gray.500"),
                            spacing="2",
                            align="start",
                        ),
                        size="2",
                    ),
                    
                    # News Item 3
                    rx.card(
                        rx.vstack(
                            rx.heading("Mobile App", size="4", color="purple.600"),
                            rx.text(
                                "Die mobile Version der Plattform ist jetzt verfügbar...",
                                color="gray.600",
                                size="3",
                            ),
                            rx.text("10. Juli 2025", size="2", color="gray.500"),
                            spacing="2",
                            align="start",
                        ),
                        size="2",
                    ),
                    
                    # News Item 4
                    rx.card(
                        rx.vstack(
                            rx.heading("API Release", size="4", color="orange.600"),
                            rx.text(
                                "Entwickler können jetzt unsere Analyse-API nutzen...",
                                color="gray.600",
                                size="3",
                            ),
                            rx.text("8. Juli 2025", size="2", color="gray.500"),
                            spacing="2",
                            align="start",
                        ),
                        size="2",
                    ),
                    
                    columns="4",  # Responsive grid
                    spacing="4",
                    width="100%",
                ),
                
                spacing="6",
                padding_y="4em",
            ),
        ),
    )


def front_page_why_platform() -> rx.Component:
    """
    Platform benefits section using content from 01_front_page_index_text.md.
    
    Highlights key reasons to choose the platform with checkmarks.
    """
    return rx.section(
        rx.container(
            rx.vstack(
                rx.heading(
                    "🌟 Warum unsere Plattform?",
                    size="7",
                    weight="bold",
                    text_align="center",
                    color="gray.800",
                ),
                
                rx.grid(
                    # Benefits list
                    *[
                        rx.hstack(
                            rx.icon("check-circle", size=24, color="green.500"),
                            rx.text(
                                benefit,
                                size="4",
                                color="gray.700",
                                weight="medium",
                            ),
                            spacing="3",
                            align="center",
                        ) for benefit in [
                            "Professionelle Datenanalyse mit modernsten Algorithmen",
                            "Benutzerfreundliche Oberfläche komplett in deutscher Sprache",
                            "Sichere Authentifizierung für den Schutz Ihrer Daten",
                            "Responsive Design für Desktop und Mobile",
                            "Regelmäßige Updates mit den neuesten Ziehungsergebnissen",
                            "Datenschutz-konform nach deutschen Standards"
                        ]
                    ],
                    columns="1",
                    spacing="4",
                    width="100%",
                    max_width="600px",
                ),
                
                spacing="6",
                align="center",
                padding_y="4em",
            ),
        ),
        bg="green.50",
    )


def front_page_quick_access() -> rx.Component:
    """
    Quick access section for different user types.
    
    Based on content from 01_front_page_index_text.md quick access section.
    """
    return rx.section(
        rx.container(
            rx.vstack(
                rx.heading(
                    "🔗 Schnellzugriff",
                    size="6",
                    weight="bold",
                    text_align="center",
                    color="gray.800",
                ),
                
                rx.grid(
                    # For Beginners
                    rx.card(
                        rx.vstack(
                            rx.icon("users", size=32, color="blue.500"),
                            rx.heading("Für Einsteiger", size="4", color="blue.600"),
                            rx.text(
                                "Schauen Sie sich unsere öffentlichen Analyseergebnisse an",
                                text_align="center",
                                color="gray.600",
                            ),
                            rx.button(
                                "Öffentliche Analysen",
                                variant="outline",
                                color="blue.500",
                                _hover={"bg": "blue.50"},
                                on_click=lambda: rx.scroll_to("#public-analysis"),
                            ),
                            spacing="3",
                            align="center",
                        ),
                        size="2",
                    ),
                    
                    # For Advanced
                    rx.card(
                        rx.vstack(
                            rx.icon("trending-up", size=32, color="green.500"),
                            rx.heading("Für Fortgeschrittene", size="4", color="green.600"),
                            rx.text(
                                "Registrieren Sie sich für erweiterte Tools",
                                text_align="center",
                                color="gray.600",
                            ),
                            rx.link(
                                rx.button(
                                    "Jetzt registrieren",
                                    bg="green.500",
                                    color="white",
                                    _hover={"bg": "green.600"},
                                ),
                                href="/registrieren",
                            ),
                            spacing="3",
                            align="center",
                        ),
                        size="2",
                    ),
                    
                    # For Experts
                    rx.card(
                        rx.vstack(
                            rx.icon("brain-circuit", size=32, color="purple.500"),
                            rx.heading("Für Experten", size="4", color="purple.600"),
                            rx.text(
                                "Nutzen Sie unsere Machine Learning-Funktionen",
                                text_align="center",
                                color="gray.600",
                            ),
                            reclerk.signed_in(
                                rx.link(
                                    rx.button(
                                        "ML-Features",
                                        bg="purple.500",
                                        color="white",
                                        _hover={"bg": "purple.600"},
                                    ),
                                    href="/ml-features",
                                )
                            ),
                            reclerk.signed_out(
                                rx.link(
                                    rx.button(
                                        "Anmelden für ML",
                                        variant="outline",
                                        color="purple.500",
                                        _hover={"bg": "purple.50"},
                                    ),
                                    href="/anmelden",
                                )
                            ),
                            spacing="3",
                            align="center",
                        ),
                        size="2",
                    ),
                    
                    columns="3",
                    spacing="4",
                    width="100%",
                ),
                
                spacing="6",
                padding_y="4em",
            ),
        ),
    )


def front_page_contact_support() -> rx.Component:
    """
    Contact and support section.
    
    Uses content from 01_front_page_index_text.md contact section.
    """
    return rx.section(
        rx.container(
            rx.vstack(
                rx.heading(
                    "📞 Kontakt & Support",
                    size="6",
                    weight="bold",
                    text_align="center",
                    color="gray.800",
                ),
                
                rx.text(
                    "Haben Sie Fragen? Unser deutschsprachiger Support steht Ihnen gerne zur Verfügung. "
                    "Kontaktieren Sie uns über unser Kontaktformular oder per E-Mail.",
                    text_align="center",
                    color="gray.600",
                    size="4",
                    line_height="1.6",
                    max_width="600px",
                ),
                
                rx.hstack(
                    rx.link(
                        rx.button(
                            "📧 Kontaktformular",
                            variant="solid",
                            bg="blue.500",
                            color="white",
                            _hover={"bg": "blue.600"},
                        ),
                        href="/kontakt",
                    ),
                    rx.link(
                        rx.button(
                            "📋 Support-Center",
                            variant="outline",
                            color="blue.500",
                            _hover={"bg": "blue.50"},
                        ),
                        href="/support",
                    ),
                    spacing="4",
                    justify="center",
                ),
                
                spacing="6",
                align="center",
                padding_y="4em",
            ),
        ),
        bg="blue.50",
    )


def front_page_disclaimer() -> rx.Component:
    """
    Disclaimer section with responsible gaming message.
    
    Uses the disclaimer text from 01_front_page_index_text.md.
    """
    return rx.section(
        rx.container(
            rx.card(
                rx.vstack(
                    rx.heading("⚠️ Wichtiger Hinweis", size="4", color="orange.600"),
                    rx.text(
                        "Diese Plattform dient der statistischen Analyse und Unterhaltung. "
                        "Lotto ist ein Glücksspiel. Spielen Sie verantwortungsbewusst und nur "
                        "mit Geld, das Sie sich leisten können zu verlieren.",
                        text_align="center",
                        color="gray.600",
                        size="3",
                        line_height="1.5",
                    ),
                    spacing="3",
                    align="center",
                ),
                bg="orange.50",
                border="1px solid",
                border_color="orange.200",
                size="2",
                width="100%",
                max_width="600px",
                margin="0 auto",
            ),
            padding_y="3em",
        ),
    )
