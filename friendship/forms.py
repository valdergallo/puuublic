#!/usr/bin/env python
# encoding: utf-8
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.conf import settings
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from friendship.models import UserProfile
from friendship.widgets import AdminImageWidget
from publication.models import Favorites, Theme

from captcha.fields import CaptchaField

class RegisterForm(forms.Form):
    name = forms.CharField(
        label='Nome Completo:',
        error_messages={
            'required': u'Digite um nome',
        },
        max_length=100
    )
    email1 = forms.CharField(
        label=u'Email',
        error_messages={
            'required': u'Digite um email',
        },
        required=True,
    )

    email2 = forms.CharField(
        label=u'Digite novamente o Email',
        error_messages={
            'required': u'Repita o email',
        },
        required=True,
    )
    password = forms.CharField(
        label=u'Senha',
        widget=forms.PasswordInput,
        error_messages={
            'required': u'Digite uma senha',
        },
        required=True,
    )
    captcha = CaptchaField(
        label='Você é humano?',
        error_messages={
            'required': u'Digite as letras do CAPTCHA',
            'invalid': u'Letras da caixa não conferem',
        },
    )

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        email1 = cleaned_data.get('email1')
        email2 = cleaned_data.get('email2')

        user_exists = User.objects.filter(email=email1)
        if user_exists:
            raise forms.ValidationError(u'Usuário já existe')

        if email2 != email1:
            raise forms.ValidationError(u'Emails não combinam')
        return self.cleaned_data


    def send_confirmation_email(self):
        """
        Envia email ao usuário com os dados
        """
        subject = u'[Puuublic] Seja Bem-vindo!'
        email = self.cleaned_data.get('email1')
        message_html = render_to_string('email.html', {
            'SITE_URL': settings.SITE_URL,
            'password': self.cleaned_data.get('password1'),
            'email': email,
        })
        message_txt = render_to_string('email.txt', {})
        from_email = settings.DEFAULT_FROM_EMAIL
        msg = EmailMultiAlternatives(subject, message_txt, from_email ,
                                             [email])
        msg.attach_alternative(message_html, "text/html")
        return msg.send()


    def save(self):
        email = self.cleaned_data.get('email1')
        full_name = self.cleaned_data.get('name').split()
        user = User()
        user.is_active = True
        user.email = email
        user.first_name =  full_name[0][:30]
        if len(full_name) > 1:
            user.last_name = ' '.join(full_name[1:])[:30]
        if len(email) <= 30:
            user.username = self.cleaned_data.get('email1')
        else:
            user.username = User.objects.make_random_password(29)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        #favorita o puublic 
        theme, created = Theme.objects.get_or_create(slug='descubra-o-puuublic')
        Favorites.objects.create(user=user, theme=theme)
        self.send_confirmation_email()
        return user

    class Meta:
        fields = ('email1', 'email2', 'password1', 'password2', 'captcha', )



class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'regiter_user',
        'placeholder': u'Email',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id':'register_password',
        'placeholder': u'Senha'
    }))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError(u'Usuário inválido')
        if not user.is_active:
            raise forms.ValidationError(u'Usuário desativado')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'password',)


class RecoverPassForm(forms.Form):
    password1 = forms.CharField(label="Digite uma senha",
                                widget=forms.PasswordInput())
    password2 = forms.CharField(label="Digite novamente",
                                widget=forms.PasswordInput())

    def clean(self):
        p1 = self.cleaned_data['password1']
        p2 = self.cleaned_data['password2']

        if p1 != p2:
            raise forms.ValidationError(u"Senhas não conferem")

        if len(p1) < 6:
            raise forms.ValidationError(u"Senha deve conter mais que 6 caracteres")

        return self.cleaned_data



class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class':'config-large'
    }))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class':'config-large'
    }))

    class Meta:
        model = User
        fields = ('first_name','last_name',)


class EditProfileForm(forms.ModelForm):
    BIRTH_YEAR_CHOICES = range(1930, 2013)
    GENDER_CHOICES = (
        ('M','Masculino'),
        ('F','Feminino'),
    )

    COUNTRIES = (
        ('AF', _(u'Afghanistan')),
        ('AX', _(u'\xc5land Islands')),
        ('AL', _(u'Albania')),
        ('DZ', _(u'Algeria')),
        ('AS', _(u'American Samoa')),
        ('AD', _(u'Andorra')),
        ('AO', _(u'Angola')),
        ('AI', _(u'Anguilla')),
        ('AQ', _(u'Antarctica')),
        ('AG', _(u'Antigua and Barbuda')),
        ('AR', _(u'Argentina')),
        ('AM', _(u'Armenia')),
        ('AW', _(u'Aruba')),
        ('AU', _(u'Australia')),
        ('AT', _(u'Austria')),
        ('AZ', _(u'Azerbaijan')),
        ('BS', _(u'Bahamas')),
        ('BH', _(u'Bahrain')),
        ('BD', _(u'Bangladesh')),
        ('BB', _(u'Barbados')),
        ('BY', _(u'Belarus')),
        ('BE', _(u'Belgium')),
        ('BZ', _(u'Belize')),
        ('BJ', _(u'Benin')),
        ('BM', _(u'Bermuda')),
        ('BT', _(u'Bhutan')),
        ('BO', _(u'Bolivia, Plurinational State of')),
        ('BQ', _(u'Bonaire, Sint Eustatius and Saba')),
        ('BA', _(u'Bosnia and Herzegovina')),
        ('BW', _(u'Botswana')),
        ('BV', _(u'Bouvet Island')),
        ('BR', _(u'Brazil')),
        ('IO', _(u'British Indian Ocean Territory')),
        ('BN', _(u'Brunei Darussalam')),
        ('BG', _(u'Bulgaria')),
        ('BF', _(u'Burkina Faso')),
        ('BI', _(u'Burundi')),
        ('KH', _(u'Cambodia')),
        ('CM', _(u'Cameroon')),
        ('CA', _(u'Canada')),
        ('CV', _(u'Cape Verde')),
        ('KY', _(u'Cayman Islands')),
        ('CF', _(u'Central African Republic')),
        ('TD', _(u'Chad')),
        ('CL', _(u'Chile')),
        ('CN', _(u'China')),
        ('CX', _(u'Christmas Island')),
        ('CC', _(u'Cocos (Keeling) Islands')),
        ('CO', _(u'Colombia')),
        ('KM', _(u'Comoros')),
        ('CG', _(u'Congo')),
        ('CD', _(u'Congo, The Democratic Republic of the')),
        ('CK', _(u'Cook Islands')),
        ('CR', _(u'Costa Rica')),
        ('CI', _(u"C\xf4te D'ivoire")),
        ('HR', _(u'Croatia')),
        ('CU', _(u'Cuba')),
        ('CW', _(u'Cura\xe7ao')),
        ('CY', _(u'Cyprus')),
        ('CZ', _(u'Czech Republic')),
        ('DK', _(u'Denmark')),
        ('DJ', _(u'Djibouti')),
        ('DM', _(u'Dominica')),
        ('DO', _(u'Dominican Republic')),
        ('EC', _(u'Ecuador')),
        ('EG', _(u'Egypt')),
        ('SV', _(u'El Salvador')),
        ('GQ', _(u'Equatorial Guinea')),
        ('ER', _(u'Eritrea')),
        ('EE', _(u'Estonia')),
        ('ET', _(u'Ethiopia')),
        ('FK', _(u'Falkland Islands (Malvinas)')),
        ('FO', _(u'Faroe Islands')),
        ('FJ', _(u'Fiji')),
        ('FI', _(u'Finland')),
        ('FR', _(u'France')),
        ('GF', _(u'French Guiana')),
        ('PF', _(u'French Polynesia')),
        ('TF', _(u'French Southern Territories')),
        ('GA', _(u'Gabon')),
        ('GM', _(u'Gambia')),
        ('GE', _(u'Georgia')),
        ('DE', _(u'Germany')),
        ('GH', _(u'Ghana')),
        ('GI', _(u'Gibraltar')),
        ('GR', _(u'Greece')),
        ('GL', _(u'Greenland')),
        ('GD', _(u'Grenada')),
        ('GP', _(u'Guadeloupe')),
        ('GU', _(u'Guam')),
        ('GT', _(u'Guatemala')),
        ('GG', _(u'Guernsey')),
        ('GN', _(u'Guinea')),
        ('GW', _(u'Guinea-bissau')),
        ('GY', _(u'Guyana')),
        ('HT', _(u'Haiti')),
        ('HM', _(u'Heard Island and McDonald Islands')),
        ('VA', _(u'Holy See (Vatican City State)')),
        ('HN', _(u'Honduras')),
        ('HK', _(u'Hong Kong')),
        ('HU', _(u'Hungary')),
        ('IS', _(u'Iceland')),
        ('IN', _(u'India')),
        ('ID', _(u'Indonesia')),
        ('IR', _(u'Iran, Islamic Republic of')),
        ('IQ', _(u'Iraq')),
        ('IE', _(u'Ireland')),
        ('IM', _(u'Isle of Man')),
        ('IL', _(u'Israel')),
        ('IT', _(u'Italy')),
        ('JM', _(u'Jamaica')),
        ('JP', _(u'Japan')),
        ('JE', _(u'Jersey')),
        ('JO', _(u'Jordan')),
        ('KZ', _(u'Kazakhstan')),
        ('KE', _(u'Kenya')),
        ('KI', _(u'Kiribati')),
        ('KP', _(u"Korea, Democratic People's Republic of")),
        ('KR', _(u'Korea, Republic of')),
        ('KW', _(u'Kuwait')),
        ('KG', _(u'Kyrgyzstan')),
        ('LA', _(u"Lao People's Democratic Republic")),
        ('LV', _(u'Latvia')),
        ('LB', _(u'Lebanon')),
        ('LS', _(u'Lesotho')),
        ('LR', _(u'Liberia')),
        ('LY', _(u'Libya')),
        ('LI', _(u'Liechtenstein')),
        ('LT', _(u'Lithuania')),
        ('LU', _(u'Luxembourg')),
        ('MO', _(u'Macao')),
        ('MK', _(u'Macedonia, The Former Yugoslav Republic of')),
        ('MG', _(u'Madagascar')),
        ('MW', _(u'Malawi')),
        ('MY', _(u'Malaysia')),
        ('MV', _(u'Maldives')),
        ('ML', _(u'Mali')),
        ('MT', _(u'Malta')),
        ('MH', _(u'Marshall Islands')),
        ('MQ', _(u'Martinique')),
        ('MR', _(u'Mauritania')),
        ('MU', _(u'Mauritius')),
        ('YT', _(u'Mayotte')),
        ('MX', _(u'Mexico')),
        ('FM', _(u'Micronesia, Federated States of')),
        ('MD', _(u'Moldova, Republic of')),
        ('MC', _(u'Monaco')),
        ('MN', _(u'Mongolia')),
        ('ME', _(u'Montenegro')),
        ('MS', _(u'Montserrat')),
        ('MA', _(u'Morocco')),
        ('MZ', _(u'Mozambique')),
        ('MM', _(u'Myanmar')),
        ('NA', _(u'Namibia')),
        ('NR', _(u'Nauru')),
        ('NP', _(u'Nepal')),
        ('NL', _(u'Netherlands')),
        ('NC', _(u'New Caledonia')),
        ('NZ', _(u'New Zealand')),
        ('NI', _(u'Nicaragua')),
        ('NE', _(u'Niger')),
        ('NG', _(u'Nigeria')),
        ('NU', _(u'Niue')),
        ('NF', _(u'Norfolk Island')),
        ('MP', _(u'Northern Mariana Islands')),
        ('NO', _(u'Norway')),
        ('OM', _(u'Oman')),
        ('PK', _(u'Pakistan')),
        ('PW', _(u'Palau')),
        ('PS', _(u'Palestinian Territory, Occupied')),
        ('PA', _(u'Panama')),
        ('PG', _(u'Papua New Guinea')),
        ('PY', _(u'Paraguay')),
        ('PE', _(u'Peru')),
        ('PH', _(u'Philippines')),
        ('PN', _(u'Pitcairn')),
        ('PL', _(u'Poland')),
        ('PT', _(u'Portugal')),
        ('PR', _(u'Puerto Rico')),
        ('QA', _(u'Qatar')),
        ('RE', _(u'R\xe9union')),
        ('RO', _(u'Romania')),
        ('RU', _(u'Russian Federation')),
        ('RW', _(u'Rwanda')),
        ('BL', _(u'Saint Barth\xe9lemy')),
        ('SH', _(u'Saint Helena, Ascension and Tristan Da Cunha')),
        ('KN', _(u'Saint Kitts and Nevis')),
        ('LC', _(u'Saint Lucia')),
        ('MF', _(u'Saint Martin (French Part)')),
        ('PM', _(u'Saint Pierre and Miquelon')),
        ('VC', _(u'Saint Vincent and the Grenadines')),
        ('WS', _(u'Samoa')),
        ('SM', _(u'San Marino')),
        ('ST', _(u'Sao Tome and Principe')),
        ('SA', _(u'Saudi Arabia')),
        ('SN', _(u'Senegal')),
        ('RS', _(u'Serbia')),
        ('SC', _(u'Seychelles')),
        ('SL', _(u'Sierra Leone')),
        ('SG', _(u'Singapore')),
        ('SX', _(u'Sint Maarten (Dutch Part)')),
        ('SK', _(u'Slovakia')),
        ('SI', _(u'Slovenia')),
        ('SB', _(u'Solomon Islands')),
        ('SO', _(u'Somalia')),
        ('ZA', _(u'South Africa')),
        ('GS', _(u'South Georgia and the South Sandwich Islands')),
        ('SS', _(u'South Sudan')),
        ('ES', _(u'Spain')),
        ('LK', _(u'Sri Lanka')),
        ('SD', _(u'Sudan')),
        ('SR', _(u'Suriname')),
        ('SJ', _(u'Svalbard and Jan Mayen')),
        ('SZ', _(u'Swaziland')),
        ('SE', _(u'Sweden')),
        ('CH', _(u'Switzerland')),
        ('SY', _(u'Syrian Arab Republic')),
        ('TW', _(u'Taiwan, Province of China')),
        ('TJ', _(u'Tajikistan')),
        ('TZ', _(u'Tanzania, United Republic of')),
        ('TH', _(u'Thailand')),
        ('TL', _(u'Timor-leste')),
        ('TG', _(u'Togo')),
        ('TK', _(u'Tokelau')),
        ('TO', _(u'Tonga')),
        ('TT', _(u'Trinidad and Tobago')),
        ('TN', _(u'Tunisia')),
        ('TR', _(u'Turkey')),
        ('TM', _(u'Turkmenistan')),
        ('TC', _(u'Turks and Caicos Islands')),
        ('TV', _(u'Tuvalu')),
        ('UG', _(u'Uganda')),
        ('UA', _(u'Ukraine')),
        ('AE', _(u'United Arab Emirates')),
        ('GB', _(u'United Kingdom')),
        ('US', _(u'United States')),
        ('UM', _(u'United States Minor Outlying Islands')),
        ('UY', _(u'Uruguay')),
        ('UZ', _(u'Uzbekistan')),
        ('VU', _(u'Vanuatu')),
        ('VE', _(u'Venezuela, Bolivarian Republic of')),
        ('VN', _(u'Viet Nam')),
        ('VG', _(u'Virgin Islands, British')),
        ('VI', _(u'Virgin Islands, U.S.')),
        ('WF', _(u'Wallis and Futuna')),
        ('EH', _(u'Western Sahara')),
        ('YE', _(u'Yemen')),
        ('ZM', _(u'Zambia')),
        ('ZW', _(u'Zimbabwe')),
    )


    birthday = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES),\
         required=False)

    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.Select(attrs={
        'class':'select-large',
    }))

    country = forms.ChoiceField(choices=COUNTRIES,widget=forms.Select(attrs={
        'class':'select-large',
    }),required=False)

    url = forms.URLField(required=False,widget=forms.TextInput(attrs={
        'class':'config-large',
    }),error_messages={
        'invalid':u'Digite uma URL válida'
    })

    city = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'class':'config-large',
        'placeholder':u'Digite o nome da sua cidade',
    }))

    image = forms.ImageField(required=False,widget=AdminImageWidget)
    nickname = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'input-large',
            }), error_messages={'required': u'Digite um apelido'})

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if UserProfile.objects.filter(nickname=nickname).exclude(id=self.instance.id):
            raise forms.ValidationError(u'Apelido já em uso, escolha outro')
        return nickname

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image._size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(u'Tamanho limite da imagem: 3MB')
        return image


    class Meta:
        model = UserProfile
        exclude = ('user',)
