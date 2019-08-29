---
title: Notas
permalink: /notas/reporterhacks/
layout: notas
subtitle: · ReporterHacks
---
<div class="row my-3">
<div class="col-lg-12">
 <div class="card mb-4">
              <div class="card-body">
            {% assign tags_list = site.tags %}
            {% if tags_list.first[0] == null %}
            {% for tag in tags_list %}
                  <a class="btn btn-light btn-sm mb-1" href="{{site.baseurl}}/notas/reporterhacks#{{ tag | url_escape | strip | replace: ' ', '-' }}">{{ tag | camelcase }} </a>
                {% endfor %}
            {% else %}
                {% for tag in tags_list %}                        
                  <a class="btn btn-light btn-sm mb-1" href="{{site.baseurl}}/notas/reporterhacks#{{ tag[0] | url_escape | strip | replace: ' ', '-' }}">{{ tag[0] | camelcase }}</a>
                {% endfor %}
            {% endif %}
            {% assign tags_list = nil %}
              </div>
  </div>
</div>

{% for tag in site.tags %}     
<div class="col-md-12">
<h2 id="{{ tag[0] | replace: " ","-" }}"><span class="text-capitalize">{{ tag[0] }}</span></h2>
</div>

{% assign pages_list = tag[1] %}
{% for post in pages_list %}
{% if post.title != null %}
{% if group == null or group == post.group %}
<div class="col-sm-6 col-md-6 col-lg-4">
	<div class="card mb-4 shadow-sm">
   {% if post.image %} 
     {% if site.lazyimages == "enabled" %}
	<img class="img-fluid lazyimg" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAACCAQAAAA3fa6RAAAADklEQVR42mNkAANGCAUAACMAA2w/AMgAAAAASUVORK5CYII=" data-src="{% if post.image contains "://" %}{{ post.image }}{% else %}{{ post.image | absolute_url }}{% endif %}" alt="{{ post.title }}">
	  {% else %}
	<img class="img-fluid" src="{% if post.image contains "://" %}{{ post.image }}{% else %}{% else %}{{ site.baseurl }}/{{ post.image }}{% endif %}" alt="{{ post.title }}">
      {% endif %}
   {% endif %}
    <div class="card-body">
    <p class="card-subtitle mb-2 font-weight-bolder"><a class="text-decoration-none" href="{{ post.enlace }}">{{ post.name }}</a></p>
    <p class="card-text"><strong>{{ post.title }}</strong>. {{ post.excerpt | strip_html | truncatewords:25 }} <a class="text-decoration-none" href="{{ post.url | absolute_url }}"> Leer más</a>.</p>
              <div class="d-flex justify-content-start align-items-center">
              	{% assign sortedTags = post.tags %}
                {% for tag in sortedTags limit:2 %}
				<a class="btn btn-light btn-sm mb-1 mr-1" href="{{site.baseurl}}/notas/reporterhacks#{{ tag | replace: " ","-" }}">{{ tag }}</a>
                 {% endfor %}
              </div>
     </div>
	</div>
</div>
{% endif %}
{% endif %}
{% endfor %}
{% assign pages_list = nil %}
{% assign group = nil %}
{% endfor %}
</div>