from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Recruiter_Register(models.Model):
    company_name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    company_url = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=20)
    company_location = models.TextField()
    company_description = models.TextField()
    picture = models.ImageField()

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name='Recruirer Register'
        verbose_name_plural='Recruirer Registers'


class Job_Seeker_Register(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=20)
    picture = models.ImageField(blank=True, null=True, default='avatar.png')
    about_me = models.TextField(null=True, blank=True)
    current_Adrress = models.TextField(null=True, blank=True)
    parmanant_Adrress = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name='Job Seeker Register'
        verbose_name_plural='Job Seeker Registers'


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Job_Post(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter_Register, on_delete=models.CASCADE)
    salary = models.CharField(max_length=120)
    gender_choise = (
    ('M','Male'),
    ('F','Female'),
    ('B','Male & Female')
    )
    prefered_gender = models.CharField(max_length=1,default=3, choices=gender_choise)
    vacancy = models.CharField(max_length=10)
    education = models.CharField(max_length=120)
    place_choise = (
        ('AW','Any Where'),
        ('DH','Dhaka'),
        ('RH','Rajshahi'),
        ('BR','Borishal'),
        ('KH','Khulna'),
        ('SY','Shylet'),
        ('KM','Kumilla'),
        ('RR','Rongpur'),
    )
    prefered_Division = models.CharField(max_length=2, default=1, choices=place_choise)
    job_description = models.TextField()
    experience_choise = (
        ('NO','No'),
        ('ON','1 year'),
        ('TW','2 years'),
        ('TH','3 years'),
        ('FV','5 years'),
        ('TN','10 years'),
        ('AT','Above 10 years'),
    )
    experience = models.CharField(max_length=2, default=1, choices=experience_choise)
    age_choise = (
        ('UT','Under 20'),
        ('TT','21-30'),
        ('TF','31-40'),
        ('FF','41-50'),
        ('AF','Above 50'),
    )
    prefered_age = models.CharField(max_length=2, default=2, choices=age_choise)
    job_deadline = models.DateField()
    posted_date = models.DateField(auto_now_add=True)
    posted_time = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Job Post'
        verbose_name_plural='Job Posts'


class Job_Apply(models.Model):
    job = models.ForeignKey(Job_Post, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter_Register, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(Job_Seeker_Register, on_delete=models.CASCADE)
    phone_No = models.CharField(max_length=20)
    expected_salary = models.CharField(max_length=10)
    cv = models.FileField()
    applying_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.job.title

    class Meta:
        verbose_name='Job Apply'
        verbose_name_plural='Job Applys'


class NotificationForRecruiter(models.Model):
    recruiter = models.ForeignKey(Recruiter_Register, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_view = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Job Apply Notification'
        verbose_name_plural='Job Apply Notifications'

class Blog_Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField()
    description = models.TextField()
    post_at = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Blog Post'
        verbose_name_plural='Blog Posts'

class Create_Interview(models.Model):
    job = models.ForeignKey(Job_Post, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter_Register, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name='Create Interview'
        verbose_name_plural='Create Interviews'

class Interview_Notification(models.Model):
    job = models.ForeignKey(Job_Post, on_delete=models.CASCADE)
    jobseeker = models.ForeignKey(Job_Seeker_Register, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_view = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Interview Notification'
        verbose_name_plural='Interview Notifications'


class Create_CV_Basic_info(models.Model):
    # Basic Info
    cv_jobseeker = models.ForeignKey(Job_Seeker_Register, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=120, null=True, blank=True)
    phone_no = models.CharField(max_length=15, null=True, blank=True)
    gender_type = (
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    )
    gender = models.CharField(max_length=1, default=1, choices=gender_type)
    father_name = models.CharField(max_length=120, null=True, blank=True)
    mother_name = models.CharField(max_length=120, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    marrige_choise = (
        ('S','Single'),
        ('M','Married'),
        ('D','Divorced'),
    )
    marrige_status = models.CharField(max_length=1, default=1, choices=marrige_choise)
    nationalilty = models.CharField(max_length=100, null=True, blank=True)
    nid = models.IntegerField(null=True, blank=True)
    religion_choise = (
        ('I','Islam'),
        ('H','Hindusim'),
        ('K','Christian'),
        ('B','Boddho'),
        ('O','Others'),
    )
    religion = models.CharField(max_length=1, default=1, choices=religion_choise)
    current_address = models.TextField(null=True, blank=True)
    parmanant_address = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name='CV Basic Info'
        verbose_name_plural='CV Basic Infos'


class Create_CV_Signiture(models.Model):
    cv_jobseeker = models.ForeignKey(Job_Seeker_Register, on_delete=models.CASCADE)
    signiture = models.ImageField(default='sign.png')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cv_jobseeker.username

    class Meta:
        verbose_name='CV Singature'
        verbose_name_plural='CV Singatures'


class Create_CV_Picture(models.Model):
    cv_jobseeker = models.ForeignKey(Job_Seeker_Register, on_delete=models.CASCADE)
    picture = models.ImageField(default='avatar.png')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cv_jobseeker.username

    class Meta:
        verbose_name='CV Picture'
        verbose_name_plural='CV Pictures'

class Create_CV_Career_Objective(models.Model):
    cv_jobseeker = models.ForeignKey(Job_Seeker_Register, on_delete=models.CASCADE)
    career_objective = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cv_jobseeker.username

    class Meta:
        verbose_name='CV Career Objective'
        verbose_name_plural='CV Career Objecttives'


class Create_CV_Skill(models.Model):
    cv_jobseeker = models.ForeignKey(Job_Seeker_Register, on_delete=models.CASCADE)
    skill_and_specialize = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cv_jobseeker.username

    class Meta:
        verbose_name='CV Skill & Specialization'
        verbose_name_plural='CV Skills & Specializations'


class Create_CV_Hobby(models.Model):
    cv_jobseeker = models.ForeignKey(Job_Seeker_Register, on_delete=models.CASCADE)
    hobby = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cv_jobseeker.username

    class Meta:
        verbose_name='CV Hobby & Interest'
        verbose_name_plural='CV Hobbies & Interests'


class Create_CV_Academic_Qualification(models.Model):
    cv_jobseeker = models.ForeignKey(Job_Seeker_Register, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=50)
    major = models.CharField(max_length=120)
    Institute = models.CharField(max_length=250)
    passing_year = models.CharField(max_length=10)
    cgpa = models.CharField(max_length=30)
    duration = models.CharField(max_length=50, null=True, blank=True, default="---")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.exam_name

    class Meta:
        verbose_name='CV Academic Qualification'
        verbose_name_plural='CV Academic Qualifications'


class Create_CV_Traning(models.Model):
    cv_jobseeker = models.ForeignKey(Job_Seeker_Register, on_delete=models.CASCADE)
    traning_title = models.CharField(max_length=120)
    topic = models.CharField(max_length=150)
    training_year = models.CharField(max_length=30)
    duration = models.CharField(max_length=50)
    achievement = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.traning_title

    class Meta:
        verbose_name='CV Traning Summary'
        verbose_name_plural='CV Traning Summaries'


class Create_CV_Job_Experience(models.Model):
    cv_jobseeker = models.ForeignKey(Job_Seeker_Register, on_delete=models.CASCADE)
    designation = models.CharField(max_length=120)
    company_name = models.CharField(max_length=200)
    company_location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    is_still_work = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name='CV Job Experience'
        verbose_name_plural='CV Job Experiences'


class Create_CV_Language_Profiency(models.Model):
    cv_jobseeker = models.ForeignKey(Job_Seeker_Register, on_delete=models.CASCADE)
    language = models.CharField(max_length=120)
    profiency = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name='CV Language Profiency'
        verbose_name_plural='CV Language Profiencies'


class Create_CV_Add_Referance(models.Model):
    cv_jobseeker = models.ForeignKey(Job_Seeker_Register, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    designation = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_location = models.CharField(max_length=200)
    email = models.EmailField(max_length=150, null=True, blank=True)
    mobile = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='CV Job Referance'
        verbose_name_plural='CV Job Referances'

