---
layout: notas
title: Notas
subtitle: · archivo
permalink: /notas/archivo/
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
			<p class="small text-black-50" style="font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;">{{ post.date | date: "%d/%m/%Y" }}</p>
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
