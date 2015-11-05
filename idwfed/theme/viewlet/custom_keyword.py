from zope.interface import Interface
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common as base
from plone.app.layout.globals.interfaces import IViewView

class ICustomKeyword(base.ViewletBase):
    """class for custom plone.app.layouts.viewlets.keyboard.pt"""
    #index = ViewPageTemplateFile("templates/custom_keyword.pt")
    
    def sort_tags(self, tags=None):
        if tags:
            
            return sorted(tags)
        return tags
    