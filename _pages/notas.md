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
			<a class="" href="{{site.baseurl}}/notas/archivo/#{{ category | replace: " ","-" }}"><strong class="d-inline-block mt-2 mb-1 text-primary">{{ category }}</strong></a>	
			{% endfor %}
			<h5><a class="text-decoration-none text-dark" href="{{ post.url | absolute_url }}">{{ post.title }}</a></h5>
			<p class="font-weight-normal mb-1">{{ post.excerpt | strip_html | truncatewords:33 }}.</p>
			<a class="text-decoration-none" href="{{ post.link }}"><p class="small text-black-50">{{ post.date | date: "%d/%m/%Y" }}</p></a>
		   {% if post.image %} 
		     {% if site.lazyimages == "enabled" %}
			<img class="img-fluid rounded lazyimg" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAACCAQAAAA3fa6RAAAADklEQVR42mNkAANGCAUAACMAA2w/AMgAAAAASUVORK5CYII=" data-src="{% if post.image contains "://" %}{{ post.image }}{% else %}{{ post.image | absolute_url }}{% endif %}" alt="{{ post.title }}">
			  {% else %}
			<img class="img-fluid rounded" src="{% if post.image contains "://" %}{{ post.image }}{% else %}{{ site.baseurl }}/{{ post.image }}{% endif %}" alt="{{ post.title }}">
		      {% endif %}
		   {% endif %}
			<hr class="mb-0">
{% endfor %}
</div>

<div class="col-sm-8 col-lg-6 my-3">
	{% for post in site.categories.Analisis limit: 5 %}
   {% if post.image %} 
     {% if site.lazyimages == "enabled" %}
	<img class="img-fluid rounded lazyimg" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAACCAQAAAA3fa6RAAAADklEQVR42mNkAANGCAUAACMAA2w/AMgAAAAASUVORK5CYII=" data-src="{% if post.image contains "://" %}{{ post.image }}{% else %}{{ post.image | absolute_url }}{% endif %}" alt="{{ post.title }}">
	  {% else %}
	<img class="img-fluid rounded" src="{% if post.image contains "://" %}{{ post.image }}{% else %}{{ site.baseurl }}/{{ post.image }}{% endif %}" alt="{{ post.title }}">
      {% endif %}
   {% endif %}
	<h2 class="mt-1"><a class="text-decoration-none text-dark" href="{{ post.url | absolute_url }}">{{ post.title }}</a></h2>
	<p>{{ post.excerpt | strip_html | truncatewords:35 }}. <a class="text-decoration-none" href="{{ post.url | absolute_url }}">Leer más.</a></p>
	<a class="text-decoration-none" href="{{ post.url | absolute_url }}"><p class="small text-black-50">{{ post.date | date: "%B, %Y" }}</p></a>
{% endfor %}

</div>

<div class="col-sm-6 col-md-6 col-lg-3 ml-auto">
	<aside class="sidebar">
		<div class="p-3 mt-3 mb-3 bg-warning rounded">
			<p class="mb-0"><strong>Notas</strong> es mi libreta de apuntes, enlaces, pistas y herramientas útiles para periodistas. <a href="https://twitter.com/mcarvajal_"><i class="fab fa-twitter"></i></a></p>
			  <footer class="blockquote-footer">Miguel Carvajal</footer>
		</div>

<a href="{{site.baseurl}}/notas/reporterhacks"><strong class="d-inline-block mt-2 mb-1 text-primary">ReporterHacks</strong></a>

{% for post in site.categories.Reporterhacks limit: 3 %}

<div class="card mb-4 shadow-sm">
   {% if post.image %} 
     {% if site.lazyimages == "enabled" %}
	<img class="img-fluid lazyimg" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAACCAQAAAA3fa6RAAAADklEQVR42mNkAANGCAUAACMAA2w/AMgAAAAASUVORK5CYII=" data-src="{% if post.image contains "://" %}{{ post.image }}{% else %}{{ post.image | absolute_url }}{% endif %}" alt="{{ post.title }}">
	  {% else %}
	<img class="img-fluid" src="{% if post.image contains "://" %}{{ post.image }}{% else %}{{ site.baseurl }}/{{ post.image }}{% endif %}" alt="{{ post.title }}">
      {% endif %}
   {% endif %}
       <div class="card-body">
	    <p class="mb-2 font-weight-bolder"><a class="text-decoration-none" href="{{ post.enlace }}">{{ post.name }}</a></p>
		<p class="card-text small"><strong>{{ post.title }}</strong>. {{ post.excerpt | strip_html | truncatewords:25 }} <a class="text-decoration-none" href="{{ post.url | absolute_url }}"> Leer más</a>.</p>
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