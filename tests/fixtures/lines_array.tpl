## My List 1
{% for l in lst1 -%}
{{loop.index}} - {{ l }}
{% endfor %}

## My List 2
{% for l in lst2 -%}
{{loop.index}} - {{ l }}
{% endfor %}
