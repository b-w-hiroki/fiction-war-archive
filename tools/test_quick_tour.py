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
    def test_cards_group_labels_and_descriptions(self):
        text = (ROOT / 'docs/ginei/astarte.html').read_text()
        for phase in (0, 2, 6):
            self.assertIn(f'aria-labelledby="tour-label-{phase}"', text)
            self.assertIn(f'aria-describedby="tour-why-{phase}"', text)
            self.assertIn(f'id="tour-why-{phase}"', text)
        self.assertEqual(text.count('class="quick-tour-card"'), 3)
        self.assertIn('.quick-tour-card:focus-visible', text)
    def test_visual_hierarchy_retains_story_and_accessibility(self):
        text = (ROOT / 'docs/ginei/astarte.html').read_text()
        self.assertEqual(text.count('class="quick-tour-stage"'), 3)
        for stage in ('1. 開始配置', '2. 転機', '3. 結果'):
            self.assertIn(stage + '</span>', text)
        self.assertIn('prefers-reduced-motion', text)
        self.assertIn('forced-colors:active', text)
        self.assertIn('aria-describedby="tour-why-2"', text)
    def test_other_battle_unchanged(self):
        text = (ROOT / 'docs/ginei/amritsar.html').read_text()
        self.assertNotIn('data-tour-phase', text)
        self.assertNotIn('@@QUICK_TOUR', text)
if __name__ == '__main__': unittest.main()
