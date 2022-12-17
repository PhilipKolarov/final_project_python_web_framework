from django import forms

from music_services.web.models import Service, Recommendation, Review, Announcement


class ServiceBaseForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'type', 'description', 'image_url', 'price']


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
            self.instance.delete()
        else:
            return self.instance

    def __make_hidden_fields(self):
        for _, f in self.fields.items():
            f.widget = forms.HiddenInput()


class RecommendationBaseForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['description',]


class RecommendationCreateForm(RecommendationBaseForm):
    pass


class RecommendationEditForm(RecommendationBaseForm):
    pass


class RecommendationDeleteForm(RecommendationBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__make_hidden_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            return self.instance

    def __make_hidden_fields(self):
        for _, f in self.fields.items():
            f.widget = forms.HiddenInput()


class ReviewBaseForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')


class ReviewCreateForm(ReviewBaseForm):
    pass


class ReviewEditForm(ReviewBaseForm):
    pass


class AnnouncementBaseForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'info')


class AnnouncementCreateForm(AnnouncementBaseForm):
    pass


class AnnouncementEditForm(AnnouncementBaseForm):
    pass


class AnnouncementDeleteForm(AnnouncementBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__make_hidden_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            return self.instance

    def __make_hidden_fields(self):
        for _, f in self.fields.items():
            f.widget = forms.HiddenInput()
