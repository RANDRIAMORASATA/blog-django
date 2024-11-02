from django import forms
from blog.models import Post

class CreateNewPostForm(forms.ModelForm):
    #  title = models.CharField(max_length=20)
    # slug = models.SlugField(max_length=40)
    # content = models.TextField()
    # #un user peut avoir plusieur post mais un post pour un user OnToMany mais un un post ne peut u avoir un user
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # #un post peut avoir qu une category  mais une category peut avoir plusieur post
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # isPublished = models.BooleanField(default=False)
    # tags = models.ManyToManyField(Tag)
    # createdAt= models.DateTimeField(auto_now_add=True)
    # updatedAt=models.DateTimeField(auto_now=True)
    class Meta:
        model = Post
        fields = ('title', 'content',  'category', 'tags', 'isPublished', 'image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
             'content': forms.Textarea(attrs={'id': 'id_content', 'class': 'form-control textarea'}),
            'category': forms.Select(attrs={'class' : 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class' : 'form-control'}),
            'isPublished': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class' : 'form-control'}),
        }