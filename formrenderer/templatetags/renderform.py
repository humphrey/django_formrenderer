import shlex

from django import template
from django.template.loader import render_to_string
from django import forms

register = template.Library()


@register.filter
def renderform(value, arg='formrenderer/default.html'):
    return _renderform(value, arg, True)


@register.filter
def renderform_html4(value, arg='formrenderer/default.html'):
    return _renderform(value, arg, False)


def _renderform(value, arg, html5=True):
    template_name = arg.split(',')[0]
    fieldnames = [f.strip() for f in arg.split(',')[1:] if len(f.strip()) > 0]

    # If no fields specified, use them all!
    if not fieldnames:
        fieldnames = value.fields.keys()

    fields = []
    for f in fieldnames:

        # Parse it all
        try:
            i = f.index('[')
        except ValueError:
            i = len(f)
        name = f[:i].split('.')[0]
        classes = f[:i].split('.')[1:]
        attrs = f[i:].strip("[] ")

        # Add in classes
        if len(classes) > 0:
            cls = value[name].field.widget.attrs.get('class', '')
            if len(cls) > 0:
                cls += ' '
            cls += ' '.join(classes)
            value[name].field.widget.attrs['class'] = cls

        # Html5 validation
        if html5:
            if value[name].field.required:
                value[name].field.widget.attrs['required'] = 'required'
            if type(value[name].field) is forms.EmailField:
                value[name].field.widget.input_type = 'email'

        # Add in attributes
        if attrs:
            # this is split a bit more carefully so that we can use the ; character within style strings
            my_splitter = shlex.shlex(attrs.encode('utf8'), posix=True)
            my_splitter.whitespace = ';'
            my_splitter.whitespace_split = True
            for attr in list(my_splitter):
                n,v = attr.strip().split("=")
                v = v.strip("' ")
                value[name].field.widget.attrs[n] = v

        fields.append(value[name])

    return render_to_string(template_name, {
        'form': value,
        'fields': fields,
    })