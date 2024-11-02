#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()
    try:
        from django.contrib.auth.models import User
        from blog.models import Category, Post, Tag,Post, Profile
        from faker import Faker
        import random
        fake = Faker()


        def create_users(max = 5):
            for _ in range(max):
                User.objects.create(
                                    username=fake.user_name(), 
                                    email = fake.email(),
                                    first_name = fake.first_name(),
                                    last_name= fake.last_name())
        def create_categories(max=5):
            for _ in range(max):
                Category.objects.create(
                    name = fake.word(),
                    description = fake.sentence()
                )
        def create_tags(max=5):
            for _ in range(max):
                Tag.objects.create(
                    name = fake.word(),
                    description = fake.sentence()
                )
        def create_posts(max=50):
            users = list(User.objects.all())
            categories = list(Category.objects.all())
            tags = list(Tag.objects.all())
            for _ in range(max):
                post = Post.objects.create(
                        title = fake.sentence(),
                        #slug = fake.slug(),
                        content = fake.paragraph(nb_sentences=random.randint(60,100)),
                        author = random.choice(users),
                        category = random.choice(categories),
                        isPublished = fake.boolean()
       
                     )
                post.tags.set(random.sample(tags, random.randint(1,5)))
                
        def create_profiles(max=5):
            users = list (User.objects.all())
            for _ in random.sample(users, min(max, len(users))): #evite de depasser lenbre max de l user
                Profile.objects.create(
                    user = _,
                    description =fake.sentence(),

                )
        # create_users(20)   
        # create_tags(7)       
        # create_categories(10)
        # create_posts(100),
        # create_profiles(20)

    except Exception as err:
        print( "Error : ", err)


if __name__ == '__main__':
    main()
