from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.validators import MaxValueValidator
from django.db.models import Count

STATUS_ACADEMIC = (
    ('85', 'Doctoral Degree'),
    ('65', 'Masters Degree'),
    ('45', 'Bachelors Degree')
)
STATUS_ADDITIONAL = (
    ('5', 'Doctorals Degree'),
    ('4', 'Masters Degree'),
    ('3', 'Bachelors Degree')
)
PROF_DEVAA = (
    ('0', 'None'),
    ('3', 'Summa Cum Laude'),
    ('2', 'Magna Cum Laude'),
    ('1', 'Cum Laude'),
    ('0.5', 'With distinction')
)
CIVIL_STATUS = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('spouse', 'Spouse')
)
ELIGIBILITY_CIVIL = (
    ('none', 'None'),
    ('yes', 'License for CE')
)
ELIGIBILITY_MECHANICAL = (
    ('none', 'None'),
    ('yes', 'License for ME')
)
ELIGIBILITY_ELECTRICAL = (
    ('none', 'None'),
    ('yes', 'License for EE')
)
ELIGIBILITY_ARCHITECT = (
    ('none', 'None'),
    ('yes', 'License for Architect')
)
ELIGIBILITY_NURSE = (
    ('none', 'None'),
    ('yes', 'License for Nurse')
)


class Applicant(models.Model):
    class Meta:
        verbose_name = "Instructor I - Computer Science / IT"
        verbose_name_plural = "Instructor I - Computer Science / IT"

    fname = models.CharField(max_length=100, verbose_name="First name ")
    mname = models.CharField(max_length=100, verbose_name="Middle name ")
    lname = models.CharField(max_length=100, verbose_name="Last name ")
    address = models.CharField(max_length=100, verbose_name="Adress ", help_text="zone/street/barangay/province or city/house no.")
    phone_number = models.CharField(max_length=11, verbose_name="Phone Number ")
    Age = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Age ")
    License = models.BooleanField(verbose_name="LET ")
    Civil_Status = models.CharField(max_length=7, choices=CIVIL_STATUS, verbose_name="Civil Status", default=" ")
    date_recorded = models.DateTimeField(default=timezone.now, editable=False)
    Academic = models.CharField(max_length=4, verbose_name="Educational Qualification ", choices=STATUS_ACADEMIC, default='', help_text='Highest academic degree or educational attainment in the field of study')
    Special = models.BooleanField(verbose_name='Special Course ', help_text='e.g. Technical/Technician')
    Additional1 = models.BooleanField(help_text="Graduate of five-year Engineering Degree", verbose_name="additional 5 points")
    Additional2 = models.BooleanField(help_text="Licensure Exam", verbose_name="additional 5 points")
    Degree = models.CharField(max_length=3, verbose_name="Question 1 ", choices=STATUS_ADDITIONAL, default='', help_text="Additional Equivalent degree earned, related to the present position")
    Additional3 = models.PositiveIntegerField(validators=[MaxValueValidator(50)], default=0, help_text="For every 3 credits earned toward a higher approved degree course", verbose_name="Question 2 ")
    Additional4 = models.PositiveIntegerField(validators=[MaxValueValidator(50)], default=0, help_text="For every 3 credits earned on the same level", verbose_name="Question 3 ")
    A1 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every full year-time academic service in a state institution of higher learning", verbose_name="Question 4 ")
    A2 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every full year-time academic service in any public or private educational institution other than SUC", verbose_name="Question 5 ")
    A3 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Computer Analyst ")
    A4 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Software Engineer ")
    A5 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Senior Programmer ")
    A6 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Junior Programmer ")
    A7 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Computer Encoder ")
    A8 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="for every cost and timesaving innovation, patented inventions and creative work as well as discovery of educational,technical,scientific and/or cultural value", verbose_name="Question 6 ")
    A9 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as original author ")
    A10 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as co-author ")
    A11 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as reviewer ")
    A12 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as translator ")
    A13 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as editor ")
    A14 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as compiler ")
    A15 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="International ")
    A16 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="National/Regional ")
    A17 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="Local ")
    A18 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="For every Instructional Manual/Audio-Visual Materials ")
    A19 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    A20 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    A21 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every training course with a duration of at least (pro-rated for less than a year)", verbose_name="c.Local")
    A22 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    A23 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    A24 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For participation as a consultant, expert in any activity of an educational, technological, professional, scientific, or cultural nature (abroad and local) sponsored by the government or other agencies ", verbose_name="c.Local")
    A25 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    A26 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    A27 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For participation as coordinator,lecturer,resource person or guest speaker in conferences,workshops and/or training", verbose_name="c.Local")
    A28 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    A29 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    A30 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For official participation in conferences, seminar, workshops ", verbose_name="c.Local")
    A31 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For expert services as adviser in doctoral dissertation and masteral thesis and undergraduate thesis ", verbose_name="expert services")
    A32 = models.PositiveIntegerField(validators=[MaxValueValidator(10000)], default=0, help_text="1/120 hrs ", verbose_name="For certified training")
    A33 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="National", verbose_name="a.Offical ")
    A34 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Local", verbose_name="Local ")
    A35 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Member", verbose_name="b.Member ")
    A36 = models.CharField(choices=PROF_DEVAA, default='', max_length=5, verbose_name="For undergraduate academic honors earned:")
    A37 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive, International", verbose_name="Competitive, International ")
    A38 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, International", verbose_name="Non-Competitive, International ")
    A39 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive National/Regional", verbose_name="Competitive National/Regional ")
    A40 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, National/Regional", verbose_name="on-Competitive, National/Regional ")
    A41 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive, Local", verbose_name="Competitive, Local ")
    A42 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, Local", verbose_name="Non-Competitive, Local ")
    A43 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="International", verbose_name="a.International")
    A44 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="National/Regional", verbose_name="b.National/Regional")
    A45 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Local", verbose_name="c.Local")
    A46 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every year of participation in service-oriented project in the community", verbose_name="For every year of participation in service-oriented project in the community")
    A47 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="First Level", verbose_name="1.First Level ")
    A48 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Second Level", verbose_name="2.Second Level ")
    A49 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Others", verbose_name="3.Others ")
    Practical_Exam = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Practical exam ")
    Class_Demo = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Class demo ")
    Voice_speech = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Voice and Speech")
    Appearance = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Appearance")
    Alertness = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Alertness")
    Ability = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Ability to Present Ideas")
    Judgement = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Judgement")
    Emotional_stability = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Emotional Stability")
    Self_confidence = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Self-Confidence")
    total = models.PositiveIntegerField(blank=True, null=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', verbose_name='user ')

    @property
    def AA1(self):
        return self.A1

    @property
    def AA2(self):
        return self.A2 * .75

    @property
    def AA3(self):
        return self.A3 * 2

    @property
    def AA4(self):
        return self.A4 * 1.75

    @property
    def AA5(self):
        return self.A5 * 1.50

    @property
    def AA6(self):
        return self.A6 * 1.25

    @property
    def AA7(self):
        return self.A7 * 1

    @property
    def AA8(self):
        return self.A8 * 7

    @property
    def AA9(self):
        return self.A9 * 5

    @property
    def AA10(self):
        return self.A10 * 3

    @property
    def AA11(self):
        return self.A11 * 3

    @property
    def AA12(self):
        return self.A12 * 3

    @property
    def AA13(self):
        return self.A13 * 2

    @property
    def AA14(self):
        return self.A14 * 2

    @property
    def AA15(self):
        return self.A15 * 5

    @property
    def AA16(self):
        return self.A16 * 3

    @property
    def AA17(self):
        return self.A17 * 2

    @property
    def AA18(self):
        return self.A18 * 2

    @property
    def AA19(self):
        return self.A19 * 4

    @property
    def AA20(self):
        return self.A20 * 3

    @property
    def AA21(self):
        return self.A21 * 2

    @property
    def AA22(self):
        return self.A22 * 5

    @property
    def AA23(self):
        return self.A23 * 3

    @property
    def AA24(self):
        return self.A24 * 2

    @property
    def AA25(self):
        return self.A25 * 5

    @property
    def AA26(self):
        return self.A26 * 3

    @property
    def AA27(self):
        return self.A27 * 2

    @property
    def AA28(self):
        return self.A28 * 3

    @property
    def AA29(self):
        return self.A29 * 2

    @property
    def AA30(self):
        return self.A30 * 1

    @property
    def AA31(self):
        return self.A31 * 1

    @property
    def AA32(self):
        return self.A32 / 120

    @property
    def AA33(self):
        return self.A33 * 2

    @property
    def AA34(self):
        return self.A34 * 1.5

    @property
    def AA35(self):
        return self.A35 * 1

    @property
    def AA36(self):
        if self.A36 == '3':
            return 3
        elif self.A36 == '2':
            return 2
        elif self.A36 == '1':
            return 1
        elif self.A36 == '0.5':
            return 0.5
        else:
            return 0

    @property
    def AA37(self):
        return self.A37 * 5

    @property
    def AA38(self):
        return self.A38 * 3

    @property
    def AA39(self):
        return self.A39 * 3

    @property
    def AA40(self):
        return self.A40 * 2

    @property
    def AA41(self):
        return self.A41 * 1

    @property
    def AA42(self):
        return self.A42 * 1

    @property
    def AA43(self):
        return self.A43 * 5

    @property
    def AA44(self):
        return self.A44 * 3

    @property
    def AA45(self):
        return self.A45 * 2

    @property
    def AA46(self):
        return self.A46 * 1

    @property
    def AA47(self):
        return self.A47 * 1

    @property
    def AA48(self):
        return self.A48 * 2

    @property
    def AA49(self):
        return self.A49 * .5

    @property
    def exam(self):
        return self.Practical_Exam * .15

    @property
    def educ_qua(self):
        if self.Academic == '85':
            return round(self.doct, 3)
        elif self.Academic == '65':
            return round(self.mast, 3)
        else:
            return round(self.bach, 3)

    @property
    def Educ_Qual(self):
        if self.educ_qua > 34:
            return 85 * .40
        else:
            return self.educ_qua

    @property
    def deg(self):
        if self.Additional3 != 0 and self.Additional4 != 0:
            return ((self.Additional3 / 3) * 1) + ((self.Additional4 / 3) * .5)
        elif self.Additional3 != 0:
            return (self.Additional3 / 3) * 1
        elif self.Additional4 != 0:
            return (self.Additional4 / 3) * .5
        else:
            return 0

    @property
    def doct(self):
        if self.Academic == '85':
            return 85 * .40
        else:
            return 0

    @property
    def mast(self):
        if self.Academic == '65' and self.Special == 1 and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((69 + 25 + self.deg + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((69 + self.deg + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional2 and self.deg != 0:
            return round((69 + 25 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 and self.deg != 0:
            return round((69 + 25 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 == 1 and self.Additional2:
            return round((69 + 25 + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional1 == 1 and self.Additional2:
            return round((69 + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.deg != 0:
            return round((69 + 25 + self.deg) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional2:
            return round((69 + 25 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 == 1:
            return round((69 + 25 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg == 1 and self.Additional1 == 1:
            return round((69 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg == 1 and self.Additional1 == 1:
            return round((69 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg != 0:
            return round((69 + self.deg) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional2 == 1:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 + .40
        elif self.Academic == '65' and self.Additional1 == 2:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65':
            return round(69 * .40, 3)
        else:
            return 0

    @property
    def bach(self):
        if self.Academic == '45' and self.Special == 1 and self.Additional1 == 1 and self.Additional2 == 1 and self.deg != 0:
            return round((45 + 25 + self.deg + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((45 + self.deg + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional2 and self.deg != 0:
            return round((45 + 25 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 and self.deg != 0:
            return round((45 + 25 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 == 1 and self.Additional2:
            return round((45 + 25 + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 1 and self.Additional2:
            return round((45 + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.deg != 0:
            return round((45 + 25 + self.deg) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional2:
            return round((45 + 25 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 == 1:
            return round((45 + 25 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg == 1 and self.Additional1 == 1:
            return round((45 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg == 1 and self.Additional1 == 1:
            return round((45 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg != 0:
            return round((45 + self.deg) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional2 == 1:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 2:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45':
            return round(45 * .40, 3)
        else:
            return 0

    @property
    def subtot2(self):
        return self.AA1 + self.AA2 + self.AA3 + self.AA4 + self.AA5 + self.AA6 + self.AA7

    @property
    def Acad_Exp(self):
        if self.subtot2 > 25:
            return round(25 * .15, 3)
        else:
            return round(self.subtot2 * .15, 3)

    @property
    def subtot3(self):
        return self.AA8 + self.AA9 + self.AA10 + self.AA11 + self.AA12 + self.AA13 + self.AA14 + self.AA15 + self.AA16 + self.AA17 + self.AA18 + self.AA19 + self.AA20 + self.AA21 + self.AA22 + self.AA23 + self.AA24 + self.AA25 + self.AA26 + self.AA27 + self.AA28 + self.AA29 + self.AA30 + self.AA31 + self.AA32 + self.AA33 + self.AA34 + self.AA35 + self.AA37 + self.AA38 + self.AA39 + self.AA40 + self.AA41 + self.AA42 + self.AA43 + self.AA44 + self.AA45 + self.AA46 + self.AA47 + self.AA48 + self.AA49 + self.AA36

    @property
    def Prof_Devt(self):
        if self.subtot3 > 45:
            return round(45 * .10, 3)
        else:
            return round(self.subtot3 * .10, 3)

    @property
    def Demo(self):
        return round(self.Class_Demo * .10, 1)

    @property
    def totalin(self):
        return self.Voice_speech + self.Appearance + self.Alertness + self.Ability + self.Judgement + self.Emotional_stability + self.Self_confidence

    @property
    def Interview(self):
        if self.totalin < 7:
            return 0
        else:
            return round(((self.totalin + 65) * .10), 1)

    @property
    def get_totals(self):
        if self.Academic == '85':
            return round((self.doct + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
        elif self.Academic == '65':
            if self.mast < 40:
                return round((self.mast + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
            else:
                return round((40 + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
        elif self.Academic == '45':
            if self.mast < 40:
                return round((self.bach + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
            else:
                return round((40 + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)

    def save(self, *args, **kwargs):
        self.total = self.get_totals
        super(Applicant, self).save(*args, **kwargs)

    @property
    def rank(self):
        aggregate = Applicant.objects.filter(total__gt=self.total).aggregate(ranking=Count('total'))
        return aggregate['ranking'] + 1

    @property
    def remarks(self):
        if self.Academic == '85' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET and lack in minimum average qualification requirements')
            else:
                return('Not yet qualified lack in minimum average qualification requirements')
        elif self.Academic == '85' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit')
            else:
                return('Qualified but exceed in age limit')
        elif self.Academic == '85' and self.Age > 45 and self.total < 60:
                return('Not qualified exceed in age limit')
        elif self.Academic == '85' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET')
            else:
                return('Qualified')
        elif self.Academic == '65' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET, lack in minimum average qualification requirements')
            else:
                return('Not yet qualified lack in minimum average qualification requirements')
        elif self.Academic == '65' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit')
            else:
                return('Qualified but exceed in age limit')
        elif self.Academic == '65' and self.Age > 45 and self.total < 60:
                return('Not qualified exceed in age limit')
        elif self.Academic == '65' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET')
            else:
                return('Qualified')
        elif self.Academic == '45' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET, Masters degree needed, lack in minimum average qualification requirements')
            else:
                return('Not yet qualified masters degree needed, lack in minimum average qualification requirements')
        elif self.Academic == '45' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit, no LET & masters degree needed')
            else:
                return('Not qualified masters degree needed & exceed in age limit')
        elif self.Academic == '45' and self.Age > 45 and self.total < 60:
                return('Not qualified masters degree needed & exceed in age limit')
        elif self.Academic == '45' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET & masters degree needed')
            else:
                return('Not yet qualified masters degree needed')


class Civil_Engr(models.Model):
    class Meta:
        verbose_name = "Instructor I - Civil Engineering"
        verbose_name_plural = "Instructor I - Civil Engineering"
    fname = models.CharField(max_length=100, verbose_name="First name ")
    mname = models.CharField(max_length=100, verbose_name="Middle name ")
    lname = models.CharField(max_length=100, verbose_name="Last name ")
    address = models.CharField(max_length=100, verbose_name="Adress ", help_text="zone/street/barangay/province or city/house no.")
    phone_number = models.CharField(max_length=11, verbose_name="Phone Number ")
    Age = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Age ")
    License = models.BooleanField(verbose_name="LET ")
    Civil_Status = models.CharField(max_length=7, choices=CIVIL_STATUS, verbose_name="Civil Status", default=" ")
    Eligibility = models.CharField(max_length=100, choices=ELIGIBILITY_CIVIL, verbose_name="Eligibility", default=" ")
    date_recorded = models.DateTimeField(default=timezone.now, editable=False)
    Academic = models.CharField(max_length=4, verbose_name="Educational Qualification ", choices=STATUS_ACADEMIC, default='', help_text='Highest academic degree or educational attainment in the field of study')
    Special = models.BooleanField(verbose_name='Special Course ', help_text='e.g. Technical/Technician')
    Additional1 = models.BooleanField(help_text="Graduate of five-year Engineering Degree", verbose_name="additional 5 points")
    Additional2 = models.BooleanField(help_text="Licensure Exam", verbose_name="additional 5 points")
    Degree = models.CharField(max_length=3, verbose_name="Question 1 ", choices=STATUS_ADDITIONAL, default='', help_text="Additional Equivalent degree earned, related to the present position")
    Additional3 = models.PositiveIntegerField(validators=[MaxValueValidator(50)], default=0, help_text="For every 3 credits earned toward a higher approved degree course", verbose_name="Question 2 ")
    Additional4 = models.PositiveIntegerField(validators=[MaxValueValidator(50)], default=0, help_text="For every 3 credits earned on the same level", verbose_name="Question 3 ")
    B1 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every full year-time academic service in a state institution of higher learning", verbose_name="Question 4 ")
    B2 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every full year-time academic service in any public or private educational institution other than SUC", verbose_name="Question 5 ")
    B3 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Project Engineer/Project Manager ")
    B4 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Structural/Design Engineer ")
    B5 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Supervising Engineer ")
    B6 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Construction Engineer ")
    B7 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Field Engineer ")
    B8 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Sustaining Engineer ")
    B9 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="for every cost and timesaving innovation, patented inventions and creative work as well as discovery of educational,technical,scientific and/or cultural value", verbose_name="Question 6 ")
    B10 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as original author ")
    B11 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as co-author ")
    B12 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as reviewer ")
    B13 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as translator ")
    B14 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as editor ")
    B15 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as compiler ")
    B16 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="International ")
    B17 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="National/Regional ")
    B18 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="Local ")
    B19 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="For every Instructional Manual/Audio-Visual Materials ")
    B20 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    B21 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    B22 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every training course with a duration of at least (pro-rated for less than a year)", verbose_name="c.Local")
    B23 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    B24 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    B25 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For participation as a consultant, expert in any activity of an educational, technological, professional, scientific, or cultural nature (abroad and local) sponsored by the government or other agencies ", verbose_name="c.Local")
    B26 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    B27 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    B28 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For participation as coordinator,lecturer,resource person or guest speaker in conferences,workshops and/or training", verbose_name="c.Local")
    B29 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    B30 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    B31 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For official participation in conferences, seminar, workshops ", verbose_name="c.Local")
    B32 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For expert services as adviser in doctoral dissertation and masteral thesis and undergraduate thesis ", verbose_name="expert services")
    B33 = models.PositiveIntegerField(validators=[MaxValueValidator(10000)], default=0, help_text="1/120 hrs ", verbose_name="For certified training")
    B34 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="National", verbose_name="a.Offical ")
    B35 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Local", verbose_name="Local ")
    B36 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Member", verbose_name="b.Member ")
    B37 = models.CharField(choices=PROF_DEVAA, default='', max_length=5, verbose_name="For undergraduate academic honors earned:")
    B38 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive, International", verbose_name="Competitive, International ")
    B39 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, International", verbose_name="Non-Competitive, International ")
    B40 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive National/Regional", verbose_name="Competitive National/Regional ")
    B41 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, National/Regional", verbose_name="on-Competitive, National/Regional ")
    B42 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive, Local", verbose_name="Competitive, Local ")
    B43 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, Local", verbose_name="Non-Competitive, Local ")
    B44 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="International", verbose_name="a.International")
    B45 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="National/Regional", verbose_name="b.National/Regional")
    B46 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Local", verbose_name="c.Local")
    B47 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every year of participation in service-oriented project in the community", verbose_name="For every year of participation in service-oriented project in the community")
    B48 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="First Level", verbose_name="1.First Level ")
    B49 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Second Level", verbose_name="2.Second Level ")
    B50 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Others", verbose_name="3.Others ")
    Practical_Exam = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Practical exam ")
    Class_Demo = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Class demo ")
    Voice_speech = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Voice and Speech")
    Appearance = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Appearance")
    Alertness = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Alertness")
    Ability = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Ability to Present Ideas")
    Judgement = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Judgement")
    Emotional_stability = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Emotional Stability")
    Self_confidence = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Self-Confidence")
    total = models.PositiveIntegerField(blank=True, null=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', verbose_name='user ')

    @property
    def BB1(self):
        return self.B1

    @property
    def BB2(self):
        return self.B2 * .75

    @property
    def BB3(self):
        return self.B3 * 2

    @property
    def BB4(self):
        return self.B4 * 1.75

    @property
    def BB5(self):
        return self.B5 * 1.50

    @property
    def BB6(self):
        return self.B6 * 1.25

    @property
    def BB7(self):
        return self.B7 * 1

    @property
    def BB8(self):
        return self.B8 * .5

    @property
    def BB9(self):
        return self.B9 * 7

    @property
    def BB10(self):
        return self.B10 * 5

    @property
    def BB11(self):
        return self.B11 * 3

    @property
    def BB12(self):
        return self.B12 * 3

    @property
    def BB13(self):
        return self.B13 * 3

    @property
    def BB14(self):
        return self.B14 * 2

    @property
    def BB15(self):
        return self.B15 * 2

    @property
    def BB16(self):
        return self.B16 * 5

    @property
    def BB17(self):
        return self.B17 * 3

    @property
    def BB18(self):
        return self.B18 * 2

    @property
    def BB19(self):
        return self.B19 * 2

    @property
    def BB20(self):
        return self.B20 * 4

    @property
    def BB21(self):
        return self.B21 * 3

    @property
    def BB22(self):
        return self.B22 * 2

    @property
    def BB23(self):
        return self.B23 * 5

    @property
    def BB24(self):
        return self.B24 * 3

    @property
    def BB25(self):
        return self.B25 * 2

    @property
    def BB26(self):
        return self.B26 * 5

    @property
    def BB27(self):
        return self.B27 * 3

    @property
    def BB28(self):
        return self.B28 * 2

    @property
    def BB29(self):
        return self.B29 * 3

    @property
    def BB30(self):
        return self.B30 * 2

    @property
    def BB31(self):
        return self.B31 * 1

    @property
    def BB32(self):
        return self.B32 * 1

    @property
    def BB33(self):
        return self.B33 / 120

    @property
    def BB34(self):
        return self.B34 * 2

    @property
    def BB35(self):
        return self.B35 * 1.5

    @property
    def BB36(self):
        return self.B36 * 1

    @property
    def BB37(self):
        if self.B37 == '3':
            return 3
        elif self.B37 == '2':
            return 2
        elif self.B37 == '1':
            return 1
        elif self.B37 == '0.5':
            return 0.5
        else:
            return 0

    @property
    def BB38(self):
        return self.B38 * 5

    @property
    def BB39(self):
        return self.B39 * 3

    @property
    def BB40(self):
        return self.B40 * 3

    @property
    def BB41(self):
        return self.B41 * 2

    @property
    def BB42(self):
        return self.B42 * 1

    @property
    def BB43(self):
        return self.B43 * 1

    @property
    def BB44(self):
        return self.B44 * 5

    @property
    def BB45(self):
        return self.B45 * 3

    @property
    def BB46(self):
        return self.B46 * 2

    @property
    def BB47(self):
        return self.B47 * 1

    @property
    def BB48(self):
        return self.B48 * 1

    @property
    def BB49(self):
        return self.B49 * 2

    @property
    def BB50(self):
        return self.B50 * .5

    @property
    def exam(self):
        return self.Practical_Exam * .15

    @property
    def educ_qua(self):
        if self.Academic == '85':
            return round(self.doct, 3)
        elif self.Academic == '65':
            return round(self.mast, 3)
        else:
            return round(self.bach, 3)

    @property
    def Educ_Qual(self):
        if self.educ_qua > 34:
            return 85 * .40
        else:
            return self.educ_qua

    @property
    def deg(self):
        if self.Additional3 != 0 and self.Additional4 != 0:
            return ((self.Additional3 / 3) * 1) + ((self.Additional4 / 3) * .5)
        elif self.Additional3 != 0:
            return (self.Additional3 / 3) * 1
        elif self.Additional4 != 0:
            return (self.Additional4 / 3) * .5
        else:
            return 0

    @property
    def doct(self):
        if self.Academic == '85':
            return 85 * .40
        else:
            return 0

    @property
    def mast(self):
        if self.Academic == '65' and self.Special == 1 and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((69 + 25 + self.deg + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((69 + self.deg + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional2 and self.deg != 0:
            return round((69 + 25 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 and self.deg != 0:
            return round((69 + 25 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 == 1 and self.Additional2:
            return round((69 + 25 + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional1 == 1 and self.Additional2:
            return round((69 + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.deg != 0:
            return round((69 + 25 + self.deg) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional2:
            return round((69 + 25 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 == 1:
            return round((69 + 25 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg == 1 and self.Additional1 == 1:
            return round((69 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg == 1 and self.Additional1 == 1:
            return round((69 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg != 0:
            return round((69 + self.deg) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional2 == 1:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 + .40
        elif self.Academic == '65' and self.Additional1 == 2:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65':
            return round(69 * .40, 3)
        else:
            return 0

    @property
    def bach(self):
        if self.Academic == '45' and self.Special == 1 and self.Additional1 == 1 and self.Additional2 == 1 and self.deg != 0:
            return round((45 + 25 + self.deg + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((45 + self.deg + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional2 and self.deg != 0:
            return round((45 + 25 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 and self.deg != 0:
            return round((45 + 25 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 == 1 and self.Additional2:
            return round((45 + 25 + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 1 and self.Additional2:
            return round((45 + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.deg != 0:
            return round((45 + 25 + self.deg) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional2:
            return round((45 + 25 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 == 1:
            return round((45 + 25 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg == 1 and self.Additional1 == 1:
            return round((45 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg == 1 and self.Additional1 == 1:
            return round((45 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg != 0:
            return round((45 + self.deg) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional2 == 1:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 2:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45':
            return round(45 * .40, 3)
        else:
            return 0

    @property
    def subtot2(self):
        return self.BB1 + self.BB2 + self.BB3 + self.BB4 + self.BB5 + self.BB6 + self.BB7 + self.BB8

    @property
    def Acad_Exp(self):
        if self.subtot2 > 25:
            return round(25 * .15, 3)
        else:
            return round(self.subtot2 * .15, 3)

    @property
    def subtot3(self):
        return self.BB9 + self.BB10 + self.BB11 + self.BB12 + self.BB13 + self.BB14 + self.BB15 + self.BB16 + self.BB17 + self.BB18 + self.BB19 + self.BB20 + self.BB21 + self.BB22 + self.BB23 + self.BB24 + self.BB25 + self.BB26 + self.BB27 + self.BB28 + self.BB29 + self.BB30 + self.BB31 + self.BB32 + self.BB33 + self.BB34 + self.BB35 + self.BB36 + self.BB38 + self.BB39 + self.BB40 + self.BB41 + self.BB42 + self.BB43 + self.BB44 + self.BB45 + self.BB46 + self.BB47 + self.BB48 + self.BB49 + self.BB50 + self.BB37

    @property
    def Prof_Devt(self):
        if self.subtot3 > 45:
            return round(45 * .10, 3)
        else:
            return round(self.subtot3 * .10, 3)

    @property
    def Demo(self):
        return round(self.Class_Demo * .10, 1)

    @property
    def totalin(self):
        return self.Voice_speech + self.Appearance + self.Alertness + self.Ability + self.Judgement + self.Emotional_stability + self.Self_confidence

    @property
    def Interview(self):
        if self.totalin < 7:
            return 0
        else:
            return round(((self.totalin + 65) * .10), 1)

    @property
    def get_totals(self):
        if self.Academic == '85':
            return round((self.doct + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
        elif self.Academic == '65':
            if self.mast < 40:
                return round((self.mast + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
            else:
                return round((40 + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
        elif self.Academic == '45':
            if self.mast < 40:
                return round((self.bach + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
            else:
                return round((40 + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)

    def save(self, *args, **kwargs):
        self.total = self.get_totals
        super(Civil_Engr, self).save(*args, **kwargs)

    @property
    def rank(self):
        aggregate = Civil_Engr.objects.filter(total__gt=self.total).aggregate(ranking=Count('total'))
        return aggregate['ranking'] + 1

    @property
    def remarks(self):
        if self.Academic == '85' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET and lack in minimum average qualification requirements')
            else:
                return('Not yet qualified lack in minimum average qualification requirements')
        elif self.Academic == '85' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit')
            else:
                return('Qualified but exceed in age limit')
        elif self.Academic == '85' and self.Age > 45 and self.total < 60:
                return('Not qualified exceed in age limit')
        elif self.Academic == '85' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET')
            else:
                return('Qualified')
        elif self.Academic == '65' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET, lack in minimum average qualification requirements')
            else:
                return('Not yet qualified lack in minimum average qualification requirements')
        elif self.Academic == '65' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit')
            else:
                return('Qualified but exceed in age limit')
        elif self.Academic == '65' and self.Age > 45 and self.total < 60:
                return('Not qualified exceed in age limit')
        elif self.Academic == '65' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET')
            else:
                return('Qualified')
        elif self.Academic == '45' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET, Masters degree needed, lack in minimum average qualification requirements')
            else:
                return('Not yet qualified masters degree needed, lack in minimum average qualification requirements')
        elif self.Academic == '45' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit, no LET & masters degree needed')
            else:
                return('Not qualified masters degree needed & exceed in age limit')
        elif self.Academic == '45' and self.Age > 45 and self.total < 60:
                return('Not qualified masters degree needed & exceed in age limit')
        elif self.Academic == '45' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET & masters degree needed')
            else:
                return('Not yet qualified masters degree needed')


class Mechanical_Engr(models.Model):
    class Meta:
        verbose_name = "Instructor I - Mechanical Engineering"
        verbose_name_plural = "Instructor I - Mechanical Engineering"
    fname = models.CharField(max_length=100, verbose_name="First name ")
    mname = models.CharField(max_length=100, verbose_name="Middle name ")
    lname = models.CharField(max_length=100, verbose_name="Last name ")
    address = models.CharField(max_length=100, verbose_name="Adress ", help_text="zone/street/barangay/province or city/house no.")
    phone_number = models.CharField(max_length=11, verbose_name="Phone Number ")
    Age = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Age ")
    License = models.BooleanField(verbose_name="LET ")
    Civil_Status = models.CharField(max_length=7, choices=CIVIL_STATUS, verbose_name="Civil Status", default=" ")
    Eligibility = models.CharField(max_length=100, choices=ELIGIBILITY_MECHANICAL, verbose_name="Eligibility", default=" ")
    date_recorded = models.DateTimeField(default=timezone.now, editable=False)
    Academic = models.CharField(max_length=4, verbose_name="Educational Qualification ", choices=STATUS_ACADEMIC, default='', help_text='Highest academic degree or educational attainment in the field of study')
    Special = models.BooleanField(verbose_name='Special Course ', help_text='e.g. Technical/Technician')
    Additional1 = models.BooleanField(help_text="Graduate of five-year Engineering Degree", verbose_name="additional 5 points")
    Additional2 = models.BooleanField(help_text="Licensure Exam", verbose_name="additional 5 points")
    Degree = models.CharField(max_length=3, verbose_name="Question 1 ", choices=STATUS_ADDITIONAL, default='', help_text="Additional Equivalent degree earned, related to the present position")
    Additional3 = models.PositiveIntegerField(validators=[MaxValueValidator(50)], default=0, help_text="For every 3 credits earned toward a higher approved degree course", verbose_name="Question 2 ")
    Additional4 = models.PositiveIntegerField(validators=[MaxValueValidator(50)], default=0, help_text="For every 3 credits earned on the same level", verbose_name="Question 3 ")
    C1 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every full year-time academic service in a state institution of higher learning", verbose_name="Question 4 ")
    C2 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every full year-time academic service in any public or private educational institution other than SUC", verbose_name="Question 5 ")
    C3 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Plant Engineer ")
    C4 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Supervising Engineer ")
    C5 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Production Engineer ")
    C6 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Maintenance Engineer ")

    C7 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="for every cost and timesaving innovation, patented inventions and creative work as well as discovery of educational,technical,scientific and/or cultural value", verbose_name="Question 6 ")
    C8 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as original author ")
    C9 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as co-author ")
    C10 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as reviewer ")
    C11 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as translator ")
    C12 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as editor ")
    C13 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as compiler ")
    C14 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="International ")
    C15 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="National/Regional ")
    C16 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="Local ")
    C17 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="For every Instructional Manual/Audio-Visual Materials ")
    C18 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    C19 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    C20 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every training course with a duration of at least (pro-rated for less than a year)", verbose_name="c.Local")
    C21 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    C22 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    C23 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For participation as a consultant, expert in any activity of an educational, technological, professional, scientific, or cultural nature (abroad and local) sponsored by the government or other agencies ", verbose_name="c.Local")
    C24 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    C25 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    C26 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For participation as coordinator,lecturer,resource person or guest speaker in conferences,workshops and/or training", verbose_name="c.Local")
    C27 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    C28 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    C29 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For official participation in conferences, seminar, workshops ", verbose_name="c.Local")
    C30 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For expert services as adviser in doctoral dissertation and masteral thesis and undergraduate thesis ", verbose_name="expert services")
    C31 = models.PositiveIntegerField(validators=[MaxValueValidator(10000)], default=0, help_text="1/120 hrs ", verbose_name="For certified training")
    C32 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="National", verbose_name="a.Offical ")
    C33 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Local", verbose_name="Local ")
    C34 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Member", verbose_name="b.Member ")
    C35 = models.CharField(choices=PROF_DEVAA, default='', max_length=5, verbose_name="For undergraduate academic honors earned:")
    C36 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive, International", verbose_name="Competitive, International ")
    C37 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, International", verbose_name="Non-Competitive, International ")
    C38 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive National/Regional", verbose_name="Competitive National/Regional ")
    C39 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, National/Regional", verbose_name="on-Competitive, National/Regional ")
    C40 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive, Local", verbose_name="Competitive, Local ")
    C41 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, Local", verbose_name="Non-Competitive, Local ")
    C42 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="International", verbose_name="a.International")
    C43 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="National/Regional", verbose_name="b.National/Regional")
    C44 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Local", verbose_name="c.Local")
    C45 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every year of participation in service-oriented project in the community", verbose_name="For every year of participation in service-oriented project in the community")
    C46 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="First Level", verbose_name="1.First Level ")
    C47 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Second Level", verbose_name="2.Second Level ")
    C48 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Others", verbose_name="3.Others ")
    Practical_Exam = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Practical exam ")
    Class_Demo = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Class demo ")
    Voice_speech = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Voice and Speech")
    Appearance = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Appearance")
    Alertness = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Alertness")
    Ability = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Ability to Present Ideas")
    Judgement = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Judgement")
    Emotional_stability = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Emotional Stability")
    Self_confidence = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Self-Confidence")
    total = models.PositiveIntegerField(blank=True, null=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', verbose_name='user ')

    @property
    def CC1(self):
        return self.C1

    @property
    def CC2(self):
        return self.C2 * .75

    @property
    def CC3(self):
        return self.C3 * 2

    @property
    def CC4(self):
        return self.C4 * 1.75

    @property
    def CC5(self):
        return self.C5 * 1.50

    @property
    def CC6(self):
        return self.C6 * 1

    @property
    def CC7(self):
        return self.C7 * 7

    @property
    def CC8(self):
        return self.C8 * 5

    @property
    def CC9(self):
        return self.C9 * 3

    @property
    def CC10(self):
        return self.C10 * 3

    @property
    def CC11(self):
        return self.C11 * 3

    @property
    def CC12(self):
        return self.C12 * 2

    @property
    def CC13(self):
        return self.C13 * 2

    @property
    def CC14(self):
        return self.C14 * 5

    @property
    def CC15(self):
        return self.C15 * 3

    @property
    def CC16(self):
        return self.C16 * 2

    @property
    def CC17(self):
        return self.C17 * 2

    @property
    def CC18(self):
        return self.C18 * 4

    @property
    def CC19(self):
        return self.C19 * 3

    @property
    def CC20(self):
        return self.C20 * 2

    @property
    def CC21(self):
        return self.C21 * 5

    @property
    def CC22(self):
        return self.C22 * 3

    @property
    def CC23(self):
        return self.C23 * 2

    @property
    def CC24(self):
        return self.C24 * 5

    @property
    def CC25(self):
        return self.C25 * 3

    @property
    def CC26(self):
        return self.C26 * 2

    @property
    def CC27(self):
        return self.C27 * 3

    @property
    def CC28(self):
        return self.C28 * 2

    @property
    def CC29(self):
        return self.C30 * 1

    @property
    def CC30(self):
        return self.C30 * 1

    @property
    def CC31(self):
        return self.C31 / 120

    @property
    def CC32(self):
        return self.C32 * 2

    @property
    def CC33(self):
        return self.C33 * 1.5

    @property
    def CC34(self):
        return self.C34 * 1

    @property
    def CC35(self):
        if self.C35 == '3':
            return 3
        elif self.C35 == '2':
            return 2
        elif self.C35 == '1':
            return 1
        elif self.C35 == '0.5':
            return 0.5
        else:
            return 0

    @property
    def CC36(self):
        return self.C36 * 5

    @property
    def CC37(self):
        return self.C37 * 3

    @property
    def CC38(self):
        return self.C38 * 3

    @property
    def CC39(self):
        return self.C39 * 2

    @property
    def CC40(self):
        return self.C40 * 1

    @property
    def CC41(self):
        return self.C41 * 1

    @property
    def CC42(self):
        return self.C42 * 5

    @property
    def CC43(self):
        return self.C43 * 3

    @property
    def CC44(self):
        return self.C44 * 2

    @property
    def CC45(self):
        return self.C45 * 1

    @property
    def CC46(self):
        return self.C46 * 1

    @property
    def CC47(self):
        return self.C47 * 2

    @property
    def CC48(self):
        return self.C48 * .5

    @property
    def exam(self):
        return self.Practical_Exam * .15

    @property
    def educ_qua(self):
        if self.Academic == '85':
            return round(self.doct, 3)
        elif self.Academic == '65':
            return round(self.mast, 3)
        else:
            return round(self.bach, 3)

    @property
    def Educ_Qual(self):
        if self.educ_qua > 34:
            return 85 * .40
        else:
            return self.educ_qua

    @property
    def deg(self):
        if self.Additional3 != 0 and self.Additional4 != 0:
            return ((self.Additional3 / 3) * 1) + ((self.Additional4 / 3) * .5)
        elif self.Additional3 != 0:
            return (self.Additional3 / 3) * 1
        elif self.Additional4 != 0:
            return (self.Additional4 / 3) * .5
        else:
            return 0

    @property
    def doct(self):
        if self.Academic == '85':
            return 85 * .40
        else:
            return 0

    @property
    def mast(self):
        if self.Academic == '65' and self.Special == 1 and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((69 + 25 + self.deg + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((69 + self.deg + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional2 and self.deg != 0:
            return round((69 + 25 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 and self.deg != 0:
            return round((69 + 25 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 == 1 and self.Additional2:
            return round((69 + 25 + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional1 == 1 and self.Additional2:
            return round((69 + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.deg != 0:
            return round((69 + 25 + self.deg) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional2:
            return round((69 + 25 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 == 1:
            return round((69 + 25 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg == 1 and self.Additional1 == 1:
            return round((69 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg == 1 and self.Additional1 == 1:
            return round((69 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg != 0:
            return round((69 + self.deg) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional2 == 1:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 + .40
        elif self.Academic == '65' and self.Additional1 == 2:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65':
            return round(69 * .40, 3)
        else:
            return 0

    @property
    def bach(self):
        if self.Academic == '45' and self.Special == 1 and self.Additional1 == 1 and self.Additional2 == 1 and self.deg != 0:
            return round((45 + 25 + self.deg + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((45 + self.deg + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional2 and self.deg != 0:
            return round((45 + 25 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 and self.deg != 0:
            return round((45 + 25 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 == 1 and self.Additional2:
            return round((45 + 25 + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 1 and self.Additional2:
            return round((45 + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.deg != 0:
            return round((45 + 25 + self.deg) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional2:
            return round((45 + 25 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 == 1:
            return round((45 + 25 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg == 1 and self.Additional1 == 1:
            return round((45 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg == 1 and self.Additional1 == 1:
            return round((45 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg != 0:
            return round((45 + self.deg) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional2 == 1:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 2:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45':
            return round(45 * .40, 3)
        else:
            return 0

    @property
    def subtot2(self):
        return self.CC1 + self.CC2 + self.CC3 + self.CC4 + self.CC5 + self.CC6

    @property
    def Acad_Exp(self):
        if self.subtot2 > 25:
            return round(25 * .15, 3)
        else:
            return round(self.subtot2 * .15, 3)

    @property
    def subtot3(self):
        return self.CC7 + self.CC8 + self.CC9 + self.CC10 + self.CC11 + self.CC12 + self.CC13 + self.CC14 + self.CC15 + self.CC16 + self.CC17 + self.CC18 + self.CC19 + self.CC20 + self.CC21 + self.CC22 + self.CC23 + self.CC24 + self.CC25 + self.CC26 + self.CC27 + self.CC28 + self.CC29 + self.CC30 + self.CC31 + self.CC32 + self.CC33 + self.CC34 + self.CC36 + self.CC37 + self.CC38 + self.CC39 + self.CC40 + self.CC41 + self.CC42 + self.CC43 + self.CC44 + self.CC45 + self.CC46 + self.CC47 + self.CC48 + self.CC35

    @property
    def Prof_Devt(self):
        if self.subtot3 > 45:
            return round(45 * .10, 3)
        else:
            return round(self.subtot3 * .10, 3)

    @property
    def Demo(self):
        return round(self.Class_Demo * .10, 1)

    @property
    def totalin(self):
        return self.Voice_speech + self.Appearance + self.Alertness + self.Ability + self.Judgement + self.Emotional_stability + self.Self_confidence

    @property
    def Interview(self):
        if self.totalin < 7:
            return 0
        else:
            return round(((self.totalin + 65) * .10), 1)

    @property
    def get_totals(self):
        if self.Academic == '85':
            return round((self.doct + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
        elif self.Academic == '65':
            if self.mast < 40:
                return round((self.mast + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
            else:
                return round((40 + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
        elif self.Academic == '45':
            if self.mast < 40:
                return round((self.bach + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
            else:
                return round((40 + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)

    def save(self, *args, **kwargs):
        self.total = self.get_totals
        super(Mechanical_Engr, self).save(*args, **kwargs)

    @property
    def rank(self):
        aggregate = Mechanical_Engr.objects.filter(total__gt=self.total).aggregate(ranking=Count('total'))
        return aggregate['ranking'] + 1

    @property
    def remarks(self):
        if self.Academic == '85' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET and lack in minimum average qualification requirements')
            else:
                return('Not yet qualified lack in minimum average qualification requirements')
        elif self.Academic == '85' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit')
            else:
                return('Qualified but exceed in age limit')
        elif self.Academic == '85' and self.Age > 45 and self.total < 60:
                return('Not qualified exceed in age limit')
        elif self.Academic == '85' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET')
            else:
                return('Qualified')
        elif self.Academic == '65' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET, lack in minimum average qualification requirements')
            else:
                return('Not yet qualified lack in minimum average qualification requirements')
        elif self.Academic == '65' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit')
            else:
                return('Qualified but exceed in age limit')
        elif self.Academic == '65' and self.Age > 45 and self.total < 60:
                return('Not qualified exceed in age limit')
        elif self.Academic == '65' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET')
            else:
                return('Qualified')
        elif self.Academic == '45' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET, Masters degree needed, lack in minimum average qualification requirements')
            else:
                return('Not yet qualified masters degree needed, lack in minimum average qualification requirements')
        elif self.Academic == '45' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit, no LET & masters degree needed')
            else:
                return('Not qualified masters degree needed & exceed in age limit')
        elif self.Academic == '45' and self.Age > 45 and self.total < 60:
                return('Not qualified masters degree needed & exceed in age limit')
        elif self.Academic == '45' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET & masters degree needed')
            else:
                return('Not yet qualified masters degree needed')


class Electronics_Engr(models.Model):
    class Meta:
        verbose_name = "Instructor I - Electronics Communication Engineering"
        verbose_name_plural = "Instructor I - Electronics Communication Engineering"
    fname = models.CharField(max_length=100, verbose_name="First name ")
    mname = models.CharField(max_length=100, verbose_name="Middle name ")
    lname = models.CharField(max_length=100, verbose_name="Last name ")
    address = models.CharField(max_length=100, verbose_name="Adress ", help_text="zone/street/barangay/province or city/house no.")
    phone_number = models.CharField(max_length=11, verbose_name="Phone Number ")
    Age = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Age ")
    License = models.BooleanField(verbose_name="LET ")
    Civil_Status = models.CharField(max_length=7, choices=CIVIL_STATUS, verbose_name="Civil Status", default=" ")
    Eligibility = models.CharField(max_length=100, choices=ELIGIBILITY_ELECTRICAL, verbose_name="Eligibility", default=" ")
    date_recorded = models.DateTimeField(default=timezone.now, editable=False)
    Academic = models.CharField(max_length=4, verbose_name="Educational Qualification ", choices=STATUS_ACADEMIC, default='', help_text='Highest academic degree or educational attainment in the field of study')
    Special = models.BooleanField(verbose_name='Special Course ', help_text='e.g. Technical/Technician')
    Additional1 = models.BooleanField(help_text="Graduate of five-year Engineering Degree", verbose_name="additional 5 points")
    Additional2 = models.BooleanField(help_text="Licensure Exam", verbose_name="additional 5 points")
    Degree = models.CharField(max_length=3, verbose_name="Question 1 ", choices=STATUS_ADDITIONAL, default='', help_text="Additional Equivalent degree earned, related to the present position")
    Additional3 = models.PositiveIntegerField(validators=[MaxValueValidator(50)], default=0, help_text="For every 3 credits earned toward a higher approved degree course", verbose_name="Question 2 ")
    Additional4 = models.PositiveIntegerField(validators=[MaxValueValidator(50)], default=0, help_text="For every 3 credits earned on the same level", verbose_name="Question 3 ")

    D1 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every full year-time academic service in a state institution of higher learning", verbose_name="Question 4 ")
    D2 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every full year-time academic service in any public or private educational institution other than SUC", verbose_name="Question 5 ")
    D3 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Project Engineer ")
    D4 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Supervising Engineer ")
    D5 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Senior Electronics Engineer ")
    D6 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Junior Electronics Engineer ")
    D7 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Electronics Technician ")
    D8 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="for every cost and timesaving innovation, patented inventions and creative work as well as discovery of educational,technical,scientific and/or cultural value", verbose_name="Question 6 ")
    D9 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as original author ")
    D10 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as co-author ")
    D11 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as reviewer ")
    D12 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as translator ")
    D13 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as editor ")
    D14 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as compiler ")
    D15 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="International ")
    D16 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="National/Regional ")
    D17 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="Local ")
    D18 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="For every Instructional Manual/Audio-Visual Materials ")
    D19 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    D20 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    D21 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every training course with a duration of at least (pro-rated for less than a year)", verbose_name="c.Local")
    D22 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    D23 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    D24 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For participation as a consultant, expert in any activity of an educational, technological, professional, scientific, or cultural nature (abroad and local) sponsored by the government or other agencies ", verbose_name="c.Local")
    D25 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    D26 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    D27 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For participation as coordinator,lecturer,resource person or guest speaker in conferences,workshops and/or training", verbose_name="c.Local")
    D28 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    D29 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    D30 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For official participation in conferences, seminar, workshops ", verbose_name="c.Local")
    D31 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For expert services as adviser in doctoral dissertation and masteral thesis and undergraduate thesis ", verbose_name="expert services")
    D32 = models.PositiveIntegerField(validators=[MaxValueValidator(10000)], default=0, help_text="1/120 hrs ", verbose_name="For certified training")
    D33 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="National", verbose_name="a.Offical ")
    D34 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Local", verbose_name="Local ")
    D35 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Member", verbose_name="b.Member ")
    D36 = models.CharField(choices=PROF_DEVAA, default='', max_length=5, verbose_name="For undergraduate academic honors earned:")
    D37 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive, International", verbose_name="Competitive, International ")
    D38 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, International", verbose_name="Non-Competitive, International ")
    D39 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive National/Regional", verbose_name="Competitive National/Regional ")
    D40 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, National/Regional", verbose_name="on-Competitive, National/Regional ")
    D41 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive, Local", verbose_name="Competitive, Local ")
    D42 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, Local", verbose_name="Non-Competitive, Local ")
    D43 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="International", verbose_name="a.International")
    D44 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="National/Regional", verbose_name="b.National/Regional")
    D45 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Local", verbose_name="c.Local")
    D46 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every year of participation in service-oriented project in the community", verbose_name="For every year of participation in service-oriented project in the community")
    D47 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="First Level", verbose_name="1.First Level ")
    D48 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Second Level", verbose_name="2.Second Level ")
    D49 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Others", verbose_name="3.Others ")
    Practical_Exam = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Practical exam ")
    Class_Demo = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Class demo ")
    Voice_speech = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Voice and Speech")
    Appearance = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Appearance")
    Alertness = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Alertness")
    Ability = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Ability to Present Ideas")
    Judgement = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Judgement")
    Emotional_stability = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Emotional Stability")
    Self_confidence = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Self-Confidence")
    total = models.PositiveIntegerField(blank=True, null=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', verbose_name='user ')

    @property
    def DD1(self):
        return self.D1

    @property
    def DD2(self):
        return self.D2 * .75

    @property
    def DD3(self):
        return self.D3 * 2

    @property
    def DD4(self):
        return self.D4 * 1.75

    @property
    def DD5(self):
        return self.D5 * 1.50

    @property
    def DD6(self):
        return self.D6 * 1.25

    @property
    def DD7(self):
        return self.D7 * 1

    @property
    def DD8(self):
        return self.D8 * 7

    @property
    def DD9(self):
        return self.D9 * 5

    @property
    def DD10(self):
        return self.D10 * 3

    @property
    def DD11(self):
        return self.D11 * 3

    @property
    def DD12(self):
        return self.D12 * 3

    @property
    def DD13(self):
        return self.D13 * 2

    @property
    def DD14(self):
        return self.D14 * 2

    @property
    def DD15(self):
        return self.D15 * 5

    @property
    def DD16(self):
        return self.D16 * 3

    @property
    def DD17(self):
        return self.D17 * 2

    @property
    def DD18(self):
        return self.D18 * 2

    @property
    def DD19(self):
        return self.D19 * 4

    @property
    def DD20(self):
        return self.D20 * 3

    @property
    def DD21(self):
        return self.D21 * 2

    @property
    def DD22(self):
        return self.D22 * 5

    @property
    def DD23(self):
        return self.D23 * 3

    @property
    def DD24(self):
        return self.D24 * 2

    @property
    def DD25(self):
        return self.D25 * 5

    @property
    def DD26(self):
        return self.D26 * 3

    @property
    def DD27(self):
        return self.D27 * 2

    @property
    def DD28(self):
        return self.D28 * 3

    @property
    def DD29(self):
        return self.D29 * 2

    @property
    def DD30(self):
        return self.D30 * 1

    @property
    def DD31(self):
        return self.D31 * 1

    @property
    def DD32(self):
        return self.D32 / 120

    @property
    def DD33(self):
        return self.D33 * 2

    @property
    def DD34(self):
        return self.D34 * 1.5

    @property
    def DD35(self):
        return self.D35 * 1

    @property
    def DD36(self):
        if self.D36 == '3':
            return 3
        elif self.D36 == '2':
            return 2
        elif self.D36 == '1':
            return 1
        elif self.D36 == '0.5':
            return 0.5
        else:
            return 0

    @property
    def DD37(self):
        return self.D37 * 5

    @property
    def DD38(self):
        return self.D38 * 3

    @property
    def DD39(self):
        return self.D39 * 3

    @property
    def DD40(self):
        return self.D40 * 2

    @property
    def DD41(self):
        return self.D41 * 1

    @property
    def DD42(self):
        return self.D42 * 1

    @property
    def DD43(self):
        return self.D43 * 5

    @property
    def DD44(self):
        return self.D44 * 3

    @property
    def DD45(self):
        return self.D45 * 2

    @property
    def DD46(self):
        return self.D46 * 1

    @property
    def DD47(self):
        return self.D47 * 1

    @property
    def DD48(self):
        return self.D48 * 2

    @property
    def DD49(self):
        return self.D49 * .5

    @property
    def exam(self):
        return round(self.Practical_Exam * .15, 3)

    @property
    def educ_qua(self):
        if self.Academic == '85':
            return round(self.doct, 3)
        elif self.Academic == '65':
            return round(self.mast, 3)
        else:
            return round(self.bach, 3)

    @property
    def Educ_Qual(self):
        if self.educ_qua > 34:
            return 85 * .40
        else:
            return self.educ_qua

    @property
    def deg(self):
        if self.Additional3 != 0 and self.Additional4 != 0:
            return ((self.Additional3 / 3) * 1) + ((self.Additional4 / 3) * .5)
        elif self.Additional3 != 0:
            return (self.Additional3 / 3) * 1
        elif self.Additional4 != 0:
            return (self.Additional4 / 3) * .5
        else:
            return 0

    @property
    def doct(self):
        if self.Academic == '85':
            return 85 * .40
        else:
            return 0

    @property
    def mast(self):
        if self.Academic == '65' and self.Special == 1 and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((69 + 25 + self.deg + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((69 + self.deg + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional2 and self.deg != 0:
            return round((69 + 25 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 and self.deg != 0:
            return round((69 + 25 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 == 1 and self.Additional2:
            return round((69 + 25 + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional1 == 1 and self.Additional2:
            return round((69 + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.deg != 0:
            return round((69 + 25 + self.deg) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional2:
            return round((69 + 25 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 == 1:
            return round((69 + 25 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg == 1 and self.Additional1 == 1:
            return round((69 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg == 1 and self.Additional1 == 1:
            return round((69 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg != 0:
            return round((69 + self.deg) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional2 == 1:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 + .40
        elif self.Academic == '65' and self.Additional1 == 2:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65':
            return round(65 * .40, 3)
        else:
            return 0

    @property
    def bach(self):
        if self.Academic == '45' and self.Special == 1 and self.Additional1 == 1 and self.Additional2 == 1 and self.deg != 0:
            return round((45 + 25 + self.deg + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((45 + self.deg + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional2 and self.deg != 0:
            return round((45 + 25 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 and self.deg != 0:
            return round((45 + 25 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 == 1 and self.Additional2:
            return round((45 + 25 + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 1 and self.Additional2:
            return round((45 + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.deg != 0:
            return round((45 + 25 + self.deg) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional2:
            return round((45 + 25 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 == 1:
            return round((45 + 25 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg == 1 and self.Additional1 == 1:
            return round((45 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg == 1 and self.Additional1 == 1:
            return round((45 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg != 0:
            return round((45 + self.deg) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional2 == 1:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 2:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45':
            return round(45 * .40, 3)
        else:
            return 0

    @property
    def subtot2(self):
        return self.DD1 + self.DD2 + self.DD3 + self.DD4 + self.DD5 + self.DD6 + self.DD7

    @property
    def Acad_Exp(self):
        if self.subtot2 > 25:
            return round(25 * .15, 3)
        else:
            return round(self.subtot2 * .15, 3)

    @property
    def subtot3(self):
        return self.DD8 + self.DD9 + self.DD10 + self.DD11 + self.DD12 + self.DD13 + self.DD14 + self.DD15 + self.DD16 + self.DD17 + self.DD18 + self.DD19 + self.DD20 + self.DD21 + self.DD22 + self.DD23 + self.DD24 + self.DD25 + self.DD26 + self.DD27 + self.DD28 + self.DD29 + self.DD30 + self.DD31 + self.DD32 + self.DD33 + self.DD34 + self.DD35 + self.DD37 + self.DD38 + self.DD39 + self.DD40 + self.DD41 + self.DD42 + self.DD43 + self.DD44 + self.DD45 + self.DD46 + self.DD47 + self.DD48 + self.DD49 + self.DD36

    @property
    def Prof_Devt(self):
        if self.subtot3 > 45:
            return round(45 * .10, 3)
        else:
            return round(self.subtot3 * .10, 3)

    @property
    def Demo(self):
        return round(self.Class_Demo * .10, 1)

    @property
    def totalin(self):
        return self.Voice_speech + self.Appearance + self.Alertness + self.Ability + self.Judgement + self.Emotional_stability + self.Self_confidence

    @property
    def Interview(self):
        if self.totalin < 7:
            return 0
        else:
            return round(((self.totalin + 65) * .10), 3)

    @property
    def get_totals(self):
        if self.Academic == '85':
            return round((self.doct + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
        elif self.Academic == '65':
            if self.mast < 40:
                return round((self.mast + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
            else:
                return round((40 + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
        elif self.Academic == '45':
            if self.mast < 40:
                return round((self.bach + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
            else:
                return round((40 + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)

    def save(self, *args, **kwargs):
        self.total = self.get_totals
        super(Electronics_Engr, self).save(*args, **kwargs)

    @property
    def rank(self):
        aggregate = Electronics_Engr.objects.filter(total__gt=self.total).aggregate(ranking=Count('total'))
        return aggregate['ranking'] + 1

    @property
    def remarks(self):
        if self.Academic == '85' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET and lack in minimum average qualification requirements')
            else:
                return('Not yet qualified lack in minimum average qualification requirements')
        elif self.Academic == '85' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit')
            else:
                return('Qualified but exceed in age limit')
        elif self.Academic == '85' and self.Age > 45 and self.total < 60:
                return('Not qualified exceed in age limit')
        elif self.Academic == '85' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET')
            else:
                return('Qualified')
        elif self.Academic == '65' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET, lack in minimum average qualification requirements')
            else:
                return('Not yet qualified lack in minimum average qualification requirements')
        elif self.Academic == '65' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit')
            else:
                return('Qualified but exceed in age limit')
        elif self.Academic == '65' and self.Age > 45 and self.total < 60:
                return('Not qualified exceed in age limit')
        elif self.Academic == '65' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET')
            else:
                return('Qualified')
        elif self.Academic == '45' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET, Masters degree needed, lack in minimum average qualification requirements')
            else:
                return('Not yet qualified masters degree needed, lack in minimum average qualification requirements')
        elif self.Academic == '45' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit, no LET & masters degree needed')
            else:
                return('Not qualified masters degree needed & exceed in age limit')
        elif self.Academic == '45' and self.Age > 45 and self.total < 60:
                return('Not qualified masters degree needed & exceed in age limit')
        elif self.Academic == '45' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET & masters degree needed')
            else:
                return('Not yet qualified masters degree needed')


class Architect(models.Model):
    class Meta:
        verbose_name_plural = "Instructor I - Architect/Draffting Instructor"
    fname = models.CharField(max_length=100, verbose_name="First name ")
    mname = models.CharField(max_length=100, verbose_name="Middle name ")
    lname = models.CharField(max_length=100, verbose_name="Last name ")
    address = models.CharField(max_length=100, verbose_name="Adress ", help_text="zone/street/barangay/province or city/house no.")
    phone_number = models.CharField(max_length=11, verbose_name="Phone Number ")
    Age = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Age ")
    License = models.BooleanField(verbose_name="LET ")
    Civil_Status = models.CharField(max_length=7, choices=CIVIL_STATUS, verbose_name="Civil Status", default=" ")
    Eligibility = models.CharField(max_length=100, choices=ELIGIBILITY_ARCHITECT, verbose_name="Eligibility", default=" ")
    date_recorded = models.DateTimeField(default=timezone.now, editable=False)
    Academic = models.CharField(max_length=4, verbose_name="Educational Qualification ", choices=STATUS_ACADEMIC, default='', help_text='Highest academic degree or educational attainment in the field of study')
    Special = models.BooleanField(verbose_name='Special Course ', help_text='e.g. Technical/Technician')
    Additional1 = models.BooleanField(help_text="Graduate of five-year Engineering Degree", verbose_name="additional 5 points")
    Additional2 = models.BooleanField(help_text="Licensure Exam", verbose_name="additional 5 points")
    Degree = models.CharField(max_length=3, verbose_name="Question 1 ", choices=STATUS_ADDITIONAL, default='', help_text="Additional Equivalent degree earned, related to the present position")
    Additional3 = models.PositiveIntegerField(validators=[MaxValueValidator(50)], default=0, help_text="For every 3 credits earned toward a higher approved degree course", verbose_name="Question 2 ")
    Additional4 = models.PositiveIntegerField(validators=[MaxValueValidator(50)], default=0, help_text="For every 3 credits earned on the same level", verbose_name="Question 3 ")

    E1 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every full year-time academic service in a state institution of higher learning", verbose_name="Question 4 ")
    E2 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every full year-time academic service in any public or private educational institution other than SUC", verbose_name="Question 5 ")
    E3 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Project Engineer ")
    E4 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Architectural/Interior Design ")
    E5 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Supervising Draftsman/Architect ")
    E6 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="General Draftsman ")
    E7 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Draftsman ")
    E8 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="for every cost and timesaving innovation, patented inventions and creative work as well as discovery of educational,technical,scientific and/or cultural value", verbose_name="Question 6 ")
    E9 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as original author ")
    E10 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as co-author ")
    E11 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as reviewer ")
    E12 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as translator ")
    E13 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as editor ")
    E14 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as compiler ")
    E15 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="International ")
    E16 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="National/Regional ")
    E17 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="Local ")
    E18 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="For every Instructional Manual/Audio-Visual Materials ")
    E19 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    E20 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    E21 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every training course with a duration of at least (pro-rated for less than a year)", verbose_name="c.Local")
    E22 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    E23 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    E24 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For participation as a consultant, expert in any activity of an educational, technological, professional, scientific, or cultural nature (abroad and local) sponsored by the government or other agencies ", verbose_name="c.Local")
    E25 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    E26 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    E27 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For participation as coordinator,lecturer,resource person or guest speaker in conferences,workshops and/or training", verbose_name="c.Local")
    E28 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    E29 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    E30 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For official participation in conferences, seminar, workshops ", verbose_name="c.Local")
    E31 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For expert services as adviser in doctoral dissertation and masteral thesis and undergraduate thesis ", verbose_name="expert services")
    E32 = models.PositiveIntegerField(validators=[MaxValueValidator(10000)], default=0, help_text="1/120 hrs ", verbose_name="For certified training")
    E33 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="National", verbose_name="a.Offical ")
    E34 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Local", verbose_name="Local ")
    E35 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Member", verbose_name="b.Member ")
    E36 = models.CharField(choices=PROF_DEVAA, default='', max_length=5, verbose_name="For undergraduate academic honors earned:")
    E37 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive, International", verbose_name="Competitive, International ")
    E38 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, International", verbose_name="Non-Competitive, International ")
    E39 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive National/Regional", verbose_name="Competitive National/Regional ")
    E40 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, National/Regional", verbose_name="on-Competitive, National/Regional ")
    E41 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive, Local", verbose_name="Competitive, Local ")
    E42 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, Local", verbose_name="Non-Competitive, Local ")
    E43 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="International", verbose_name="a.International")
    E44 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="National/Regional", verbose_name="b.National/Regional")
    E45 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Local", verbose_name="c.Local")
    E46 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every year of participation in service-oriented project in the community", verbose_name="For every year of participation in service-oriented project in the community")
    E47 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="First Level", verbose_name="1.First Level ")
    E48 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Second Level", verbose_name="2.Second Level ")
    E49 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Others", verbose_name="3.Others ")
    Practical_Exam = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Practical exam ")
    Class_Demo = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Class demo ")
    Voice_speech = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Voice and Speech")
    Appearance = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Appearance")
    Alertness = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Alertness")
    Ability = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Ability to Present Ideas")
    Judgement = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Judgement")
    Emotional_stability = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Emotional Stability")
    Self_confidence = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Self-Confidence")
    total = models.PositiveIntegerField(blank=True, null=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', verbose_name='user ')

    @property
    def EE1(self):
        return self.E1

    @property
    def EE2(self):
        return self.E2 * .75

    @property
    def EE3(self):
        return self.E3 * 2

    @property
    def EE4(self):
        return self.E4 * 1.75

    @property
    def EE5(self):
        return self.E5 * 1.50

    @property
    def EE6(self):
        return self.E6 * 1.25

    @property
    def EE7(self):
        return self.E7 * 1

    @property
    def EE8(self):
        return self.E8 * 7

    @property
    def EE9(self):
        return self.E9 * 5

    @property
    def EE10(self):
        return self.E10 * 3

    @property
    def EE11(self):
        return self.E11 * 3

    @property
    def EE12(self):
        return self.E12 * 3

    @property
    def EE13(self):
        return self.E13 * 2

    @property
    def EE14(self):
        return self.E14 * 2

    @property
    def EE15(self):
        return self.E15 * 5

    @property
    def EE16(self):
        return self.E16 * 3

    @property
    def EE17(self):
        return self.E17 * 2

    @property
    def EE18(self):
        return self.E18 * 2

    @property
    def EE19(self):
        return self.E19 * 4

    @property
    def EE20(self):
        return self.E20 * 3

    @property
    def EE21(self):
        return self.E21 * 2

    @property
    def EE22(self):
        return self.E22 * 5

    @property
    def EE23(self):
        return self.E23 * 3

    @property
    def EE24(self):
        return self.E24 * 2

    @property
    def EE25(self):
        return self.E25 * 5

    @property
    def EE26(self):
        return self.E26 * 3

    @property
    def EE27(self):
        return self.E27 * 2

    @property
    def EE28(self):
        return self.E28 * 3

    @property
    def EE29(self):
        return self.E29 * 2

    @property
    def EE30(self):
        return self.E30 * 1

    @property
    def EE31(self):
        return self.E31 * 1

    @property
    def EE32(self):
        return self.E32 / 120

    @property
    def EE33(self):
        return self.E33 * 2

    @property
    def EE34(self):
        return self.E34 * 1.5

    @property
    def EE35(self):
        return self.E35 * 1

    @property
    def EE36(self):
        if self.E36 == '3':
            return 3
        elif self.E36 == '2':
            return 2
        elif self.E36 == '1':
            return 1
        elif self.E36 == '0.5':
            return 0.5
        else:
            return 0

    @property
    def EE37(self):
        return self.E37 * 5

    @property
    def EE38(self):
        return self.E38 * 3

    @property
    def EE39(self):
        return self.E39 * 3

    @property
    def EE40(self):
        return self.E40 * 2

    @property
    def EE41(self):
        return self.E41 * 1

    @property
    def EE42(self):
        return self.E42 * 1

    @property
    def EE43(self):
        return self.E43 * 5

    @property
    def EE44(self):
        return self.E44 * 3

    @property
    def EE45(self):
        return self.E45 * 2

    @property
    def EE46(self):
        return self.E46 * 1

    @property
    def EE47(self):
        return self.E47 * 1

    @property
    def EE48(self):
        return self.E48 * 2

    @property
    def EE49(self):
        return self.E49 * .5

    @property
    def exam(self):
        return self.Practical_Exam * .15

    @property
    def educ_qua(self):
        if self.Academic == '85':
            return round(self.doct, 3)
        elif self.Academic == '65':
            return round(self.mast, 3)
        else:
            return round(self.bach, 3)

    @property
    def Educ_Qual(self):
        if self.educ_qua > 34:
            return 85 * .40
        else:
            return self.educ_qua

    @property
    def deg(self):
        if self.Additional3 != 0 and self.Additional4 != 0:
            return ((self.Additional3 / 3) * 1) + ((self.Additional4 / 3) * .5)
        elif self.Additional3 != 0:
            return (self.Additional3 / 3) * 1
        elif self.Additional4 != 0:
            return (self.Additional4 / 3) * .5
        else:
            return 0

    @property
    def doct(self):
        if self.Academic == '85':
            return 85 * .40
        else:
            return 0

    @property
    def mast(self):
        if self.Academic == '65' and self.Special == 1 and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((69 + 25 + self.deg + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((69 + self.deg + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional2 and self.deg != 0:
            return round((69 + 25 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 and self.deg != 0:
            return round((69 + 25 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 == 1 and self.Additional2:
            return round((69 + 25 + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional1 == 1 and self.Additional2:
            return round((69 + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.deg != 0:
            return round((69 + 25 + self.deg) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional2:
            return round((69 + 25 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 == 1:
            return round((69 + 25 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg == 1 and self.Additional1 == 1:
            return round((69 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg == 1 and self.Additional1 == 1:
            return round((69 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg != 0:
            return round((69 + self.deg) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional2 == 1:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 + .40
        elif self.Academic == '65' and self.Additional1 == 2:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65':
            return round(69 * .40, 3)
        else:
            return 0

    @property
    def bach(self):
        if self.Academic == '45' and self.Special == 1 and self.Additional1 == 1 and self.Additional2 == 1 and self.deg != 0:
            return round((45 + 25 + self.deg + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((45 + self.deg + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional2 and self.deg != 0:
            return round((45 + 25 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 and self.deg != 0:
            return round((45 + 25 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 == 1 and self.Additional2:
            return round((45 + 25 + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 1 and self.Additional2:
            return round((45 + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.deg != 0:
            return round((45 + 25 + self.deg) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional2:
            return round((45 + 25 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 == 1:
            return round((45 + 25 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg == 1 and self.Additional1 == 1:
            return round((45 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg == 1 and self.Additional1 == 1:
            return round((45 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg != 0:
            return round((45 + self.deg) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional2 == 1:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 2:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45':
            return round(45 * .40, 3)
        else:
            return 0

    @property
    def subtot2(self):
        return self.EE1 + self.EE2 + self.EE3 + self.EE4 + self.EE5 + self.EE6 + self.EE7

    @property
    def Acad_Exp(self):
        if self.subtot2 > 25:
            return round(25 * .15, 3)
        else:
            return round(self.subtot2 * .15, 3)

    @property
    def subtot3(self):
        return self.EE8 + self.EE9 + self.EE10 + self.EE11 + self.EE12 + self.EE13 + self.EE14 + self.EE15 + self.EE16 + self.EE17 + self.EE18 + self.EE19 + self.EE20 + self.EE21 + self.EE22 + self.EE23 + self.EE24 + self.EE25 + self.EE26 + self.EE27 + self.EE28 + self.EE29 + self.EE30 + self.EE31 + self.EE32 + self.EE33 + self.EE34 + self.EE35 + self.EE37 + self.EE38 + self.EE39 + self.EE40 + self.EE41 + self.EE42 + self.EE43 + self.EE44 + self.EE45 + self.EE46 + self.EE47 + self.EE48 + self.EE49 + self.EE36

    @property
    def Prof_Devt(self):
        if self.subtot3 > 45:
            return round(45 * .10, 3)
        else:
            return round(self.subtot3 * .10, 3)

    @property
    def Demo(self):
        return round(self.Class_Demo * .10, 1)

    @property
    def totalin(self):
        return self.Voice_speech + self.Appearance + self.Alertness + self.Ability + self.Judgement + self.Emotional_stability + self.Self_confidence

    @property
    def Interview(self):
        if self.totalin < 7:
            return 0
        else:
            return round(((self.totalin + 65) * .10), 1)

    @property
    def get_totals(self):
        if self.Academic == '85':
            return round((self.doct + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
        elif self.Academic == '65':
            if self.mast < 40:
                return round((self.mast + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
            else:
                return round((40 + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
        elif self.Academic == '45':
            if self.mast < 40:
                return round((self.bach + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
            else:
                return round((40 + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)

    def save(self, *args, **kwargs):
        self.total = self.get_totals
        super(Architect, self).save(*args, **kwargs)

    @property
    def rank(self):
        aggregate = Architect.objects.filter(total__gt=self.total).aggregate(ranking=Count('total'))
        return aggregate['ranking'] + 1

    @property
    def remarks(self):
        if self.Academic == '85' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET and lack in minimum average qualification requirements')
            else:
                return('Not yet qualified lack in minimum average qualification requirements')
        elif self.Academic == '85' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit')
            else:
                return('Qualified but exceed in age limit')
        elif self.Academic == '85' and self.Age > 45 and self.total < 60:
                return('Not qualified exceed in age limit')
        elif self.Academic == '85' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET')
            else:
                return('Qualified')
        elif self.Academic == '65' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET, lack in minimum average qualification requirements')
            else:
                return('Not yet qualified lack in minimum average qualification requirements')
        elif self.Academic == '65' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit')
            else:
                return('Qualified but exceed in age limit')
        elif self.Academic == '65' and self.Age > 45 and self.total < 60:
                return('Not qualified exceed in age limit')
        elif self.Academic == '65' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET')
            else:
                return('Qualified')
        elif self.Academic == '45' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET, Masters degree needed, lack in minimum average qualification requirements')
            else:
                return('Not yet qualified masters degree needed, lack in minimum average qualification requirements')
        elif self.Academic == '45' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit, no LET & masters degree needed')
            else:
                return('Not qualified masters degree needed & exceed in age limit')
        elif self.Academic == '45' and self.Age > 45 and self.total < 60:
                return('Not qualified masters degree needed & exceed in age limit')
        elif self.Academic == '45' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET & masters degree needed')
            else:
                return('Not yet qualified masters degree needed')


class Nurse(models.Model):
    class Meta:
        verbose_name_plural = "Clinical Instructor - Nurse"
    fname = models.CharField(max_length=100, verbose_name="First name ")
    mname = models.CharField(max_length=100, verbose_name="Middle name ")
    lname = models.CharField(max_length=100, verbose_name="Last name ")
    address = models.CharField(max_length=100, verbose_name="Adress ", help_text="zone/street/barangay/province or city/house no.")
    phone_number = models.CharField(max_length=11, verbose_name="Phone Number ")
    Age = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Age ")
    License = models.BooleanField(verbose_name="LET ")
    Civil_Status = models.CharField(max_length=7, choices=CIVIL_STATUS, verbose_name="Civil Status", default=" ")
    Eligibility = models.CharField(max_length=100, choices=ELIGIBILITY_NURSE, verbose_name="Eligibility", default=" ")
    date_recorded = models.DateTimeField(default=timezone.now, editable=False)
    Academic = models.CharField(max_length=4, verbose_name="Educational Qualification ", choices=STATUS_ACADEMIC, default='', help_text='Highest academic degree or educational attainment in the field of study')
    Special = models.BooleanField(verbose_name='Special Course ', help_text='e.g. Technical/Technician')
    Additional1 = models.BooleanField(help_text="Graduate of five-year Engineering Degree", verbose_name="additional 5 points")
    Additional2 = models.BooleanField(help_text="Licensure Exam", verbose_name="additional 5 points")
    Degree = models.CharField(max_length=3, verbose_name="Question 1 ", choices=STATUS_ADDITIONAL, default='', help_text="Additional Equivalent degree earned, related to the present position")
    Additional3 = models.PositiveIntegerField(validators=[MaxValueValidator(50)], default=0, help_text="For every 3 credits earned toward a higher approved degree course", verbose_name="Question 2 ")
    Additional4 = models.PositiveIntegerField(validators=[MaxValueValidator(50)], default=0, help_text="For every 3 credits earned on the same level", verbose_name="Question 3 ")
    F1 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every full year-time academic service in a state institution of higher learning", verbose_name="Question 4 ")
    F2 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every full year-time academic service in any public or private educational institution other than SUC", verbose_name="Question 5 ")
    F3 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Chief Nurse ")
    F4 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Supervisor ")
    F5 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Senior Nurse ")
    F6 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, verbose_name="Staff Nurse ")
    F7 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as original author ")
    F8 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as co-author ")
    F9 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as reviewer ")
    F10 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as translator ")
    F11 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as editor ")
    F12 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="as compiler ")
    F13 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="International ")
    F14 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="National/Regional ")
    F15 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="Local ")
    F16 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="For every Instructional Manual/Audio-Visual Materials ")
    F17 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    F18 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    F19 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every training course with a duration of at least (pro-rated for less than a year)", verbose_name="c.Local")
    F20 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    F21 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    F22 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For participation as a consultant, expert in any activity of an educational, technological, professional, scientific, or cultural nature (abroad and local) sponsored by the government or other agencies ", verbose_name="c.Local")
    F23 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    F24 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    F25 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For participation as coordinator,lecturer,resource person or guest speaker in conferences,workshops and/or training", verbose_name="c.Local")
    F26 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="a.International")
    F27 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="", verbose_name="b.National/Regional")
    F28 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For official participation in conferences, seminar, workshops ", verbose_name="c.Local")
    F29 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For expert services as adviser in doctoral dissertation and masteral thesis and undergraduate thesis ", verbose_name="expert services")
    F30 = models.PositiveIntegerField(validators=[MaxValueValidator(10000)], default=0, help_text="1/120 hrs ", verbose_name="For certified training")
    F31 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="National", verbose_name="a.Offical ")
    F32 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Local", verbose_name="Local ")
    F33 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Member", verbose_name="b.Member ")
    F34 = models.CharField(choices=PROF_DEVAA, default='', max_length=5, verbose_name="For undergraduate academic honors earned:")
    F35 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive, International", verbose_name="Competitive, International ")
    F36 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, International", verbose_name="Non-Competitive, International ")
    F37 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive National/Regional", verbose_name="Competitive National/Regional ")
    F38 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, National/Regional", verbose_name="on-Competitive, National/Regional ")
    F39 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Competitive, Local", verbose_name="Competitive, Local ")
    F40 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Non-Competitive, Local", verbose_name="Non-Competitive, Local ")
    F41 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="International", verbose_name="a.International")
    F42 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="National/Regional", verbose_name="b.National/Regional")
    F43 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Local", verbose_name="c.Local")
    F44 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="For every year of participation in service-oriented project in the community", verbose_name="For every year of participation in service-oriented project in the community")
    F45 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="First Level", verbose_name="1.First Level ")
    F46 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Second Level", verbose_name="2.Second Level ")
    F47 = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Others", verbose_name="3.Others ")
    Practical_Exam = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Practical exam ")
    Class_Demo = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Class demo ")
    Voice_speech = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Voice and Speech")
    Appearance = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Appearance")
    Alertness = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Alertness")
    Ability = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Ability to Present Ideas")
    Judgement = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Judgement")
    Emotional_stability = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Emotional Stability")
    Self_confidence = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text="rate from 1 - 5 (1 is the lowest)", verbose_name="Self-Confidence")
    total = models.PositiveIntegerField(blank=True, null=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', verbose_name='user ')

    @property
    def FF1(self):
        return self.F1

    @property
    def FF2(self):
        return self.F2 * .75

    @property
    def FF3(self):
        return self.F3 * 2

    @property
    def FF4(self):
        return self.F4 * 1.75

    @property
    def FF5(self):
        return self.F5 * 1.50

    @property
    def FF6(self):
        return self.F6 * 1

    @property
    def FF7(self):
        return self.F7 * 5

    @property
    def FF8(self):
        return self.F8 * 3

    @property
    def FF9(self):
        return self.F9 * 3

    @property
    def FF10(self):
        return self.F10 * 3

    @property
    def FF11(self):
        return self.F11 * 2

    @property
    def FF12(self):
        return self.F12 * 2

    @property
    def FF13(self):
        return self.F13 * 5

    @property
    def FF14(self):
        return self.F14 * 3

    @property
    def FF15(self):
        return self.F15 * 2

    @property
    def FF16(self):
        return self.F16 * 2

    @property
    def FF17(self):
        return self.F17 * 4

    @property
    def FF18(self):
        return self.F18 * 3

    @property
    def FF19(self):
        return self.F19 * 2

    @property
    def FF20(self):
        return self.F20 * 5

    @property
    def FF21(self):
        return self.F21 * 3

    @property
    def FF22(self):
        return self.F22 * 2

    @property
    def FF23(self):
        return self.F23 * 5

    @property
    def FF24(self):
        return self.F24 * 3

    @property
    def FF25(self):
        return self.F25 * 2

    @property
    def FF26(self):
        return self.F26 * 3

    @property
    def FF27(self):
        return self.F27 * 2

    @property
    def FF28(self):
        return self.F28 * 1

    @property
    def FF29(self):
        return self.F29 * 1

    @property
    def FF30(self):
        return self.F30 / 120

    @property
    def FF31(self):
        return self.F31 * 2

    @property
    def FF32(self):
        return self.F32 * 1.5

    @property
    def FF33(self):
        return self.F33 * 1

    @property
    def FF34(self):
        if self.F34 == '3':
            return 3
        elif self.F34 == '2':
            return 2
        elif self.F34 == '1':
            return 1
        elif self.F34 == '0.5':
            return 0.5
        else:
            return 0

    @property
    def FF35(self):
        return self.F35 * 5

    @property
    def FF36(self):
        return self.F36 * 3

    @property
    def FF37(self):
        return self.F37 * 3

    @property
    def FF38(self):
        return self.F38 * 2

    @property
    def FF39(self):
        return self.F39 * 1

    @property
    def FF40(self):
        return self.F40 * 1

    @property
    def FF41(self):
        return self.F41 * 5

    @property
    def FF42(self):
        return self.F42 * 3

    @property
    def FF43(self):
        return self.F43 * 2

    @property
    def FF44(self):
        return self.F44 * 1

    @property
    def FF45(self):
        return self.F45 * 1

    @property
    def FF46(self):
        return self.F46 * 2

    @property
    def FF47(self):
        return self.F47 * .5

    @property
    def exam(self):
        return self.Practical_Exam * .15

    @property
    def educ_qua(self):
        if self.Academic == '85':
            return round(self.doct, 3)
        elif self.Academic == '65':
            return round(self.mast, 3)
        else:
            return round(self.bach, 3)

    @property
    def Educ_Qual(self):
        if self.educ_qua > 34:
            return 85 * .40
        else:
            return self.educ_qua

    @property
    def deg(self):
        if self.Additional3 != 0 and self.Additional4 != 0:
            return ((self.Additional3 / 3) * 1) + ((self.Additional4 / 3) * .5)
        elif self.Additional3 != 0:
            return (self.Additional3 / 3) * 1
        elif self.Additional4 != 0:
            return (self.Additional4 / 3) * .5
        else:
            return 0

    @property
    def doct(self):
        if self.Academic == '85':
            return 85 * .40
        else:
            return 0

    @property
    def mast(self):
        if self.Academic == '65' and self.Special == 1 and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((69 + 25 + self.deg + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((69 + self.deg + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional2 and self.deg != 0:
            return round((69 + 25 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 and self.deg != 0:
            return round((69 + 25 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 == 1 and self.Additional2:
            return round((69 + 25 + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional1 == 1 and self.Additional2:
            return round((69 + 5 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.deg != 0:
            return round((69 + 25 + self.deg) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional2:
            return round((69 + 25 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1 and self.Additional1 == 1:
            return round((69 + 25 + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg == 1 and self.Additional1 == 1:
            return round((69 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg == 1 and self.Additional1 == 1:
            return round((69 + self.deg + 5) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.deg != 0:
            return round((69 + self.deg) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Additional2 == 1:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 + .40
        elif self.Academic == '65' and self.Additional1 == 2:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65' and self.Special == 1:
            return round((69 + 25) * .40, 3)
            if self.mast > 85:
                return 85 * .40
        elif self.Academic == '65':
            return round(69 * .40, 3)
        else:
            return 0

    @property
    def bach(self):
        if self.Academic == '45' and self.Special == 1 and self.Additional1 == 1 and self.Additional2 == 1 and self.deg != 0:
            return round((45 + 25 + self.deg + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 1 and self.Additional2 and self.deg != 0:
            return round((45 + self.deg + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional2 and self.deg != 0:
            return round((45 + 25 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 and self.deg != 0:
            return round((45 + 25 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 == 1 and self.Additional2:
            return round((45 + 25 + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 1 and self.Additional2:
            return round((45 + 5 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.deg != 0:
            return round((45 + 25 + self.deg) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional2:
            return round((45 + 25 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1 and self.Additional1 == 1:
            return round((45 + 25 + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg == 1 and self.Additional1 == 1:
            return round((45 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg == 1 and self.Additional1 == 1:
            return round((45 + self.deg + 5) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.deg != 0:
            return round((45 + self.deg) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional2 == 1:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Additional1 == 2:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45' and self.Special == 1:
            return round((45 + 25) * .40, 3)
            if self.bach > 85:
                return 85 * 40
        elif self.Academic == '45':
            return round(45 * .40, 3)
        else:
            return 0

    @property
    def subtot2(self):
        return self.FF1 + self.FF2 + self.FF3 + self.FF4 + self.FF5 + self.FF6

    @property
    def Acad_Exp(self):
        if self.subtot2 > 25:
            return round(25 * .15, 3)
        else:
            return round(self.subtot2 * .15, 3)

    @property
    def subtot3(self):
        return self.FF7 + self.FF8 + self.FF9 + self.FF10 + self.FF11 + self.FF12 + self.FF13 + self.FF14 + self.FF15 + self.FF16 + self.FF17 + self.FF18 + self.FF19 + self.FF20 + self.FF21 + self.FF22 + self.FF23 + self.FF24 + self.FF25 + self.FF26 + self.FF27 + self.FF28 + self.FF29 + self.FF30 + self.FF31 + self.FF32 + self.FF33 + self.FF35 + self.FF36 + self.FF37 + self.FF38 + self.FF39 + self.FF40 + self.FF41 + self.FF42 + self.FF43 + self.FF44 + self.FF45 + self.FF46 + self.FF47 + self. FF44

    @property
    def Prof_Devt(self):
        if self.subtot3 > 45:
            return round(45 * .10, 3)
        else:
            return round(self.subtot3 * .10, 3)

    @property
    def Demo(self):
        return round(self.Class_Demo * .10, 1)

    @property
    def totalin(self):
        return self.Voice_speech + self.Appearance + self.Alertness + self.Ability + self.Judgement + self.Emotional_stability + self.Self_confidence

    @property
    def Interview(self):
        if self.totalin < 7:
            return 0
        else:
            return round(((self.totalin + 65) * .10), 1)

    @property
    def get_totals(self):
        if self.Academic == '85':
            return round((self.doct + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
        elif self.Academic == '65':
            if self.mast < 40:
                return round((self.mast + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
            else:
                return round((40 + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
        elif self.Academic == '45':
            if self.mast < 40:
                return round((self.bach + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)
            else:
                return round((40 + self.Acad_Exp + self.Prof_Devt + self.Interview + self.Demo + self.exam), 3)

    def save(self, *args, **kwargs):
        self.total = self.get_totals
        super(Nurse, self).save(*args, **kwargs)

    @property
    def rank(self):
        aggregate = Nurse.objects.filter(total__gt=self.total).aggregate(ranking=Count('total'))
        return aggregate['ranking'] + 1

    @property
    def remarks(self):
        if self.Academic == '85' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET and lack in minimum average qualification requirements')
            else:
                return('Not yet qualified lack in minimum average qualification requirements')
        elif self.Academic == '85' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit')
            else:
                return('Qualified but exceed in age limit')
        elif self.Academic == '85' and self.Age > 45 and self.total < 60:
                return('Not qualified exceed in age limit')
        elif self.Academic == '85' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET')
            else:
                return('Qualified')
        elif self.Academic == '65' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET, lack in minimum average qualification requirements')
            else:
                return('Not yet qualified lack in minimum average qualification requirements')
        elif self.Academic == '65' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit')
            else:
                return('Qualified but exceed in age limit')
        elif self.Academic == '65' and self.Age > 45 and self.total < 60:
                return('Not qualified exceed in age limit')
        elif self.Academic == '65' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET')
            else:
                return('Qualified')
        elif self.Academic == '45' and self.Age <= 45 and self.total < 60:
            if self.License == 0:
                return('Not yet qualified no LET, Masters degree needed, lack in minimum average qualification requirements')
            else:
                return('Not yet qualified masters degree needed, lack in minimum average qualification requirements')
        elif self.Academic == '45' and self.Age > 45 and self.total >= 60:
            if self.License == 0:
                return('Not qualified no LET and exceed in age limit, no LET & masters degree needed')
            else:
                return('Not qualified masters degree needed & exceed in age limit')
        elif self.Academic == '45' and self.Age > 45 and self.total < 60:
                return('Not qualified masters degree needed & exceed in age limit')
        elif self.Academic == '45' and self.Age <= 45 and self.total >= 60:
            if self.License == 0:
                return('Not yet qualified no LET & masters degree needed')
            else:
                return('Not yet qualified masters degree needed')


class ApplicantAdmin(admin.ModelAdmin):
    ordering = ('-total', )
    actions = ['download_csv']
    list_display = ('name_of_applicant', 'Age', 'Civil_Status', 'Eligibility', 'License', 'date_recorded', 'Academic', 'Educ_Qual', 'Acad_Exp', 'Prof_Devt', 'exam', 'Demo', 'Interview', 'total', 'rank', 'remarks')
    list_display_links = ('name_of_applicant', 'Age', 'Civil_Status', 'Eligibility', 'License', 'date_recorded', 'Academic', 'Educ_Qual', 'Acad_Exp', 'Prof_Devt', 'exam', 'Demo', 'Interview', 'total', 'rank', 'remarks')
    change_list_template = 'change_list_graph.html'

    def name_of_applicant(self, obj):
        return "{} {} {}".format(obj.fname, obj.mname, obj.lname)

    def download_csv(self, request, queryset):
        None
    download_csv.short_description = "Download CSV file for selected stats."

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        from io import StringIO

        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["id", "fname", "mname", "lname", "address", "Age", "Civil_Status", "Eligibility", "date_recorded", "Academic", "Demo", "Interview", "total", "remarks"])
        for s in queryset:
            writer.writerow([s.id, s.fname, s.mname, s.lname, s.address, s.Age, s.Civil_Status, s.Eligibility, s.date_recorded, s.Academic, s.Demo, s.Interview, s.total, s.remarks])
        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=applicant.csv'
        return response


class ITAdmin(admin.ModelAdmin):
    ordering = ('-total', )
    actions = ['download_csv']
    list_display = ('name_of_applicant', 'Age', 'Civil_Status', 'License', 'date_recorded', 'Academic', 'Educ_Qual', 'Acad_Exp', 'Prof_Devt', 'exam', 'Demo', 'Interview', 'total', 'rank', 'remarks')
    list_display_links = ('name_of_applicant', 'Age', 'Civil_Status', 'License', 'date_recorded', 'Academic', 'Educ_Qual', 'Acad_Exp', 'Prof_Devt', 'exam', 'Demo', 'Interview', 'total', 'rank', 'remarks')
    search_fields = ('id', 'fname', 'mname', 'lname', 'Academic')
    change_list_template = 'change_list_graph.html'

    def name_of_applicant(self, obj):
        return "{} {} {}".format(obj.fname, obj.mname, obj.lname)

    def download_csv(self, request, queryset):
        None
    download_csv.short_description = "Download CSV file for selected stats."

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        from io import StringIO

        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["id", "fname", "mname", "lname", "address", "Age", "Civil_Status", "Eligibility", "date_recorded", "Academic", "Demo", "Interview", "total", "remarks"])
        for s in queryset:
            writer.writerow([s.id, s.fname, s.mname, s.lname, s.address, s.Age, s.Civil_Status, s.Eligibility, s.date_recorded, s.Academic, s.Demo, s.Interview, s.total, s.remarks])
        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=applicant.csv'
        return response


admin.site.register(Nurse, ApplicantAdmin)
admin.site.register(Architect, ApplicantAdmin)
admin.site.register(Electronics_Engr, ApplicantAdmin)
admin.site.register(Mechanical_Engr, ApplicantAdmin)
admin.site.register(Civil_Engr, ApplicantAdmin)
admin.site.register(Applicant, ITAdmin)
