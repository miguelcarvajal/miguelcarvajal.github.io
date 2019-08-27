---
title: Notas
permalink: /notas/reporterhacks
layout: notas
subtitle: · ReporterHacks
---
<div class="row my-3">
{% for post in site.categories.Reporterhacks %}

<div class="col-sm-6 col-md-6 col-lg-4">
	<div class="card mb-4 shadow-sm">
     {% if post.image %} 
     {% if site.lazyimages == "enabled" %}
	<img class="img-fluid lazyimg" src="{{ post.image }}" alt="{{ post.title }}">
	  {% else %}
      {% endif %}
	<img class="img-fluid" src="{{ post.image }}" alt="{{ post.title }}">
      {% endif %}
    <div class="card-body">
		<p class="card-text"><strong>{{ post.title }}</strong>. {{ post.excerpt | strip_html | truncatewords:30 }}. <a class="text-decoration-none" href="{{ post.enlace }}"> Consultar herramienta</a>.</p>
              <div class="d-flex justify-content-start align-items-center">
              	{% assign sortedTags = post.tags %}
                {% for tag in sortedTags limit:2 %}
				<a class="btn btn-light btn-sm mb-1 mr-1" href="{{site.baseurl}}/notas/reporterhacks#{{ tag | replace: " ","-" }}">{{ tag }}</a>
                 {% endfor %}
              </div>
     </div>
	</div>
</div>

{% endfor %}
</div>
