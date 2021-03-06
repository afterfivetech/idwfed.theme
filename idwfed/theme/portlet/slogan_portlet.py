from five import grok
from zope.formlib import form
from zope import schema
from zope.interface import implements
from zope.component import getMultiAdapter
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


#grok.templatedir('templates')

class IContentNavigation(IPortletDataProvider):
    
    slogan_text = schema.TextLine(
            title = u"Slogan Text"    
        )
    
    
    

class Assignment(base.Assignment):
    implements(IContentNavigation)
    
    def __init__(self,slogan_text=None):
        self.slogan_text = slogan_text
        
    title = u"Slogan portlet"
    

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('slogan_portlet.pt')
    
    
    def __init__(self, context, request, view, manager, data):
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        self.data = data
        
        
    def contents(self):
        return self.data.slogan_text

        
    

class AddForm(base.AddForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Add Slogan Portlet"
    description = ''
    
    def create(self, data):
        assignment = Assignment()
        form.applyChanges(assignment, self.form_fields, data)
        return assignment
    

class EditForm(base.EditForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Edit Slogan Portlet"
    description = ''