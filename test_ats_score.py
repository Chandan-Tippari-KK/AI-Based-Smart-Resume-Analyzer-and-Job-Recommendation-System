
import unittest
from pathlib import Path

from resume_parser import extract_text_from_pdf
from nlp_skill_extractor import extract_skills_nlp
from ats_score import calculate_ats_score


# Locate the sample PDF relative to this test file.
PROJECT_DIR = Path(__file__).resolve().parent
SAMPLE_RESUME = PROJECT_DIR / "sample_resume.pdf"


class TestATSScore(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Load and process the sample resume once for this test class."""
        if not SAMPLE_RESUME.is_file():
            raise FileNotFoundError(
                f"Sample resume not found: {SAMPLE_RESUME}"
            )

        cls.resume_text = extract_text_from_pdf(str(SAMPLE_RESUME))
        cls.skills = extract_skills_nlp(cls.resume_text)
        cls.result = calculate_ats_score(
            cls.resume_text,
            cls.skills
        )

    def test_resume_text_is_extracted(self):
        self.assertIsInstance(self.resume_text, str)
        self.assertTrue(self.resume_text.strip())

    def test_ats_result_contains_expected_keys(self):
        self.assertIn("ATS Score", self.result)
        self.assertIn("Missing", self.result)

    def test_ats_score_is_within_valid_range(self):
        score = self.result["ATS Score"]

        self.assertIsInstance(score, (int, float))
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)

    def test_missing_sections_is_a_list(self):
        self.assertIsInstance(self.result["Missing"], list)


if __name__ == "__main__":
    unittest.main()
