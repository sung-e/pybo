from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields=['subject', 'content']
        widgets={
            'subject': forms.TextInput(attrs={'class':'form-contrl'}),
            'content':forms.TextInput(attrs={'class':'form-control', 'rows':100}),
        }

class AnswerForm(forms.Modelform):
    class Meta:
        model=Answer
        fields=['content']
        labels={
            'content':'답변내용',
        }
