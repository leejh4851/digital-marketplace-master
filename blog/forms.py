from django import forms
from .models import Post


class PostForm(forms.ModelForm):  # ModelForm

	class Meta:

		model = Post  # model 에 정의된 class Post 에서 
		fields = ['title', 'author', 'content'] # 사용자로부터 여기에 적어준 field 데이터를 직접 입력 받는다. 
