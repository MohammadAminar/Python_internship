from django import forms
class TeacherModel(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TeacherModel, self).__init__(*args, **kwargs)
        for item in TeacherModel.visible_fields(self):
            item.field.widget.attrs['class'] = 'form-control'

    User_Id = forms.CharField(widget=forms.HiddenInput, required=True, initial=0, label='')
    FirstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'امین'}),
                                max_length=50,
                                required=True,
                                label='نام')
    LastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'عرب پور'}),
                               max_length=50,
                               required=True,
                               label='نام خانوادگی')
    International_Code = forms.CharField(widget=forms.TextInput,
                                         max_length=10,
                                         required=True,
                                         label='کد ملی',
                                         error_messages={'Error': 'کد ملی نامعتبر است'})
    Phone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': '09*********'}),
                            max_length=11,
                            required=True,
                            label='شماره تلفن',
                            error_messages={'Error': 'شماره تلفن معتبر نیست'})
    Username = forms.CharField(widget=forms.TextInput,
                               max_length=50,
                               required=True,
                               label='نام کاربری',
                               error_messages={'Error': 'نام کاربری را صحیح وارد کنید'})
    Password = forms.CharField(widget=forms.PasswordInput,
                               max_length=50,
                               required=True,
                               min_length=8,
                               label='رمز عبور',
                               error_messages={'Error': 'رمز عبور کوتاه است'})
    Code_vezarat_olom = forms.CharField(widget=forms.TextInput,
                                        max_length=10,
                                        required=True,
                                        label='کد وزارت علوم',
                                        error_messages={'Error': 'کد وزارت علوم نامعتبر است'})

    CHOICES = [
        ('True', 'بله'),
        ('False', 'خیر'),
    ]

    Work_experience = forms.ChoiceField(label='تجربه کاری',
                                        choices=CHOICES,
                                        required=True)
    Education = forms.CharField(widget=forms.TextInput,
                                max_length=50,
                                required=True,
                                label='تحصیلات')
class StudentModel(forms.Form):
    def __init__(self, *args, **kwargs):
        super(StudentModel, self).__init__(*args, **kwargs)
        for item in StudentModel.visible_fields(self):
            item.field.widget.attrs['class'] = 'form-control'

    User_Id = forms.CharField(widget=forms.HiddenInput, required=True, initial=0, label='')
    FirstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'امین'}),
                                max_length=50,
                                required=True,
                                label='نام')
    LastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'عرب پور'}),
                               max_length=50,
                               required=True,
                               label='نام خانوادگی')
    International_Code = forms.CharField(widget=forms.TextInput,
                                         max_length=10,
                                         required=True,
                                         label='کد ملی',
                                         error_messages={'Error': 'کد ملی نامعتبر است'})
    Phone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': '09*********'}),
                            max_length=11,
                            required=True,
                            label='شماره تلفن',
                            error_messages={'Error': 'شماره تلفن معتبر نیست'})
    Username = forms.CharField(widget=forms.TextInput,
                               max_length=50,
                               required=True,
                               label='نام کاربری',
                               error_messages={'Error': 'نام کاربری را صحیح وارد کنید'})
    Password = forms.CharField(widget=forms.PasswordInput,
                               max_length=50,
                               required=True,
                               min_length=8,
                               label='رمز عبور',
                               error_messages={'Error': 'رمز عبور کوتاه است'})
    Education_level = forms.CharField(widget=forms.TextInput,
                                      label='سطح تحصیلات',
                                      max_length=50,
                                      required=True,
                                      error_messages={'required': 'لطفا سطح تحصیلات را وارد کنید'})

    DEBT_STATUS_CHOICES = [
        ('SUSPENDED', 'معلق شده'),
        ('PAID', 'پرداخت شده'),
        ('UNPAID', 'پرداخت نشده'),
    ]

    Debt_status = forms.ChoiceField(choices=DEBT_STATUS_CHOICES,
                                    label='وضعیت بدهی')
class ManagerModel(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ManagerModel, self).__init__(*args, **kwargs)
        for item in ManagerModel.visible_fields(self):
            item.field.widget.attrs['class'] = 'form-control'

    User_Id = forms.CharField(widget=forms.HiddenInput, required=True, initial=0, label='')
    FirstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'امین'}),
                                max_length=50,
                                required=True,
                                label='نام')
    LastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'عرب پور'}),
                               max_length=50,
                               required=True,
                               label='نام خانوادگی')
    International_Code = forms.CharField(widget=forms.TextInput,
                                         max_length=10,
                                         required=True,
                                         label='کد ملی',
                                         error_messages={'Error': 'کد ملی نامعتبر است'})
    Phone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': '09*********'}),
                            max_length=11,
                            required=True,
                            label='شماره تلفن',
                            error_messages={'Error': 'شماره تلفن معتبر نیست'})
    Username = forms.CharField(widget=forms.TextInput,
                               max_length=50,
                               required=True,
                               label='نام کاربری',
                               error_messages={'Error': 'نام کاربری را صحیح وارد کنید'})
    Password = forms.CharField(widget=forms.PasswordInput,
                               max_length=50,
                               required=True,
                               min_length=8,
                               label='رمز عبور',
                               error_messages={'Error': 'رمز عبور کوتاه است'})
class ParentModel(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ParentModel, self).__init__(*args, **kwargs)
        for item in ParentModel.visible_fields(self):
            item.field.widget.attrs['class'] = 'form-control'

    User_Id = forms.CharField(widget=forms.HiddenInput, required=True, initial=0, label='')
    FirstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'امین'}),
                                max_length=50,
                                required=True,
                                label='نام')
    LastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'عرب پور'}),
                               max_length=50,
                               required=True,
                               label='نام خانوادگی')
    International_Code = forms.CharField(widget=forms.TextInput,
                                         max_length=10,
                                         required=True,
                                         label='کد ملی',
                                         error_messages={'Error': 'کد ملی نامعتبر است'})
    Phone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': '09*********'}),
                            max_length=11,
                            required=True,
                            label='شماره تلفن',
                            error_messages={'Error': 'شماره تلفن معتبر نیست'})
    Username = forms.CharField(widget=forms.TextInput,
                               max_length=50,
                               required=True,
                               label='نام کاربری',
                               error_messages={'Error': 'نام کاربری را صحیح وارد کنید'})
    Password = forms.CharField(widget=forms.PasswordInput,
                               max_length=50,
                               required=True,
                               min_length=8,
                               label='رمز عبور',
                               error_messages={'Error': 'رمز عبور کوتاه است'})
    Number_of_children = forms.IntegerField(label='تعداد فرزندان در این مدرسه',
                                            required=True)
