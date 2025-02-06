from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, null=True, default='@luiss.it', blank= True)
    FRESHMAN = 'FR'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    PROFESSOR = 'PR'
    ROLE = [
        (FRESHMAN, 'Freshman'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
        (PROFESSOR, 'Professor')
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=ROLE,
        default=FRESHMAN,
    )
    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.year_in_school}'

class Course(models.Model):
    # class instances/variables
    name = models.CharField(max_length=100)
    ssd = models.CharField(max_length=10)
    code = models.CharField(max_length=10)
    cfu = models.IntegerField()
    description = models.TextField(default=None, null=True, blank=True)
    teacher = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        blank=True, default=None, null=True)
    FIRST = 1
    SECOND = 2
    THIRD = 3
    YEARS = [(FIRST, 'First year'),(SECOND, 'Second year'),(THIRD, 'Third year'),]
    SEMESTERS = [(FIRST, 'First semester'),(SECOND, 'Second semester'),]
    course_year = models.IntegerField(choices=YEARS,default=FIRST,)
    course_semester = models.IntegerField(choices=SEMESTERS,default=FIRST,)
    def __str__(self):
        return f'Course: {self.name}'

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(default= "img/300-erasmus-luiss_4.jpeg")
    description = models.TextField(null=True, blank=True)
    accomplish_date = models.DateField(null=True, blank=True)
    person = models.ManyToManyField(Person, blank=True, default=None)

    def __str__(self):
        return self.title

class New(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(default= "img/300-erasmus-luiss_4.jpeg") #saves the images in news-img folder inside img
    def __str__(self):
        return self.title

#c1 = Course(name='Fundamentals of Management', ssd='SECS-P/08', code='TDS04', cfu=8, teacher =)
#p1= Person(firsts)
#c2 = Course(name='Introduction to Computer Programming', ssd='ING-INF/05', code='TDS03', cfu=6, teacher =)