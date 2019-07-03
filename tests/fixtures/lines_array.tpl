>> my_lst
{% for l in lst1 -%}
{{loop.index}} - {{ l }}
{% endfor %}

>> my_lst2
{% for l in lst2 -%}
{{loop.index}} - {{ l }}
{% endfor %}
