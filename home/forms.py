from django import forms
from home.models import Bestiary, Items, Spells, Author
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль',
    }))

    class Meta:
        model = Author
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя',
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя',
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите фамилию',
    }))

    Organization = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите организацию',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите почту',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Подтвердите пароль',
    }))

    class Meta:
        model = Author
        fields = ('username', 'first_name', 'last_name', 'Organization', 'email', 'password1', 'password2')


class BestiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Bestiary
        fields = ['Bestiary_ID', 'Size_ID', 'Species_ID',
                  'Speed', 'Worldview_ID', 'Danger',
                  'Bestiary_Author', 'Language_ID', 'Habitat_ID',
                  'Hits', 'Armor_ID', 'Characteristics',
                  'Resistance_Damage', 'Immunity_Damage', 'Skills',
                  'Description', ]


class BestiaryDeleteForm(forms.ModelForm):
    class Meta:
        model = Bestiary
        fields = ['Bestiary_ID', 'Size_ID', 'Species_ID',
                  'Worldview_ID', 'Danger',
                  'Bestiary_Author', 'Language_ID', 'Habitat_ID',
                  'Hits', 'Armor_ID', ]


class BestiaryFindForm(forms.ModelForm):
    class Meta:
        model = Bestiary
        fields = ['Bestiary_ID', 'Size_ID', 'Species_ID',
                  'Worldview_ID', 'Danger',
                  'Bestiary_Author', 'Language_ID', 'Habitat_ID',
                  'Hits', 'Armor_ID', ]


class ItemsCreateForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['Item_ID', 'Item_Type', 'Item_Rarity',
                  'Item_Setting', 'Item_Author', 'Item_Price',
                  'Item_Description', ]


class ItemsDeleteForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['Item_ID', 'Item_Type', 'Item_Rarity',
                  'Item_Setting', 'Item_Author', 'Item_Price', ]


class ItemsFindForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['Item_ID', 'Item_Type', 'Item_Rarity',
                  'Item_Setting', 'Item_Author', 'Item_Price', ]


class SpellDeleteForm(forms.ModelForm):
    class Meta:
        model = Spells
        fields = ['Spell_ID', 'Spell_Author', 'Spell_Level',
                  'School', 'Archetypes', ]


class SpellCreateForm(forms.ModelForm):
    class Meta:
        model = Spells
        fields = ['Spell_ID', 'Spell_Author', 'Spell_Level',
                  'School', 'Time_Application', 'Distance',
                  'Duration', 'Components', 'Archetypes',
                  'Description', ]


class SpellFindForm(forms.ModelForm):
    class Meta:
        model = Spells
        fields = ['Spell_ID', 'Spell_Level', 'Archetypes',
                  'Spell_Author', 'School', ]