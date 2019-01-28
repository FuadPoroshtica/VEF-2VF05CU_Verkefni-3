{% extends "base.html" %}

{% block title %} {{ frett[1] }} {% endblock %}

{% block content %}
     <div>
        <section>
            <h1>{{ frett[1] }}</h1>
            <img src='/static/mynd{{ nr }}.jpg'/>
        </section>
        <section>
            <p>{{ frett[2] }}</p>
            <h5><a href="/">Forsíða</a></h5>
        </section>
     </div>
{% endblock content %}
