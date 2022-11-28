from django.test import TestCase

class TestAvaliacao(TestCase):
    def setUp(self):
        self.index = self.client.get('')
        self.cadastro = self.client.get('cadastro')
        self.alunos = self.client.get('alunos')

    def test_200_response(self):
        self.assertEqual(200, self.index.status_code)

    def test_200_response(self):
        self.assertEqual(200, self.cadastro.status_code)
    
    def test_200_response(self):
        self.assertEqual(200, self.alunos.status_code)

    def test_template_index(self):
        self.assertTemplateUsed(self.index, 'index.html')
    
    def test_template_cadastro(self):
        self.assertTemplateUsed(self.cadastro, 'cadastro.html')
    
    def test_template_alunos(self):
        self.assertTemplateUsed(self.alunos, 'alunos.html')