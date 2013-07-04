# Django Form Renderer

Provides template filters that allow you to give you power to render forms however you want.

HTML 5 input types are automatically used for field types that are appropriate.

If a field is required, the [required="required"] is automatically added to the element.

## Examples

### Simple HTML5 Example

```HTML+Django/Jinja
{% load renderform %}
<form>
    <legend>Your details</legend>
    {{ form|renderform:"formrenderer/default.html, name, email, phone" }}

    <legend>Extra info</legend>
    {{ form|renderform:"formrenderer/default.html, dealer, comments" }}
</form>
```

### Or use HTML 4 (but why would you?)

```HTML+Django/Jinja
{{ form|renderform_html4:"formrenderer/default.html, name, email, phone" }}
```

### Add a class name to a field

Append the field name with the class name. Eg. `my_field.class_name`

```HTML+Django/Jinja
{{ form|renderform:"formrenderer/default.html, name.class_name" }}
```

### Add an attribute

Append the field name with the attribute. Eg. `my_field[key=value]`

```HTML+Django/Jinja
{{ form|renderform:"formrenderer/default.html, comments[rows=3]" }}
{{ form|renderform:"formrenderer/default.html, comments[rows=3,disabled=disabled]" }}
```

### Add class names and attributes

Append the field name with the class name. Eg. `my_field[key=value]`

```HTML+Django/Jinja
{{ form|renderform:"formrenderer/default.html, comments.my_class[rows=3]" }}
```

### Complicated Example

```HTML+Django/Jinja
{% load renderform %}
<form>
    {{ form|renderform:"formrenderer/bootstrap_horizontal.html, name.input-block-level, email.input-block-level }}
    <hr/>
    {{ form|renderform:"formrenderer/bootstrap_horizontal.html, phone, dealer[class=myClass] }}
    <hr/>
    {{ form|renderform:"formrenderer/bootstrap_horizontal.html, comments.input-block-level[rows=3]" }}
</form>
```
