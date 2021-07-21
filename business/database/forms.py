from django import forms
from database.models import Exhibition

class PeopleCheck(forms.Form):
	currentperson = forms.CharField(label = "Insert name here:", max_length=100)
	

	


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class TimeInput(forms.TimeInput):
    input_type = "time"


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M:%s"
        super().__init__(**kwargs)


class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["start"].widget = DateInput()
        self.fields["end"].widget = DateInput()
        self.fields["opening"].widget = TimeInput()
        self.fields["closing"].widget = TimeInput()
       

	
	
	
	
