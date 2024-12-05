from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Write comments'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'comment-input'})
