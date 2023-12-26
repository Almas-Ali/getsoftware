from datetime import datetime


short_description = '''
To get all premium softwares for free stay with us. Create an account to get more benifits like liking a post, commenting in a post etc.
You can also subscribe to our newsletter to get out latest updates.
<br><br>
Thanks for being with us.<br>
Admin
'''


about_page = '''
<p>
Hi, User <br><br>
Welcome to Get Free Software website. We provide premium softwares for free for everyone. If you like free software you can connect with us by subscribing to our newsletter for free or creating a free account on our website. We will sent you all of our latest updates about latest softwares. You don't have to pay for any softwares form now. You will get what ever you want. <br><br>

Internet need to be free and softwares have to open source. This way people can use them. Else many poor developer or normal users will not be able to use the benifits of those softwares. We feel those pains. <br><br>

If your belongs from a middle class family you will understand the sragule of a developer. You have to think about every thing about your family, carrier etc. You have many reasone on hign thought, so we are here to make clear some of your thoughts. From now don't think about softwares any more. Just have a relax time with your family and carrier. We are taking all those responsibelities from now. <br>
Stay with us and have a great time. <br>
<br>Thanks, From Developer
</p>
'''


config = {
    'website_name': 'Get Free Software',
    'sub_title': 'Softwares for everyone.',
    'short_name': 'soft',
    'top_domain': '.net',
    'main_domain': '.almasali.net',
    'domain': 'soft.almasali.net',
    'full_address': 'https://soft.almasali.net/',
    'author': 'Md. Almas Ali',
    'image': 'static/img/getfreesoftware.net.svg',
    'short_description': short_description,
    'email': 'support@soft.almasali.net',
    'number': '+8809600000000',
    'facebook': 'https://facebook.com/md.almasali.0',
    'github': 'https://github.com/Almas-Ali',
    'instagram': 'https://instagram.com/almaspr3',
    'twitter': 'https://twitter.com/almasali22',
    'linkedin': 'https://linkedin.com/in/md-almasali',
    'google': 'https://www.google.com/search?hl=en&q=Md.%20Almas%20Ali',
    'other_website_1': 'https://almasali.net',
    'other_website_2': 'https://almasali.tech',
    'about_page': about_page,
    'copyright': f'Copyright &copy; {datetime.now().year} - All Rights Reserved',
}


def precessors(request):
    '''Context preprocessor.'''

    return {'config': config}
