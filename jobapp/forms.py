from django import forms
from .models import Job_Post, Recruiter_Register, Job_Seeker_Register, Job_Apply, Create_CV_Basic_info, Create_CV_Add_Referance, Create_CV_Job_Experience, Create_CV_Language_Profiency, Create_CV_Traning, Create_CV_Academic_Qualification
from ckeditor.widgets import CKEditorWidget

class new_job_form(forms.ModelForm):
    job_deadline = forms.DateField(input_formats=['%Y-%m-%d'],
    widget=forms.DateInput(attrs={
        'class':'datepicker-input',
        'data-target':'#datepicker1',
        'type':'Date'
    }))
    class Meta:
        model = Job_Post
        fields = [
            'title',
            'category',
            'salary',
            'prefered_gender',
            'prefered_age',
            'prefered_Division',
            'vacancy',
            'education',
            'experience',
            'job_deadline',
            'job_description',
        ]

class Job_Seeker_Register_Form(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Full Name'
    }))
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Full Name'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Username'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Email'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Password'
    }))
    
    class Meta:
        model = Job_Seeker_Register
        fields = [
            'full_name',
            'username',
            'email',
            'password',
        ]


class Recruiter_Register_Form(forms.ModelForm):
    company_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Company Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Company Email'
    }))
    company_url = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'abc.com'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Password'
    }))
    company_location = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Company Location',
        'rows': 2
    }))
    company_description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Company Detail',
        'rows': 5
    }))
    class Meta:
        model = Recruiter_Register
        fields = [
            'company_name',
            'email',
            'company_url',
            'username',
            'password',
            'company_location',
            'company_description',
            'picture',
        ]

class Job_Apply_Form(forms.ModelForm):
    phone_No = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))
    expected_salary = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))
    cv = forms.CharField(widget=forms.FileInput(attrs={
        'class': 'form-control',
    }))
    class Meta:
        model = Job_Apply
        fields = [
            'phone_No',
            'expected_salary',
            'cv',
        ]


class CV_Basic_Info_Form(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Last Name'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Email'
    }))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Phone Number'
    }))
    father_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Father Name'
    }))
    mother_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Mother Name'
    }))
    date_of_birth = forms.CharField(widget=forms.DateInput(attrs={
        'class': 'form-control mb-4',
        'type': 'date'
    }))
    nationalilty = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Nationality'
    }))
    nid = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'NID Number'
    }))
    current_address = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Current Address',
        'rows':3
    }))
    parmanant_address = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Parmanant Address',
        'rows':3
    }))

    class Meta:
        model = Create_CV_Basic_info
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_no',
            'gender',
            'father_name',
            'mother_name',
            'date_of_birth',
            'marrige_status',
            'nationalilty',
            'nid',
            'religion',
            'current_address',
            'parmanant_address',
        ]


class Create_CV_Academic_Form(forms.ModelForm):
    exam_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Exam Title'
    }))
    major = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Major'
    }))
    passing_year = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Passing Year'
    }))
    Institute = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Institute'
    }))
    cgpa = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'CGPA'
    }))
    duration = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Course Duration'
    }))
    class Meta:
        model = Create_CV_Academic_Qualification
        fields = [
            'exam_name',
            'major',
            'Institute',
            'passing_year',
            'cgpa',
            'duration',
        ]


class Create_CV_Traning_Form(forms.ModelForm):
    traning_title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Training Title'
    }))
    topic = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Training Topics'
    }))
    training_year = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Training Year'
    }))
    duration = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Training Duration'
    }))
    achievement = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Training Achievement'
    }))
    class Meta:
        model=Create_CV_Traning
        fields = [
            'traning_title',
            'topic',
            'training_year',
            'duration',
            'achievement',
        ]


class Create_CV_Job_Experience_Form(forms.ModelForm):
    designation = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Your Designation'
    }))
    company_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Company Name'
    }))
    company_location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Company Location'
    }))
    start_date = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'type': 'Date',

    }))
    end_date = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'type': 'Date'
    }))
    class Meta:
        model = Create_CV_Job_Experience
        fields = {
            'designation',
            'company_name',
            'company_location',
            'start_date',
            'end_date',
        }


class Create_CV_Add_Referance_Form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Name'
    }))
    designation = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Designation'
    }))
    company_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Company Name'
    }))
    company_location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Company Location'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Email'
    }))
    mobile = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Mobile Number'
    }))
    class Meta:
        model = Create_CV_Add_Referance
        fields = [
            'name',
            'designation',
            'company_name',
            'company_location',
            'email',
            'mobile',
        ]



