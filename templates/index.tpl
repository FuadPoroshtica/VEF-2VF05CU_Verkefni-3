{% extends "base.html" %}

{% block title %} nyfrettir {% endblock %}

{% block head %}
    {{ super() }}
<style type="text/css">
    .important {color: #369;}
</style>
{% endblock %}

{% block content %}
    <div class="row">
        <section>
            <h1 class="important">{{frettir[0][1]}}</h1>
            <img src='/static/mynd0.jpg'/>
        </section>
        <section class="top2em">
            <h3>nyfréttir dagsins</h3>
            <ul>
                {% for item in frettir %}
                    <li><a href='/frett/{{ item[0] }}'>{{ item[1] }}</a> </li>
                {% endfor %}
            </ul>
        </section>
    </div>
{% endblock %}