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
    
    org_name = schema.TextLine(
            title = u"Organization Name"    
        )
    
    copyright_text = schema.TextLine(
            title = u"Copyright Text",
            required = False
        )
    
    rights_reserved = schema.TextLine(
        title = u"Rights Reserved Custom Text",
        required = False
    )
    
    
    

class Assignment(base.Assignment):
    implements(IContentNavigation)
    
    def __init__(self,org_name=None, copyright_text=None, rights_reserved=None):
        self.org_name = org_name
        self.copyright_text = copyright_text
        self.rights_reserved = rights_reserved
        
    title = u"Organization Name and Copyright Portlet"
    

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('orgname_copyright_portlet.pt')
    
    
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