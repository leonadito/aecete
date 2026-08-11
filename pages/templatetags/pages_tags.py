from django import template
from django.utils.html import format_html

register = template.Library()

# Minimal inline SVG (Heroicons-style, outline, 24x24) per symbolic icon key.
_ICON_PATHS = {
    "discount": "M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M10.5 6h.008v.008H10.5V6zm3 12h.008v.008H13.5V18zM4.5 19.5l15-15",
    "crm": "M9 17.25v1.5m6-1.5v1.5m-10.5-3h15M4.5 6.75h15a1.5 1.5 0 011.5 1.5v7.5a1.5 1.5 0 01-1.5 1.5h-15a1.5 1.5 0 01-1.5-1.5v-7.5a1.5 1.5 0 011.5-1.5z",
    "megaphone": "M10.34 15.84c-.688-.06-1.386-.09-2.09-.09H7.5a4.5 4.5 0 110-9h.75c.704 0 1.402-.03 2.09-.09m0 9.18c2.32.196 4.594.66 6.75 1.35 1.264.4 2.61-.4 2.61-1.72V6.31c0-1.32-1.346-2.12-2.61-1.72a24.301 24.301 0 01-6.75 1.35m0 9.18V5.94",
}
_DEFAULT_PATH = "M12 6v12m6-6H6"


@register.simple_tag
def render_icon(icon_key, css_class="w-8 h-8"):
    path = _ICON_PATHS.get(icon_key, _DEFAULT_PATH)
    return format_html(
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" '
        'stroke-width="1.5" stroke="currentColor" class="{}">'
        '<path stroke-linecap="round" stroke-linejoin="round" d="{}"/></svg>',
        css_class,
        path,
    )
