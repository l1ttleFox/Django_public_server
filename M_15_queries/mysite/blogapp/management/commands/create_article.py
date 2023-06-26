from django.contrib.auth.models import User
from django.core.management import BaseCommand

from blogapp.models import Article, Author, Category, Tag


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Trying to create the article")
        category = Category.objects.create(name="information")
        tag1 = Tag.objects.create(name="animals")
        tag2 = Tag.objects.create(name="cute")
        author = Author.objects.create(name="bunnyfan1995")
        article, created_or_not = Article.objects.get_or_create(
            title="Rabbits",
            content="Rabbits, also known as bunnies or bunny rabbits, are small mammals in the family Leporidae (which also contains the hares) of the order Lagomorpha (which also contains the pikas). Oryctolagus cuniculus includes the European rabbit species and its descendants, the world's 305 breeds[1] of domestic rabbit. Sylvilagus includes 13 wild rabbit species, among them the seven types of cottontail. The European rabbit, which has been introduced on every continent except Antarctica, is familiar throughout the world as a wild prey animal and as a domesticated form of livestock and pet. With its widespread effect on ecologies and cultures, the rabbit is, in many areas of the world, a part of daily life—as food, clothing, a companion, and a source of artistic inspiration. Although once considered rodents, lagomorphs like rabbits have been discovered to have diverged separately and earlier than their rodent cousins and have a number of traits rodents lack, like two extra incisors.",
            author=author,
            category=category
        )
        article.tags.add(tag1, tag2)
        article.save()
        self.stdout.write(f"Created {article}")