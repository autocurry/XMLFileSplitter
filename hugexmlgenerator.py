from mako.template import Template
from mako.runtime import Context

tpl_xml = '''
<doc>
% for i in data:
<p>${i}</p>
% endfor
</doc>
'''

tpl = Template(tpl_xml)

with open('output.xml', 'w') as f:
    ctx = Context(f, data=range(10000000))
    tpl.render_context(ctx)