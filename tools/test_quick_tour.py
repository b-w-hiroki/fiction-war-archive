import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class QuickTourTests(unittest.TestCase):
    def test_astarte_has_three_existing_phases(self):
        text = (ROOT / 'docs/ginei/astarte.html').read_text()
        for phase in (0, 2, 6):
            self.assertIn(f'data-tour-phase="{phase}"', text)
        self.assertEqual(text.count('data-tour-phase="'), 3)
        self.assertIn('i>=PH.length', text)
        self.assertNotIn('@@QUICK_TOUR', text)
    def test_other_battle_unchanged(self):
        text = (ROOT / 'docs/ginei/amritsar.html').read_text()
        self.assertNotIn('data-tour-phase', text)
        self.assertNotIn('@@QUICK_TOUR', text)
if __name__ == '__main__': unittest.main()
