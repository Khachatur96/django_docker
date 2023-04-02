from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from django.contrib.auth import get_user_model


from pages.views import AboutPageView
class HomepageTests(SimpleTestCase): # new
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
        
    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
        
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')
        
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')
        
    
    
class AboutPageTests(SimpleTestCase): # new
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)
        
    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
        
    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')
        
    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')
        # 
    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
        view.func.__name__,
        AboutPageView.as_view().__name__
        )
        

class CustomUserTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
        
        
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')
        
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
        self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
        [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
        [0].email, self.email)
