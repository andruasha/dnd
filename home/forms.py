from django import forms
from home.models import Spells


class SpellForm(forms.ModelForm):
    class Meta:
        model = Spells
        fields = ['Spell_Level', 'School', 'Archetypes']