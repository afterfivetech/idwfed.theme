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
    
    item_title = schema.TextLine(
            title = u"Policy Item",
            description=u"e.g. Terms, Privacy, Disclaimer"
        )
    
    
    link = schema.TextLine(
        title = u"Link for the Policy",
        required = False
    )
    
    
    

class Assignment(base.Assignment):
    implements(IContentNavigation)
    
    
    def __init__(self,item_title=None, link=None):
        self.item_title = item_title
        self.link = link
    
        
    @property
    def title(self):
        return "Policy Item: "+self.item_title
    

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('policy_items_portlet.pt')
    
    
    def __init__(self, context, request, view, manager, data):
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        self.data = data
        
        
    def contents(self):
        return self.data

        
    

class AddForm(base.AddForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Add Organization Name and Copyright Portlet"
    description = ''
    
    def create(self, data):
        assignment = Assignment()
        form.applyChanges(assignment, self.form_fields, data)
        return assignment
    

class EditForm(base.EditForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Edit Organization Name and Copyright Portlet"
    description = ''