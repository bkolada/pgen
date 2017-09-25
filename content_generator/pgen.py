import unicodedata
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from datetime import datetime

def main():
    generate_article()


def generate_article():
    answers = ask_article_questions()
    path = 'content/{}.md'.format(answers['slug'])
    with codecs.open(path, 'w', encoding="utf-8") as content:
        for key, value in answers.iteritems():
            content.write("{}: {}\n".format(key.capitalize(), value))


def ask_article_questions():
    title = raw_input('What is the title? ')
    tags = raw_input('What are tags use , to seperate them? ')
    category = raw_input('What is category? ')
    if can_title_be_slug(title):
        slug = raw_input('What is slug for article? ')
    else:
        slug = "_".join(title.split())
    date = datetime.today().strftime("%Y-%m-%d")
    return dict(
        title=title,
        tags=tags,
        category=category,
        slug=strip_accents(slug),
        date=date
    )


def strip_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text.decode('utf8')) if unicodedata.category(c) != 'Mn')


def can_title_be_slug(title):
    return True


if __name__ == "__main__":
    main()
