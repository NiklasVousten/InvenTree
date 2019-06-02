"""
Django Forms for interacting with Part objects
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from InvenTree.forms import HelperForm

from django import forms

from .models import Part, PartCategory, PartAttachment
from .models import BomItem


class PartImageForm(HelperForm):
    """ Form for uploading a Part image """

    class Meta:
        model = Part
        fields = [
            'image',
        ]


class BomValidateForm(HelperForm):
    """ Simple confirmation form for BOM validation.
    User is presented with a single checkbox input,
    to confirm that the BOM for this part is valid
    """

    validate = forms.BooleanField(required=False, initial=False, help_text='Confirm that the BOM is correct')

    class Meta:
        model = Part
        fields = [
            'validate'
        ]


class BomExportForm(HelperForm):

    # TODO - Define these choices somewhere else, and import them here
    format_choices = (
        ('csv', 'CSV'),
        ('pdf', 'PDF'),
        ('xml', 'XML'),
        ('xlsx', 'XLSX'),
        ('html', 'HTML')
    )

    # Select export type
    format = forms.CharField(label='Format', widget=forms.Select(choices=format_choices), required='true', help_text='Select export format')

    class Meta:
        model = Part
        fields = [
            'format',
        ]


class EditPartAttachmentForm(HelperForm):
    """ Form for editing a PartAttachment object """

    class Meta:
        model = PartAttachment
        fields = [
            'part',
            'attachment',
            'comment'
        ]


class EditPartForm(HelperForm):
    """ Form for editing a Part object """

    deep_copy = forms.BooleanField(required=False,
                                   initial=True,
                                   help_text="Perform 'deep copy' which will duplicate all BOM data for this part",
                                   widget=forms.HiddenInput())

    confirm_creation = forms.BooleanField(required=False,
                                          initial=False,
                                          help_text='Confirm part creation',
                                          widget=forms.HiddenInput())

    class Meta:
        model = Part
        fields = [
            'deep_copy',
            'confirm_creation',
            'category',
            'name',
            'IPN',
            'description',
            'keywords',
            'variant_of',
            'is_template',
            'URL',
            'default_location',
            'default_supplier',
            'units',
            'minimum_stock',
            'assembly',
            'component',
            'trackable',
            'purchaseable',
            'salable',
            'notes',
        ]


class EditCategoryForm(HelperForm):
    """ Form for editing a PartCategory object """

    class Meta:
        model = PartCategory
        fields = [
            'parent',
            'name',
            'description',
            'default_location',
            'default_keywords',
        ]


class EditBomItemForm(HelperForm):
    """ Form for editing a BomItem object """

    class Meta:
        model = BomItem
        fields = [
            'part',
            'sub_part',
            'quantity',
            'overage',
            'note'
        ]

        # Prevent editing of the part associated with this BomItem
        widgets = {'part': forms.HiddenInput()}


class PartPriceForm(forms.Form):
    """ Simple form for viewing part pricing information """

    quantity = forms.IntegerField(
        required=True,
        initial=1,
        help_text='Input quantity for price calculation'
    )

    class Meta:
        model = Part
        fields = [
            'quantity'
        ]
