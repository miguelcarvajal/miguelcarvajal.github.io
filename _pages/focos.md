---
layout: notas
title: Notas
subtitle: · focos
permalink: /notas/foco
---

<div class="article-post my-3">
{% for category in site.categories %}
<h3 id="{{ category[0] | replace: " ","-" }}" class="font-weight-light">{{ category[0] }}</h3>
{% assign pages_list = category[1] %}
{% for post in pages_list %}
{% if post.title != null %}
{% if group == null or group == post.group %}

<ul class="list-unstyled">
	<li class="media my-3">
		<div class="media-body">
			<strong>{{ post.title }}</strong>. {{ post.excerpt | strip_html | truncatewords:30 }} <a class="text-decoration-none" href="{{ post.url | absolute_url }}"> Leer más</a>.
			<a class="text-decoration-none" href="#"><p class="small text-black-50 mt-1">{{ post.date | date_to_string }}</p></a>
			<hr class="mb-0">						
		</div>
	</li>
</ul>

{% endif %}
{% endif %}
{% endfor %}
{% assign pages_list = nil %}
{% assign group = nil %}
{% endfor %}
</div> 
