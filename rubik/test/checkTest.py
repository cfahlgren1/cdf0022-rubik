from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
        
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')

    """
    Test that cube value is present
    """
    def test_check_020_ShouldReturnErrorNoValuePresent(self):
        parm = {'op':'check'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: no value present')

    """
    Test that cube value is of type str
    """
    def test_check_030_ShouldReturnErrorIncorrectValue(self):
        parm = {'op':'check', 'cube': 2}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: value is of wrong type')
    
    """
    Test cube character size at boundary
    """
    def test_check_040_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    """
    Test cube character size above boundary
    """
    def test_check_050_ShouldErrorIncorrectCharCount(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwwbbbbbbbbb'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: incorrect character count')
    
    """
    Test cube character size below boundary
    """
    def test_check_060_ShouldReturnErrorIncorrectCharCount(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: incorrect character count')

    """
    Test cube character groups and occurences
    """
    def test_check_070_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    """
    Test incorrect cube color occurences
    """
    def test_check_090_ShouldErrorIncorrectCharCount(self):
        parm = {'op':'check', 'cube': 'bbbbbbbrrrrrrrrrrrgggggggggoooooooooyyyyyyyyy'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: incorrect character count')
    
    """
    Test incorrect cube unique colors 
    """
    def test_check_100_ShouldErrorIncorrectCharCount(self):
        parm = {'op':'check', 'cube': 'ffffffaaaaaaeeeeeerrrrrrttttttyyyyyyuuuuuuiiiiiillllll'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: incorrect character count')





