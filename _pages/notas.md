---
title: Notas
permalink: /notas/
layout: notas
color: bg-dark
---
<div class="row">
<div class="col-sm-4 col-lg-3 my-2">
	{% for post in site.categories.Noticias limit: 5 %}
           	{% assign sortedCategories = post.categories %}
            {% for category in sortedCategories offset: 1 limit: 1 %}
			<a class="" href="{{site.baseurl}}/notas/foco#{{ category | replace: " ","-" }}"><strong class="d-inline-block mt-2 mb-1 text-primary">{{ category }}</strong></a>	
			{% endfor %}
			<h5>{{ post.title }}</h5>
			<p class="font-weight-normal mb-1">{{ post.excerpt | strip_html | truncatewords:25 }}. <a class="text-decoration-none" href="{{ post.url | absolute_url }}">Leer más</a></p>
			<a class="text-decoration-none" href="{{ post.link }}"><p class="small text-black-50">24 julio</p></a>
			<hr class="mb-0">
{% endfor %}
</div>

<div class="col-sm-8 col-lg-6 my-3">
	{% for post in site.categories.Analisis limit: 5 %}

   {% if post.image %} 
     {% if site.lazyimages == "enabled" %}
	<img class="img-fluid rounded lazyimg" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAACCAQAAAA3fa6RAAAADklEQVR42mNkAANGCAUAACMAA2w/AMgAAAAASUVORK5CYII=" data-src="{% if post.image contains "://" %}{{ post.image }}{% else %}{{ post.image | absolute_url }}{% endif %}" alt="{{ post.title }}">
	  {% else %}
	<img class="img-fluid rounded" src="{% if post.image contains "://" %}{{ post.image }}{% else %}{{ post.image | absolute_url }}{% endif %}" alt="{{ post.title }}">
      {% endif %}
   {% endif %}
	<h2 class="mt-1">{{ post.title }}</h2>
	<p>{{ post.excerpt | strip_html | truncatewords:25 }}. <a class="text-decoration-none" href="{{ post.url | absolute_url }}">Leer más.</a></p>
	<a class="text-decoration-none" href="{{ post.link }}"><p class="small text-black-50">{{ post.date | date: "%B, %Y" }}</p></a>

{% endfor %}

</div>

<div class="col-sm-6 col-md-6 col-lg-3 ml-auto">
	<aside class="sidebar">
		<div class="p-3 mt-3 mb-3 bg-warning rounded">
			<h4 class="font-italic">¿Qué es esto?</h4>
			<p class="mb-0">Mi libreta de apuntes sobre periodismo, medios y economía de la atención. Un método para guardar enlaces, pistas y herramientas útiles para mi trabajo.</p>
		</div>	
		
<strong class="d-inline-block mt-2 mb-1 text-primary">ReporterHacks</strong>	

{% for post in site.categories.Reporterhacks limit: 3 %}

<div class="card mb-4 shadow-sm small">
   {% if post.image %} 
     {% if site.lazyimages == "enabled" %}
	<img class="img-fluid lazyimg" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAACCAQAAAA3fa6RAAAADklEQVR42mNkAANGCAUAACMAA2w/AMgAAAAASUVORK5CYII=" data-src="{% if post.image contains "://" %}{{ post.image }}{% else %}{{ post.image | absolute_url }}{% endif %}" alt="{{ post.title }}">
	  {% else %}
	<img class="img-fluid" src="{% if post.image contains "://" %}{{ post.image }}{% else %}{{ post.image | absolute_url }}{% endif %}" alt="{{ post.title }}">
      {% endif %}
   {% endif %}
       <div class="card-body">
		<p class="card-text"><strong>{{ post.title }}</strong>. {{ post.excerpt | strip_html | truncatewords:25 }}. <a class="text-decoration-none" href="{{ post.enlace }}"> Consultar herramienta</a>.</p>
             <div class="d-flex justify-content-start align-items-center">
              	{% assign sortedTags = post.tags %}
                {% for tag in sortedTags limit:2 %}
				<a class="btn btn-light btn-sm mb-1 mr-1" href="{{site.baseurl}}/notas/reporterhacks#{{ tag | replace: " ","-" }}">{{ tag }}</a>
                 {% endfor %}
              </div>
     </div>
	</div>

{% endfor %}


</aside>
</div>
</div>