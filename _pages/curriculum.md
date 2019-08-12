---
layout: page
title: Curriculum
subtitle: Resumen del CV normalizado
permalink: curriculum.html
color: bg-dark
---
{:.no_toc}
### Índice

- The generated Toc will be an ordered list
{:toc}

* * *

# Resumen

He impartido **docencia universitaria** como profesor a tiempo completo en la Universidad Miguel Hernández (UMH) desde 2006 hasta la actualidad, en total 13 años (dos quinquenios reconocidos). Además, he sido profesor en la Universidad Católica de Murcia (2005-2006) y ayudante en la Universidad de Navarra (2000-2005). 

**Mi trayectoria científica** se ha centrado en la transformación de la industria periodística, la innovación en las redacciones y la búsqueda de modelos de negocio sostenibles, con los siguientes resultados:

- **40** publicaciones científicas
  - **16** artículos de revistas indexadas
      - **11** en revistas situadas en los niveles 1 y 2 **(JCR y SJR)** 
      - **5** en niveles 3 y 4 **(SJR, Latindex, CIRCE)**
- **26** publicaciones en libros o capítulos
  - **8** en editoriales recogidas en **Scholarly Publishers Indicators (SPI)**  

**Alto índice H y elevado número de citas en Wos, SCOPUS, Eigenfactor**. Presento un alto índice H (11) en Google Académico con un total de 739 desde 2002 y un índice H en SCOPUS (5) de un total de 9 publicaciones con 164 citas desde 2009 a 2019. Presento más de 40 publicaciones, de las cuales, 16 son artículos de revistas: 11 en los "niveles 1 y 2" y 5 en "niveles 3 y 4". 

- Índice H en Google Scholar 11 (9 desde 2014)
- Índice H en SCOPUS 4
- Citas en Google Scholar 739 (464 desde 2014)
- Citas en SCOPUS 164 
- Citas en Wos 12

**Comunicación a 23 congresos: 13 nacionales y 10 internacionales**. He presentado comunicaciones en más de 30 congresos nacionales o internacionales: 18 de los cuales cuentan con comité científico y son organizados por asociaciones de referencia en periodismo o empresa informativa. Estos méritos están acreditados en el apartado [Experiencia investigadora / 4.A.5. Congresos y seminarios](#4a5-congresos).

Estos trabajos son fruto de mi **participación en proyectos de investigación competitivo Plan Nacional I+D+i o similar**, de los cuales 6 han sido en concurrencia competitiva en instituciones de ámbito nacional (4) y europeo (2). 
   
En mi trayectoria tuve la fortuna de realizar una **estancia de investigación postdoctoral en Nueva York** en el Centro Donald McGannon de la Universidad de Fordham (2010), financiada por el Programa José Castillejo. 

Además, soy miembro de la Red de Excelencia del Ciberperiodismo, evaluador de ANEP y pertenezco a la Asociación Española de Investigación en la Comunicación (AE-IC) y a la Association for Education in Journalism and Mass Communication (AEJMC).

Entre mis principales logros, destacaría el liderazgo y la ideación del **Ranking de Innovación en Periodismo**, estudio que ha generado una fecunda línea de investigación dentro del Grupo de Investigación de la Comunicación (GICOV), al que pertenezco desde su fundación. Esta línea ha fructificado en publicaciones sobre innovación en periodismo en revistas de impacto como **El Profesional de la Información**, **Journalism Studies**, **Observatorio** y **Revista Latina**. Además, ha contribuido a la disciplina con una metodología de estudio innovadora, herramienta que emplean en tesis doctorales de diversas universidades.

Esta trayectoria científica la he compatibilizado con una notable dedicación a la gestión (actualmente soy vicedecano del Grado de Periodismo y director del Máster Universitario en Innovación en Periodismo) y a la docencia. Además, siempre he intentado mantener la vinculación con la industria para transferir los resultados de mi investigación. Soy co-fundador de una spin-off (Cuatro Galgos Innovación) desde la que he participado en contratos de consultoría y formación con empresas como Vocento, Onda Regional de Murcia y TeleElx. Este enfoque me ha permitido desarrollar proyectos de innovación como el Diccionario del Cliché, Periodistas de Datos y Chejov, editor de textos, o el Local Data Lab. Por último, he sido ponente del Consel Valenciá de Cultura (2018) para una directiva sobre la situación del periodismo local.

* * *

### Artículos en revistas científicas indexadas (16) 

<ol>
{% for articulos in site.data.articulos %}
  <li>
    <p>{{ articulos.autores }} (<strong>{{ articulos.ano }}</strong>). "{{ articulos.titulo }}", <em>{{ articulos.revista }}</em>, {{ articulos.volumen }}, pp. {{ articulos.desde }}-{{ articulos.hasta }}, <a href="{{ articulos.doi }}" target="_blank">DOI ↗️</a>.</p>
  </li>
{% endfor %}
</ol>

CARVAJAL, Miguel (**2012**). "Nuevos modelos de financiación para el reporterismo", Naukowy Przegląd Dziennikarski / Journalism Research Review Quarterly, pp. 101-110. 

### Libros (6) y capítulos de libros (20)

<ol>
{% for libros in site.data.libros %}
  <li>
    <p>{{ libros.autores }} (<strong>({{ libros.ano }})</strong>. <em>{{ libros.titulo }}</em>, publicado en editorial {{ libros.editorial }}, {{ libros.ciudad }}, {{ libros.paginas }} páginas, ISBN: {{ libros.ISBN }}, SPI: {{ libros.SPI }}.</p>
  </li>
{% endfor %}
</ol>

<ol>
{% for capitulos in site.data.capitulos %}
  <li>
    <p>{{ capitulos.autores }} (<strong>{{ capitulos.ano }}</strong>). En <em>{{ capitulos.titulo }}</em>, publicado en editorial {{ capitulos.editorial }}, pp. {{ capitulos.paginas }}, ISBN: {{ capitulos.ISBN }}, SPI: {{ capitulos.SPI }}.</p>
  </li>
{% endfor %}
</ol>

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

1. **2010 - MODERADOR** en el I Congreso Internacional de Comunicación y Publicidad, celebrado en la Universidad Miguel Hernández de Elche. 
2. **2018 - MODERADOR** en Comunica2: VIII Congreso Internacional sobre redes sociales, celebrado en la Universitat Politècnica de València. 
3. **2014 - MODERADOR** en el "XV Congreso de Periodismo Digital", celebrado en Huesca y organizado por la Asociación de Prensa de Aragón. 
4. **2009 - MODERADOR** en las XXII Jornadas de El Nuevo Lunes de la Asociación de Prensa de Alicante.
5. **2000 - ASISTENCIA** a las "XV Jornadas Internacionales de Comunicación, celebradas en la Universidad de Navarra. 
6. **2011 - ASISTENCIA** al "Seminario Humanidades Digitales" celebrado en la UMH.
7. **2015 - ASISTENCIA** al "II Seminario de Periodismo Emprendedor", organizado por la FAPE. 
8. **2016 - ASISTENCIA** en calidad de ponente a la actividad de trabajo del Proyecto MAPCOM en la Universitat Pompeu Fabra.

### Otros méritos de la actividad investigadora

1. **Evaluaciones positivas sobre la trayectoria investigadora**. Tengo reconocido un sexenio (2007-2012) y estoy pendiente de la evaluación de un segundo sexenio solicitado para el período 2013-2018. Además, he solicitado un sexenio de transferencia para el período 2013-2018 en la convocatoria extraordinaria realizada por CNEAI este año.

2. **Premios relacionados con la calidad investigadora**. El Plan de Excelencia y Competitividad de la Universidad Miguel Hernández de Elche 2014-2018 pretende aumentar su capacidad formativa, mejorar del talento docente, incrementar la generación de conocimiento y la competitividad de sus recursos humanos, desarrollar su proyección internacional e acrecentar su impacto en el sector socio-económico. Por eso, reconoce la implicación a los profesores que alcancen la excelencia investigadora mediante la concesión de premios, que recibirán la denominación Premios UMH a la Productividad Investigadora. En esta categoría he recibido los siguientes: 

   - 2014 - Premio UMH 2014 a la Productividad Investigadora. [`documentación acreditativa`](/cv/docu/Investigacion_Otros_Premios_Productividad_2014.pdf){:target="_blank"}
   - 2015 - Premio UMH 2015 a la Productividad Investigadora. [`documentación acreditativa`](/cv/docu/Investigacion_Otros_Premios_Productividad_2015.pdf){:target="_blank"}
   - 2016 - Premio UMH 2016 a la Productividad Investigadora. [`documentación acreditativa`](/cv/docu/Investigacion_Otros_Premios_Productividad_2016.pdf){:target="_blank"}
   - 2018 - Premio UMH 2018 a la Productividad Investigadora. [`documentación acreditativa`](/cv/docu/Investigacion_Otros_Premios_Productividad_2018.pdf){:target="_blank"}

3. **Miembro evaluador de 13 tribunales de Tesis Doctorales**. He participado en los tribunales como titular o suplente de tesis doctorales y en Tribunales de Premio Extraordinario de Doctorado. 

4. **Otros méritos relacionados con actividad investigadora**. 

   - 2017 - (actualidad) MIEMBRO del Banco de Expertos de la AGENCIA ESTATAL DE INVESTIGACIÓN. [`documentación acreditativa`](/cv/docu/Investigacion_Otros_Experto_2017_ANEP.pdf){:target="_blank"}
   - 2009 - (actualidad) MIEMBRO del GICOV (Grupo de Investigación de la Comunicación en la Universidad Miguel Hernández). [`documentación acreditativa`](/cv/docu/Investigacion_Otros_Miembro_GICOV.pdf){:target="_blank"}
   - 2008 - (actualidad) MIEMBRO de la Asociación Española de Investigación en Comunicación (AE - IC). [`documentación acreditativa`](/cv/docu/Investigacion_Otros_Socio_2009_AEIC.pdf){:target="_blank"}
   - 2018 - PONENTE en la Comisión de la Promoción Cultural del Consell Valenciá de Cultura para la elaboración del "Informe sobre la prensa valenciana". [`documentación acreditativa`](/cv/docu/Investigacion_Otros_Asesor_2018_Consell_GVA.pdf){:target="_blank"}

5. **Evaluador de artículos científicos en revistas indexadas**. Evaluador de artículos para Comunicación y Sociedad (SCOPUS), Revista Latina (Scopus), Sphera (Latindex) y Revista Mediterránea (Latindex).

6. **Miembro del comité científico**. Formo parte desde 2012 del comité científico de la revista polaca NAUKOWY PRZEGLAD DZIENNIKARSKI. 

### Proyectos (9)

**Participación en proyectos de investigación competitivos del Plan Nacional I+D+i o similar**. He participado en 9 proyectos de investigación, de los cuales 6 han sido en concurrencia competitiva en instituciones de ámbito nacional y/o europeo correspondientes al Plan Nacional de I+D+i (4) o similar a nivel europeo (2). 

<ol>
{% for proyectos in site.data.proyectos %}
  <li>
    <p><strong>{{ proyectos.anos }} - {{ proyectos.referencia }}</strong>. <em>{{ proyectos.titulo }}</em>, financiado por <strong>{{ proyectos.entidad }}</strong> con {{ proyectos.cuantia }}. Equipo de trabajo: {{ proyectos.equipo }} investigadores. Investigador principal: {{ proyectos.ip }}. <a href="/cv/docu/{{ proyectos.docu }}" target="_blank"><code class="highlighter-rouge">documentación acreditativa</code></a>.</p>
  </li>
{% endfor %}
</ol>

### Estancias de investigación en el extranjero

1. **Estancia postdoctoral**. He realizado una estancia de investigación postdoctoral financiada por el Programa José Castillejo en el Centro Donald McGannon de la Universidad de Fordham (2010), bajo la supervisión del profesor **Philip Napoli**. 

2. **Estancia predoctoral**. Realicé una estancia pre-doctoral con la beca FPU (Ayudas para la formación de profesorado universitario) en la **Universidad de Westminster**, bajo la supervisión del profesor **Colin Sparks**, durante 4 meses, entre junio y septiembre de 2004. 

## Otros méritos de investigación

1. **Reseñas de libros publicadas en revistas científicas**

	- **2018 - Reseña** de "Redondo, M. Verificación digital para periodistas. Manual contra bulos y desinformación internacional. Barcelona: Editorial UOC, 2018, 172 páginas. ISBN: 9788491801290" en la revista Quaderns del CAC 44, vol. XXI, julio 2018 (95-96), ISSN: 2014-2242.
	- **2008 - Reseña** de "Efrén CUEVAS y Alberto N. GARCÍA (eds.). Landscapes of the Self: The Cinema of Ross McElwee/ Paisajes del yo: El Cine de Ross McElwee. Ediciones Internacionales Universitarias (Eiunsa), Madrid, 2007, 331 pp." en la revista Comunicación y Sociedad, ISSN: 0214-0039, Diciembre, 2008. 
	- **2003 - Reseña** de "Ángel ARRESE. Empresa informativa y mercados de la comunicación. Estudios en honor del Profesor Alfonso Nieto Tamargo. Eunsa, Pamplona, 2002, 530 pp." en la revista Comunicación y Sociedad, ISSN: 0214-0039, Nº 2, 2003.

2. **Informes relacionados con proyectos de investigación**

	- **2018 - Coautor**. "Informe sobre la situación actual y perspectivas del periodismo valenciano en la era digital, elaborado por la Comisión Jurídica del Consell Valenciano de Cultura", resultado de mi colaboración como experto consultivo.
	- **2014 - Coautor**. "Ranking de Innovación Periodística 2014", elaborado con el equipo del GICOV, resultado de un proyecto de I+D+i financiado por el Ministerio de Ciencia e Innovación.
	- **2009 - Coautor**. "Newsroom Convergence – A transnational comparison", para Medienhaus Wien, resultado de un proyecto de I+D+i financiado por la Asociación de Prensa Austríaca. 
	- **2008 - Coautor**. "Newsroom convergence in multimedia organisations in Spain and Austria: quality models in the production of news", resultado de un proyecto de I+D+i financiado por el programa de Acciones Integradas del Ministerio de Ciencia e Innovación. 
	- **2002 - Coautor**. Informe "GLOBALISATION OF THE MEDIA INDUSTRY AND POSSIBLE THREATS TO CULTURAL DIVERSITY (Final Study)" para el Parlamento Europeo (STOA Panel), resultado de un proyecto de I+D+i. 

* * *

# Dedicación docente

1. **UMH-MÁSTER**. Profesor responsable de asignaturas del Máster Universitario en Innovación en Periodismo de la Universidad Miguel Hernández:
	- 2013-actualidad. Nuevos Modelos de Negocio (4,5 ECTS) 
	- 2013-actualidad. Ideación y planificación de Proyectos Periodísticos (6 ECTS)
	- 2013-actualidad. Desarrollo y lanzamiento de proyectos periodísticos  (6 ECTS)
	- 2013-actualidad. Prácticas Externas (8 ECTS)
	- 2013-actualidad. Trabajo Fin de Máster (10 ECTS) 
2. **UMH-GRADO**. Profesor de asignaturas del Grado en Periodismo de la Universidad Miguel Hernández: 
	- 2013-actualidad. Redacción Periodística (6 ECTS)
	- 2011-actualidad. Lenguaje y Técnicas de Periodismo Impreso, (6 ECTS)
	- 2011-actualidad. Estructura del Periodismo (6 ECTS),
3. **UMH-LICENCIATURA**. Profesor de asignaturas de Licenciatura en Periodismo de la Universidad Miguel Hernández:
	- 2008-2011. Lenguaje y Técnicas de Periodismo Escrito (8 ECTS)
4. **UCAM-GRADO**. Profesor de asignaturas del Grado en Publicidad y Relaciones Públicas de la Universidad San Antonio UCAM Murcia. 
	- 2005-06. Trabajo fin de Grado 
	- 2005-06. Empresa publicitaria
	- 2005-06. Introducción al Marketing
5. **UNAV-LICENCIATURA**. Profesor de asignaturas de la Licenciatura en Periodismo de la Universidad de Navarra. 
	- 2002-04. Estructura del Periodismo.
6. **UMH-Doctorado**. Docencia impartida en el programa de Doctorado de Nuevos Modelos Periodísticos durante los cursos 2011-2013. 

### Dirección de tesis doctorales, TFM Y TFG

1. **Dirección de Trabajos Fin de Máster (TFM)**. **Entre 2013 y 2018**, he dirigido un total de 30 Trabajos Fin de Máster, en el Máster Universitario en Innovación en Periodismo, título oficial de la Universidad Miguel Hernández de Elche. 
2. **Dirección de Trabajos Fin de Grado (TFG)**. **Entre 2013 y 2018**, he dirigido un total de 10 Trabajos Fin de Grado en el Grado en Periodismo de la Universidad Miguel Hernández de Elche, tres de ellos con  Matrícula de Honor. 
3. **Dirección de Tesis Doctorales**. Co-dirijo actualmente dos tesis doctorales dentro del Programa de Doctorado en Ciencias Sociales y Jurídicas de la Universidad Miguel Hernández de Elche desde 2016. 

### Otros méritos docentes
1. **Docencia en Doctoral Summer School**. He sido ponente en la Doctoral Summer School de la Red de Excelencia en Periodismo Digital y Convergencia Mediática (2018). 
2. **Docencia en otros postgrados**. He sido profesor invitado del Máster Universitario de Profesorado de la Universidad Miguel Hernández, con el "Taller de escritura", con 3 horas (2012). 
3. **Director en estudios propios**. Desde 2014 he sido director de 8 estudios propios de la Universidad Miguel Hernández de Elche, 2 de ellos impartidos en plataformas EdX. Además, he dirigido 2 cursos de verano (2008 y 2011) y 1 curso de invierno (2018). 
4. **Docencia en estudios propios**.
	- Docencia de 4 horas en el Curso de Verano "Redescubriendo a Azorín" (2012) de la Universidad Miguel Hernández. [`documentación acreditativa`](/cv/docu/Otros_Dedicacion_Azorin_UMH_2012.pdf){:target="_blank"} 
	- Docencia de 10 horas en el Curso de Verano "¿Quieres contar historias? Relato, reportaje y escritura digital" (2008) de la Universidad Miguel Hernández. 
	- Docencia de 44 horas en los cursos Guía básica del periodismo innovador y Nuevas Narrativas para periodistas impartidos en EdX. 
5. **Tutor en programa de iniciación a la docencia**. He sido Tutor Académico en programa de iniciación a la docencia de la Universidad Miguel Hernández de Elche con una duración de 20 horas.
6. **Coordinador docente en prácticas curriculares de Grado y Máster**. He sido Tutor Académico de 213 prácticas curriculares en el Grado en Periodismo y Máster Universitario en Innovación en Periodismo de la Universidad Miguel Hernández de Elche con un total de 57.000 horas.
7. **Ponente y coordinador de Jornadas de Empleo**. He sido ponente y coordinador de las Jornadas de Empleo del Grado en Periodismo de la Universidad Miguel Hernández desde 2012 hasta 2019.
8. **Docencia en centros de universidades internacionales**. He sido profesor invitado en la Universidad de Fordham durante una estancia de investigación de una duración de 8 meses. 
9. **Tutor Erasmus** de la Titulación Publicidad y Relaciones Públicas de la Universidad C. San Antonio de Murcia 2005 - 2006. 
10. **Quinquenios**. Concesión de dos tramos (2006-2011, 2012-2016). 
11. **Evaluaciones**. Evaluación positiva de la actividad docente del período 2009/2013 (Satisfactorio) y del período 2013-2017 (Excelente) en el Programa Docentia UMH (Evaluado por ANECA). 
12. **Premios de docencia**. Obtención del **Premio al Talento Docente** en el marco del Programa Docentia-UMH 2018. Seleccionado entre los 10 mejores docentes en Ciencias Sociales y Humanas de la Universidad Miguel Hernández. 
13. **Acreditaciones**. Evaluación positiva como profesor contratado doctor (20 de octubre de 2008) por parte de la Agencia Valenciana para la Evaluación de la Calidad y Acreditación. 
14. **IP de Proyectos de Innovación Docente y miembro del equipo**. He participado en 3 proyectos de Innovación Docente como IP financiados en convocatorias competitivas de la Universidad Miguel Hernández y en 2 como miembro del equipo de trabajo.
15. **Docencia reglada en inglés**. Impartición de la asignatura Media Structure en inglés durante los cursos 2013-2014, 2014-2015, 2015-2016, 2017-2018 y 2018-2019. Se trata de una asignatura optativa de Cuarto Curso del grado de Periodismo, impartida íntegramente en inglés, como fruto del "Programa de Medidas para el Impulso y el Reconocimiento de la Docencia en Inglés" de la Universidad Miguel Hernández.
16. **Organización y participación en seminarios y actividades de formación complementaria en Grado y Máster**. 
	- Co-organizador del "Seminario Local Data Lab" dirigido a estudiantes del Grado en Periodismo y del Máster Universitario en Innovación en Periodismo, desde enero hasta mayo de 2019, con una duración de 25 horas. Los resultados del proyecto pueden consultarse [aquí ↗️](https://localdatalab.umh.es/){:target="_blank"}.
	- Participación activa en el Seminario de Innovación en Periodismo "Los martes del Medialab" dirigido a estudiantes del Grado en Periodismo, desde octubre hasta diciembre de 2016, con una duración de 30 horas. 
	- Organizador de las Jornadas de Empleo de Periodismo del Grado (2015-2019).

17. **Presentación de la ponencia "Fomentar la difusión de trabajos mediante Medium"** en el VII Seminario del departamento de Ciencias Sociales y Humanas relacionado con "Estrategias de la calidad docente" (2015). 
18. **Docencia EdX**. Grabación de 30 vídeos para la docencia impartida en el Máster Univesitario en Innovación en Periodismo, en su modalidad a distancia, alojados en la plataforma EdX. Gestión de foros para la participación de los estudiantes en la modalidad a distancia en la plataforma EdX de 4 asignaturas desde el curso 2015.
19. **Estancia docente en centros relevantes con becas y ayudas de movilidad**. 
 - Estancia docente en CUNY - City University of New York (Nueva York, Estados Unidos) con una beca Destino PDI de la Universidad Miguel Hernández en 2017. 
 - Estancia docente en la Universidad de Wroclaw (Polonia) con beca Erasmus en 2011. 

### Calidad de la formación docente

1. He cursado el **Programa de Aptitud Pedagógica Universitaria**, Universidad Miguel Hernández. (Plan de Formación del Personal Docente e Investigador) con una duración de 100 horas, desde octubre 2006 a junio 2007. 

2. He cursado el **taller "Inglés conversación medio-alto"**, incluido en el Programa de Formación Docente de la Universidad Miguel Hernández, durante los meses de junio y julio de 2009, con un total de 16 horas. 

3. He cursado el **taller "Herramientas web 2.0 para la docencia e investigación periodística"**, incluido en el Programa de Formación Docente de la Universidad Miguel Hernández, celebrado los días 11 y  12 de abril de  2009.

4. He participado en los seminarios sobre **Calidad de la Investigación e Innovación en la Docencia** organizados por el departamento de Ciencias Sociales y Humanas relacionado en los cursos 2015, 2016, 2017 y 2018. 

* * *

# 6. Transferencia de conocimiento 

1. **Transferencia a través del impulso al proyecto** "Ranking en Innovación en Periodismo" de la Universidad Miguel Hernández en 2014. Este trabajo es una aportación fundamental porque recoge los resultados de una iniciativa que puse en marcha en el GICOV (Grupo de Investigación de la Comunicación) de la Universidad Miguel Hernández: el Ranking de Innovación Periodística en España. Tras implantar el Máster Universitario en Innovación en Periodismo en 2012, ideamos una estrategia de trabajo para fundamentar los conocimientos y las prácticas que enseñamos en el Máster. Por ese motivo, iniciamos el proyecto de Ranking. Los resultados de aquel informe tuvieron un gran impacto en la industria y en la academia ([puede consultarse el trabajo en su versión en línea ↗️](http://mip.umh.es/ranking/index.html){:target="_blank"}). Como promotor de la idea de Ranking y director del Máster, tuve una influencia fundamental en la creación de estos estudios. 

2. **Transferencia generadora de valor económico**. Socio fundador de CUATRO GALGOS SL, spin-off en la Universidad Miguel Hernández. Creada por los profesores e investigadores del Área de Periodismo de la UMH José Alberto García Avilés, Miguel Carvajal y Félix Arias, surge con el impulso de la Nau de la Innovació del Parque Científico Empresarial de la UMH, tras ser una de las ideas premiadas en la primera etapa de la 4ª Maratón de Creación de Empresas UMH. Se trata de una consultora creada para implantar la innovación en la comunicación y en el periodismo, que dirige su actividad hacia mercados en cambio como son los proyectos emergentes, los medios en reconversión, las agencias de comunicación y las empresas innovadoras en general. 
	- PROYECTOS desarrollados en la entidad:
		- Influencers UMH
		- [Diccionario del Cliché](http://diccionariodelcliche.umh.es/){:target="_blank"}↗️
		- [Periodistas de Datos](http://periodistasdedatos.com/){:target="_blank"}↗️
		- [Chejov, editor de textos](https://bandahacker.github.io/chejov/){:target="_blank"}↗️
		- [MinistEditor](https://twitter.com/ministeditor){:target="_blank"}↗️
	- SERVICIOS consultoría y formación a empresas: 
		- ORM. Formación en la estrategia de transformación de la redacción, diciembre 2017.
		- VOCENTO. Nuevos formatos de vídeo informativo para diarios locales, mayo 2018 y marzo 2019.
		- FACEBOOK. Seminario sobre desinformación, abril 2019. 
3. **Transferencia a través de la participación en actividades periodísticas con estudiantes del Grado y Máster**. Dirección del Programa de Radio REC Radio de Periodismo UMH desde 2015 hasta 2019. 
4. **Transferencia a través del fomento de la cultura emprendedora**. Desde 2013, he sido formador de estudiantes y promotor de cultura emprendedora en la Universidad Miguel Hernández como **miembro de la Red de Expertos del Parque Científico**. A través de la spin-off CUATRO GALGOS SL, hemos asesorado a más de 30 estudiantes de Máster en el desarrollo de sus proyectos de innovación y emprendimiento en la industria de la comunicación. Como impulsor y director del Máster Universitario en Innovación en Periodismo y socio fundador de CUATRO GALGOS SL he fomentado activamente la cultura emprendedora en el ámbito universitario. Este objetivo se ha logrado con una estrecha colaboración con la Fundación Quorum y la Maratón de Empresas de la UMH, con la que firmamos un acuerdo para el desarrollo de los proyectos empresariales de los estudiantes del Máster. 
En este período (2013-2018), he tutelado la creación de start-ups o he impulsado proyectos de innovación empresarial:
	- Start-ups periodísticas o de la comunicación (13)
	- Proyectos de innovación empresarial (7)
5. **Ganador por la idea empresarial innovadora - 2015** en los programas de emprendimiento del Parque Científico 6º Sprint y primera etapa de la 8ª Maratón de la Universidad Miguel Hernández. 
6. **Redactor de la revista Nuestro Tiempo. 1998 - 2002**. 
7. **Premio Relato Corto** de la Universidad de Navarra (2001) por el cuento "Línea 78". 

* * *

# Formación académica

1. **Licenciado en Periodismo por la Universidad de Navarra - Junio, 2000**. 
2. **Doctor en Periodismo por la Universidad de Navarra - Mayo, 2006, con Sobresaliente Cum Laude**. 
	- Programa de Doctorado con Mención de Calidad (2006) 
3. **Diploma de Estudios Avanzados** del Programa de Doctorado de la Universidad de Navarra con la Calificación de Sobresaliente.

###  Becas, ayudas y contratos

1. **Beca postdoctoral Programa José Castillejo - 2010**.
2. **Beca predoctoral Programa Formación del Profesorado Universitario - 2001-2004**. 
3. **Beca predoctoral de la Universidad de Navarra - 2001-2002**. 
3. **Beca predoctoral de la Universidad de Navarra - 2000-2001**. 

## Desempeño de cargos en gestión universitaria

1. 2015 - actualidad. **Vicedecano** de Proyección del Grado en Periodismo de la Universidad Miguel Hernández.
2. 2012 - actualidad. **Director de Máster Universitario** en Innovación en Periodismo de la Universidad Miguel Hernández.
3. 2002 - 2004. **Adjunto a Dirección de Estudios** de la Facultad de Comunicación de la Universidad de Navarra. 
4. 2015 - actualidad. **Responsable del área de Periodismo** del Departamento de Ciencias Sociales y Humanas de la Universidad Miguel Hernández.
5. 2015 - actualidad. **Miembro de la Junta de la Facultad de Ciencias Sociales y Jurídicas** de la Universidad Miguel Hernández de Elche. 
6. 2005 - 2006. Miembro del **Comité de Autoevaluación** de la Titulación de Publicidad y Relaciones Públicas de la Universidad C. San Antonio de Murcia.
7. 2011-2019. Desempeño de la **coordinación de cursos de Licenciatura y Grado** en Periodismo de la Universidad Miguel Hernández.
	- 2007 - 2011. Coordinador del curso 3º de la Licenciatura en Periodismo de la Universidad Miguel Hernández.
	- 2011 - actualidad. Coordinador del curso 2º del Grado en Periodismo de la Universidad Miguel Hernández.