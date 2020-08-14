---
title: Investigar
permalink: "/investigar.html"
layout: page
subtitle: Artículos, libros, informes y otras publicaciones
color: bg-dark
---

{:.no_toc}
### Índice

- The generated Toc will be an ordered list
{:toc}

* * *

A lo largo de **mi trayectoria investigadora** me he centrado en estudiar la transformación de la industria periodística. Desde hace una década, estoy enfocado en los procesos de innovación en periodismo, especialmente en la búsqueda de modelos de negocio sostenibles. Durante estos años he publicado numerosos estudios sobre esas materias, lo que me ha servido para obtener dos sexenios de investigación CNEAI (2007-2012, 2013-2018) y presentar los siguientes resultados:

- Más de **40** publicaciones científicas
  - **19** artículos de revistas indexadas
      - **11** en revistas situadas en los niveles 1 y 2 **(JCR y SJR)** 
      - **5** en niveles 3 y 4 **(SJR, Latindex, CIRCE)**
  - **26** publicaciones en libros o capítulos
      - **8** en editoriales recogidas en **Scholarly Publishers Indicators (SPI)**  

**Mis investigaciones tienen impacto**, como se puede apreciar en un alto índice H (11) en Google Académico, con un total de 857 citas y un índice H en SCOPUS (5) de un total de 9 publicaciones con 164 citas desde 2009 a 2019. De las 40 publicaciones, 19 son artículos de revistas de referencia: 11 en los "niveles 1 y 2" y 5 en "niveles 3 y 4". 

**Además, he presentado comunicaciones a 23 congresos** (13 nacionales y 10 internacionales). Estos trabajos son fruto de mi **participación en proyectos de I+D+i** , de los cuales 6 han sido en concurrencia competitiva en instituciones de ámbito nacional (4) y europeo (2). Además, he realizado una **estancia de investigación postdoctoral en Nueva York** en el Centro Donald McGannon de la Universidad de Fordham (2010), financiada por el Programa José Castillejo. 

Aparte, soy miembro de la **Red de Excelencia del Ciberperiodismo**, evaluador de ANEP y pertenezco a la Asociación Española de Investigación en la Comunicación (AE-IC) y a la Association for Education in Journalism and Mass Communication (AEJMC).

He liderado e ideado junto al equipo del GICOV la creación del **Ranking de Innovación en Periodismo**, estudio que ha generado una fecunda línea de investigación dentro del Grupo de Investigación de la Comunicación (GICOV), al que pertenezco desde su fundación. Esta línea ha fructificado en publicaciones sobre innovación en periodismo en revistas de impacto como **El Profesional de la Información**, **Journalism Studies**, **Observatorio** y **Revista Latina**. Además, ha contribuido a la disciplina con una metodología de estudio innovadora, herramienta que emplean en tesis doctorales de diversas universidades.

* * *

### Artículos en revistas científicas indexadas (21) 

{% for articulos in site.data.articulos %}
{{ articulos.autores }} (**{{ articulos.ano }}**). "{{ articulos.titulo }}", _{{ articulos.revista }}_, {{ articulos.volumen }}, pp. {{ articulos.desde }}-{{ articulos.hasta }}, [DOI ↗️]({{ articulos.doi }}){:target="_blank"}.
{% endfor %}


CARVAJAL, Miguel (**2012**). "Nuevos modelos de financiación para el reporterismo", Naukowy Przegląd Dziennikarski / Journalism Research Review Quarterly, pp. 101-110. 

### Libros (6) y capítulos de libros (20)

{% for libros in site.data.libros %}
{{ libros.autores }} (**{{ libros.ano }}**). _{{ libros.titulo }}_, publicado en editorial {{ libros.editorial }}, {{ libros.ciudad }}, {{ libros.paginas }} páginas, ISBN: {{ libros.ISBN }}, SPI: {{ libros.SPI }}.
{% endfor %}

**Capítulos** de libros:

{% for capitulos in site.data.capitulos %}
{{ capitulos.autores }} (**{{ capitulos.ano }}**). En _{{ capitulos.titulo }}_, publicado en editorial {{ capitulos.editorial }}, pp. {{ capitulos.paginas }}, ISBN: {{ capitulos.ISBN }}, SPI: {{ capitulos.SPI }}.
{% endfor %}

### Miembro de comités científicos de congresos (14)

<ol>
{% for comites in site.data.comites %}
  <li>
    <p><strong>{{ comites.fecha }} - {{ comites.clave }} científico </strong> en <em>{{ comites.titulo }}</em>, celebrado en {{ comites.sede }}, {{ comites.ciudad }}.</p>
  </li>
{% endfor %}
</ol>

### Comunicaciones en congresos científicos (25)

<ol>
{% for congresos in site.data.congresos %}
  <li>
    <p><strong>{{ congresos.fecha }} - {{ congresos.clave }}</strong>. {{ congresos.autor }} en <em>{{ congresos.titulo }}</em>, celebrado en {{ congresos.sede }}, {{ congresos.ciudad }}.</p>
  </li>
{% endfor %}
</ol>

### Conferencias y seminarios impartidas (9)

<ol>
{% for seminarios in site.data.seminarios %}
  <li>
    <p><strong>{{ seminarios.fecha }} - {{ seminarios.clave }}</strong>. {{ seminarios.autores }} con el título <em>{{ seminarios.paper }}</em>, celebrado en {{ seminarios.sede }}.</p>
  </li>
{% endfor %}
</ol>

### Participación en congresos (8)

- **2010 - MODERADOR** en el I Congreso Internacional de Comunicación y Publicidad, celebrado en la Universidad Miguel Hernández de Elche. 
- **2018 - MODERADOR** en Comunica2: VIII Congreso Internacional sobre redes sociales, celebrado en la Universitat Politècnica de València. 
- **2014 - MODERADOR** en el "XV Congreso de Periodismo Digital", celebrado en Huesca y organizado por la Asociación de Prensa de Aragón. 
- **2009 - MODERADOR** en las XXII Jornadas de El Nuevo Lunes de la Asociación de Prensa de Alicante.
- **2000 - ASISTENCIA** a las "XV Jornadas Internacionales de Comunicación, celebradas en la Universidad de Navarra. 
- **2011 - ASISTENCIA** al "Seminario Humanidades Digitales" celebrado en la UMH.
- **2015 - ASISTENCIA** al "II Seminario de Periodismo Emprendedor", organizado por la FAPE. 
- **2016 - ASISTENCIA** en calidad de ponente a la actividad de trabajo del Proyecto MAPCOM en la Universitat Pompeu Fabra.

### Proyectos (9)

**Participación en proyectos de investigación competitivos del Plan Nacional I+D+i o similar**. He participado en 9 proyectos de investigación, de los cuales 6 han sido en concurrencia competitiva en instituciones de ámbito nacional y/o europeo correspondientes al Plan Nacional de I+D+i (4) o similar a nivel europeo (2). 

<ol>
{% for proyectos in site.data.proyectos %}
  <li>
    <p><strong>{{ proyectos.anos }} - {{ proyectos.referencia }}</strong>. <em>{{ proyectos.titulo }}</em>, financiado por <strong>{{ proyectos.entidad }}</strong> con {{ proyectos.cuantia }}. Equipo de trabajo: {{ proyectos.equipo }} investigadores. Investigador principal: {{ proyectos.ip }}.</p>
  </li>
{% endfor %}
</ol>

### Estancias de investigación en el extranjero

**He realizado una estancia de investigación postdoctoral** financiada por el Programa José Castillejo en el Centro Donald McGannon de la Universidad de Fordham (2010), bajo la supervisión del profesor **Philip Napoli**. 

**También disfruté de una estancia pre-doctoral** con la beca FPU (Ayudas para la formación de profesorado universitario) en la **Universidad de Westminster**, bajo la supervisión del profesor **Colin Sparks**, durante 4 meses, entre junio y septiembre de 2004. 

## Otros méritos de investigación

**Reseñas de libros publicadas en revistas científicas**

- **2018 - Reseña** de "Redondo, M. Verificación digital para periodistas. Manual contra bulos y desinformación internacional. Barcelona: Editorial UOC, 2018, 172 páginas. ISBN: 9788491801290" en la revista Quaderns del CAC 44, vol. XXI, julio 2018 (95-96), ISSN: 2014-2242.
- **2008 - Reseña** de "Efrén CUEVAS y Alberto N. GARCÍA (eds.). Landscapes of the Self: The Cinema of Ross McElwee/ Paisajes del yo: El Cine de Ross McElwee. Ediciones Internacionales Universitarias (Eiunsa), Madrid, 2007, 331 pp." en la revista Comunicación y Sociedad, ISSN: 0214-0039, Diciembre, 2008. 
- **2003 - Reseña** de "Ángel ARRESE. Empresa informativa y mercados de la comunicación. Estudios en honor del Profesor Alfonso Nieto Tamargo. Eunsa, Pamplona, 2002, 530 pp." en la revista Comunicación y Sociedad, ISSN: 0214-0039, Nº 2, 2003.

**Informes relacionados con proyectos de investigación**

- **2018 - Coautor**. "Informe sobre la situación actual y perspectivas del periodismo valenciano en la era digital, elaborado por la Comisión Jurídica del Consell Valenciano de Cultura", resultado de mi colaboración como experto consultivo.
- **2014 - Coautor**. "Ranking de Innovación Periodística 2014", elaborado con el equipo del GICOV, resultado de un proyecto de I+D+i financiado por el Ministerio de Ciencia e Innovación.
- **2009 - Coautor**. "Newsroom Convergence – A transnational comparison", para Medienhaus Wien, resultado de un proyecto de I+D+i financiado por la Asociación de Prensa Austríaca. 
- **2008 - Coautor**. "Newsroom convergence in multimedia organisations in Spain and Austria: quality models in the production of news", resultado de un proyecto de I+D+i financiado por el programa de Acciones Integradas del Ministerio de Ciencia e Innovación. 
- **2002 - Coautor**. Informe "GLOBALISATION OF THE MEDIA INDUSTRY AND POSSIBLE THREATS TO CULTURAL DIVERSITY (Final Study)" para el Parlamento Europeo (STOA Panel), resultado de un proyecto de I+D+i. 

**Evaluaciones positivas sobre la trayectoria investigadora**. Tengo reconocido dos sexenios (2007-2012, 2013-2018). Además, he solicitado un sexenio de transferencia para el período 2013-2018 en la convocatoria extraordinaria realizada por CNEAI este año.

**Premios relacionados con la calidad investigadora**. El Plan de Excelencia y Competitividad de la Universidad Miguel Hernández de Elche 2014-2018 pretende aumentar su capacidad formativa, mejorar del talento docente, incrementar la generación de conocimiento y la competitividad de sus recursos humanos, desarrollar su proyección internacional e acrecentar su impacto en el sector socio-económico. Por eso, reconoce la implicación a los profesores que alcancen la excelencia investigadora mediante la concesión de premios, que recibirán la denominación Premios UMH a la Productividad Investigadora. En esta categoría he recibido los siguientes: 

- 2014 - Premio UMH 2014 a la Productividad Investigadora.
- 2015 - Premio UMH 2015 a la Productividad Investigadora.
- 2016 - Premio UMH 2016 a la Productividad Investigadora.
- 2018 - Premio UMH 2018 a la Productividad Investigadora. 

**He sido miembro evaluador de 13 tribunales de Tesis Doctorales**. He participado además en los siguientes comités y tribunales científicos. 

- 2017 - (actualidad) MIEMBRO del Banco de Expertos de la AGENCIA ESTATAL DE INVESTIGACIÓN. 
- 2009 - (actualidad) MIEMBRO del GICOV (Grupo de Investigación de la Comunicación en la Universidad Miguel Hernández).
- 2008 - (actualidad) MIEMBRO de la Asociación Española de Investigación en Comunicación (AE - IC). 
- 2012 - (actualidad) MIEMBRO de comité científico de la revista polaca NAUKOWY PRZEGLAD DZIENNIKARSKI. 
- 2018 - PONENTE en la Comisión de la Promoción Cultural del Consell Valenciá de Cultura para la elaboración del "Informe sobre la prensa valenciana".

**He evaluado artículos científicos en revistas indexadas**, como Comunicación y Sociedad (SCOPUS), Revista Latina (Scopus), Sphera (Latindex), Revista Mediterránea (Latindex), CUADERNOS.INFO, Journalism Practice (JCR), y Revista de Comunicación.
