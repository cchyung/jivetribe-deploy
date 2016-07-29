from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from models import EventPluginModel


class EventPlugin(CMSPluginBase):
    model = EventPluginModel
    render_template = 'event_plugin.html'
    cache = False
    name = _("Event")

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(EventPlugin)
