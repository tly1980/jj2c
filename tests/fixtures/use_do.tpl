{%- set a = [] -%}
{%- do a.append(1) -%}
{%- do a.append(2) -%}
{%- do a.append(name) -%}
{{ a }}
