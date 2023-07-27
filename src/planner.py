import json

from src.tools.index import Tool


class Planner:
    @classmethod
    def plan(self, llm, config, memory):
        if memory.make_plan:
            response_format = {
                "plan": [
                    {
                        "title": "You should return a short title for the current step",
                        "description": "You should return a long detailed description about the current step and justify it",
                        "action": {"name": "tool name", "args": {"arg name": "value"}},
                        "files": "You must always list all files created by the action. This can never be empty. Required",
                    }
                ],
            }

            example = {
                "plan": [
                    {
                        "title": "Create Django project",
                        "description": "Create a new Django project for the blog application.",
                        "action": {
                            "name": "terminal",
                            "args": {
                                "command": "django-admin startproject blog_project"
                            },
                        },
                        "files": ["blog_project/"],
                    },
                    {
                        "title": "Create Django app",
                        "description": "Create a new Django app within the project to handle the blog functionality.",
                        "action": {
                            "name": "terminal",
                            "args": {
                                "command": "cd ./blog_project && python manage.py startapp blog"
                            },
                        },
                        "files": ["blog_project/blog/"],
                    },
                    {
                        "title": "Define database models",
                        "description": "Define the necessary Django database models for user authentication, blog posts, categories, tags, comments, and user permissions.",
                        "action": {
                            "name": "write_file",
                            "args": {
                                "file_path": "blog_project/blog/models.py",
                                "thoughts": "To implement the given code, follow these steps: Import the necessary modules: Include the following import statements at the beginning of your Python file: from django.contrib.auth.models import AbstractUser from django.db import modelsDefine the BlogPost model: Create a new class called BlogPost and make it inherit from models.Model. Inside the class, define the required fields: title, content, tags, date, and author. Ensure that the appropriate field types are used (e.g., CharField, TextField, DateTimeField, ForeignKey, ManyToManyField). Define the Category model: Create a new class called Category and make it inherit from models.Model. Inside the class, define the required fields, such as name, using the appropriate field type. Define the Tag model: Create a new class called Tag and make it inherit from models.Model. Inside the class, define the required fields, such as name, using the appropriate field type. Define the Comment model: Create a new class called Comment and make it inherit from models.Model. Inside the class, define the required fields: content, date, author, blog_post, and parent_comment. Make sure to specify the correct field types and relationships (e.g., ForeignKey for relationships with User, BlogPost, and self). Define the UserPermission model (not present in the given code): If necessary, create a new class called UserPermission and make it inherit from models.Model. Inside the class, define the fields for defining user permissions, using appropriate field types and relationships. Remember to apply any additional configurations, such as database migrations, as required by the Django framework in order to reflect these changes in your database schema.",
                                "code": "from django.contrib.auth.models import AbstractUser\nfrom django.db import models\n\nclass User(AbstractUser):\n # Add custom fields or behaviors if needed\n pass\n\n\nclass BlogPost(models.Model):\n title = models.CharField(max_length=255)\n content = models.TextField()\n tags = models.ManyToManyField('Tag')\n date = models.DateTimeField(auto_now_add=True)\n author = models.ForeignKey(User, on_delete=models.CASCADE)\n\n\nclass Category(models.Model):\n name = models.CharField(max_length=100)\n # Add more fields as required\n\n\nclass Tag(models.Model):\n name = models.CharField(max_length=100)\n # Add more fields as required\n\n\nclass Comment(models.Model):\n content = models.TextField()\n date = models.DateTimeField(auto_now_add=True)\n author = models.ForeignKey(User, on_delete=models.CASCADE)\n blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)\n parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)\n\n\nclass UserPermission(models.Model):\n user = models.OneToOneField(User, on_delete=models.CASCADE)\n # Define permissions fields as required\n",
                            },
                        },
                        "files": ["blog_project/blog/models.py"],
                    },
                    {
                        "title": "Create Django views",
                        "description": "Create views to handle API requests and responses.",
                        "action": {
                            "name": "write_file",
                            "args": {
                                "file_path": "blog_project/blog/views.py",
                                "thoughts": "To implement the given code, follow these steps: Import the necessary modules: Include the following import statements at the beginning of your Python file: from rest_framework import generics from .models import BlogPost, Category, Tag, Comment from .serializers import BlogPostSerializer, CategorySerializer, TagSerializer, CommentSerializer Define the views for the BlogPost model: BlogPostListCreateView: Create a class called BlogPostListCreateView and make it inherit from generics.ListCreateAPIView. Inside the class, set the queryset attribute to BlogPost.objects.all() and the serializer_class attribute to BlogPostSerializer. BlogPostRetrieveUpdateDeleteView: Create a class called BlogPostRetrieveUpdateDeleteView and make it inherit from generics.RetrieveUpdateDestroyAPIView. Inside the class, set the queryset attribute to BlogPost.objects.all() and the serializer_class attribute to BlogPostSerializer. Define the views for the Category model: CategoryListCreateView: Create a class called CategoryListCreateView and make it inherit from generics.ListCreateAPIView. Inside the class, set the queryset attribute to Category.objects.all() and the serializer_class attribute to CategorySerializer. CategoryRetrieveUpdateDeleteView: Create a class called CategoryRetrieveUpdateDeleteView and make it inherit from generics.RetrieveUpdateDestroyAPIView. Inside the class, set the queryset attribute to Category.objects.all() and the serializer_class attribute to CategorySerializer. Define the views for the Tag model: TagListCreateView: Create a class called TagListCreateView and make it inherit from generics.ListCreateAPIView. Inside the class, set the queryset attribute to Tag.objects.all() and the serializer_class attribute to TagSerializer. TagRetrieveUpdateDeleteView: Create a class called TagRetrieveUpdateDeleteView and make it inherit from generics.RetrieveUpdateDestroyAPIView. Inside the class, set the queryset attribute to Tag.objects.all() and the serializer_class attribute to TagSerializer. Define the views for the Comment model: CommentListCreateView: Create a class called CommentListCreateView and make it inherit from generics.ListCreateAPIView. Inside the class, set the queryset attribute to Comment.objects.all() and the serializer_class attribute to CommentSerializer. CommentRetrieveUpdateDeleteView: Create a class called CommentRetrieveUpdateDeleteView and make it inherit from generics.RetrieveUpdateDestroyAPIView. Inside the class, set the queryset attribute to Comment.objects.all() and the serializer_class attribute to CommentSerializer. Customize the views: If you need to add any additional logic or customize the behavior of these views, you can override the methods provided by the generic views.",
                                "code": "from rest_framework import generics\nfrom .models import BlogPost, Category, Tag, Comment\nfrom .serializers import BlogPostSerializer, CategorySerializer, TagSerializer, CommentSerializer\n\n\nclass BlogPostListCreateView(generics.ListCreateAPIView):\n queryset = BlogPost.objects.all()\n serializer_class = BlogPostSerializer\n\n\nclass BlogPostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):\n queryset = BlogPost.objects.all()\n serializer_class = BlogPostSerializer\n\n\nclass CategoryListCreateView(generics.ListCreateAPIView):\n queryset = Category.objects.all()\n serializer_class = CategorySerializer\n\n\nclass CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):\n queryset = Category.objects.all()\n serializer_class = CategorySerializer\n\n\nclass TagListCreateView(generics.ListCreateAPIView):\n queryset = Tag.objects.all()\n serializer_class = TagSerializer\n\n\nclass TagRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):\n queryset = Tag.objects.all()\n serializer_class = TagSerializer\n\n\nclass CommentListCreateView(generics.ListCreateAPIView):\n queryset = Comment.objects.all()\n serializer_class = CommentSerializer\n\n\nclass CommentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):\n queryset = Comment.objects.all()\n serializer_class = CommentSerializer",
                            },
                        },
                        "files": ["blog_project/blog/views.py"],
                    },
                ]
            }

            prompt_string = (
                f"Create a plan for developing the following application: {config.app_description}\n"
                f"Think step by step, break the objective in intermediate steps and justify your step.\n\n"
                f"You must always write the correct file path in actions.\n"
                f"You must use docker-compose"
                f"DO NOT INCLUDE THE FOLLOWING ACTIONS:\n"
                f"- Creation of virtual enviroment\n"
                f"- Deploy\n"
                f"- Run server\n\n"
                f"Each step must be a action using one of this tools:\n"
                f"{json.dumps(Tool.list_tools(), indent=4)}\n\n"
                f"You should only respond in JSON format as described below:\n"
                f"Response Format:\n"
                f"{json.dumps(response_format, indent=4)}\n"
                f"Ensure the response can be parsed by Python json.loads. Only return the json!\n"
                f"Exemple:\n"
                f"{json.dumps(example, indent=4)}\n\n"
            )

            plan_response = llm.generate(prompt_string)

            memory.plan = plan_response["plan"]

            memory.make_plan = False
