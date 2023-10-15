from django import forms

class NewHabitForm(forms.Form):
    habit_name = forms.CharField(label="Enter your new habit",max_length=255)
    habit_tag = forms.CharField(label="Tags (optional)",max_length=255) #later to be changed with a multi select dropdown set up
    habit_start_date = forms.DateTimeField(label="When do you wish to start this activity")
    habit_end_date = forms.DateTimeField(label="When do you wish to end this activity") #can be optional
    min_time_to_spend = forms.DurationField(label="What's the minimum amount of time you can spend on this activity")
    # min_number_of_days_to_spend = forms.IntegerField(label="What's the minimum number of days you can spend on this activity")
    habit_performing_days = forms.MultipleChoiceField(label="Choose the days on which you want to do this activity")
    reminder_frequency = forms.ChoiceField(choices=[
                                                    ('daily','Daily'),
                                                    ('monthly','Monthly'),
                                                    ('bi-monthly','Bi-monthly'),
                                                    ('quarterly','Quarterly')
                                                    ])

class ExistingHabitForm(forms.Form):
    habit_name = forms.ChoiceField() #choices to be populated by the habits that are created using the above form.
    day_of_performing_task = forms.ChoiceField() #options are the days of the week
    habit_start_time = forms.TimeField()
    habit_end_time = forms.TimeField()
    remarks = forms.CharField(max_length=5000)