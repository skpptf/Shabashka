from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div
from crispy_forms.bootstrap import PrependedText, StrictButton
from django.utils.safestring import mark_safe


from .models import ShaUser, user_registrated, SuperCategory, SubCategory, Offer, AdditionalImage
from .models import Comment, ShaUserAvatar



class ChangeProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Адрес электронной почты")

    class Meta:
        model = ShaUser
        fields = ('username', 'email', 'first_name', 'last_name', 'send_message')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field(
                PrependedText("username",
                    mark_safe('<i class="fa fa-user"></i>'),
                    placeholder=_("Имя пользователя"), autofocus="")               
            ),
            Field(
                PrependedText("password",
                    mark_safe('<i class="fa fa-lock"></i>'),
                    placeholder=_("Пароль"))               
            ),
            Div(
                StrictButton('Войти', type='submit', css_class='btn-block btn-lg'),
                css_class='form-group'
            )               
        )
    


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(required=True)    
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field(
                PrependedText("username",
                    mark_safe('<i class="fa fa-user"></i>'),
                    placeholder=_("Имя пользователя"), autofocus="")
               
            ),
            Field(
                PrependedText("email",
                    mark_safe('<i class="fa fa-paper-plane"></i>'),
                    placeholder=_("Email адрес"))
                
            ),
            Field(
                PrependedText("password1",
                    mark_safe('<i class="fa fa-lock"></i>'),
                    placeholder=_("Пароль"))
               
            ),
            Field(
                PrependedText("password2",
                    mark_safe('<i class="fa fa-lock"></i><i class="fa fa-check"></i>'),
                    placeholder=_("Подтверждение пароля"))
                
            ),
            Div(
                StrictButton('Зарегистрироваться', type='submit', css_class='btn-block btn-lg'),
                css_class='form-group'
            )    
        )

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Введенные пароли не совпадают', code='password_mismath')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        user_registrated.send(RegisterUserForm, instance=user)
        return user

    class Meta:
        model = ShaUser
        fields = ('username', 'email', 'password1', 'password2', 
            'first_name', 'last_name', 'send_message')
        widgets ={
            "username": forms.TextInput(attrs={"placeholder": "Имя пользователя"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email адрес"}),
            "password1": forms.PasswordInput(attrs={"placeholder": "Пароль"}),
            "password2": forms.PasswordInput(attrs={"placeholder": "Подтверждение пароля"})      

        }


class SubCategoryForm(forms.ModelForm):
    super_category = forms.ModelChoiceField(queryset=SuperCategory.objects.all(),
                    empty_label=None, label="Надкатегория", required=True)
    class Meta:
        model = SubCategory
        fields = '__all__'


class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=20, label='')


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer        
        exclude = ['reviews', 'shared', 'status', "is_active"]
        widgets = {'author': forms.HiddenInput}

AIFormSet = forms.inlineformset_factory(Offer, AdditionalImage, fields='__all__')

class CommetForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'offer', 'price', 'time_amount', 'measure', 'content')
        exclude = ("is_active", )
        widgets = {
            "offer": forms.HiddenInput,
            "author": forms.HiddenInput,
            'content': forms.Textarea(attrs={'rows': 4})
        }
                   

class AvatarForm(forms.ModelForm):
    class Meta:       
        model = ShaUserAvatar
        fields = "__all__"
        widgets = {
            "user": forms.HiddenInput
        }