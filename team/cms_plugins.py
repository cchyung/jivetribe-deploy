from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import MemberPluginModel


class MemberPlugin(CMSPluginBase):
    model = MemberPluginModel
    render_template = 'member_plugin.html'
    cache = False
    name = _("Member")

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(MemberPlugin)
