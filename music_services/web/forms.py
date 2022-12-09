from django import forms
from music_services.web.models import Service, Recommendation


class ServiceBaseForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceCreateForm(ServiceBaseForm):
    pass


class ServiceEditForm(ServiceBaseForm):
    pass


class ServiceDeleteForm(ServiceBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__make_hidden_fields()

    def save(self, commit=True):
        if commit:
            Service.objects.all().delete()
            self.instance.delete()
        else:
            return self.instance

    def __make_hidden_fields(self):
        for _, f in self.fields.items():
            f.widget = forms.HiddenInput()


class RecommendationCreateForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = '__all__'
