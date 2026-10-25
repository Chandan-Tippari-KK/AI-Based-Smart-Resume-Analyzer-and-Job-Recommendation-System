
import unittest

from skill_extractor import extract_skills
from nlp_skill_extractor import extract_skills_nlp


class TestSkillExtraction(unittest.TestCase):

    def test_java_is_not_detected_inside_javascript(self):
        text = "Frontend development using JavaScript."

        self.assertNotIn("Java", extract_skills(text))
        self.assertIn("JavaScript", extract_skills(text))

    def test_java_is_detected_when_present_separately(self):
        text = "Experience with Java and JavaScript."

        skills = extract_skills(text)

        self.assertIn("Java", skills)
        self.assertIn("JavaScript", skills)

    def test_matching_is_case_insensitive(self):
        text = "Experience with python and ANGULAR."

        skills = extract_skills(text)

        self.assertIn("Python", skills)
        self.assertIn("Angular", skills)

    def test_nlp_extractor_avoids_java_false_positive(self):
        text = "Experience with JavaScript and TypeScript."

        skills = extract_skills_nlp(text)

        self.assertNotIn("Java", skills)
        self.assertIn("JavaScript", skills)
        self.assertIn("TypeScript", skills)

    def test_empty_text_returns_empty_list(self):
        self.assertEqual(extract_skills(""), [])
        self.assertEqual(extract_skills_nlp(""), [])

    def test_non_string_input_returns_empty_list(self):
        self.assertEqual(extract_skills(None), [])
        self.assertEqual(extract_skills_nlp(None), [])


if __name__ == "__main__":
    unittest.main()
