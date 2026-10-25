
import unittest

from job_recommender import recommend_jobs, JOB_DATABASE


class TestJobRecommender(unittest.TestCase):

    def test_all_required_skills_produce_full_match(self):
        skills = JOB_DATABASE["Backend Developer"]

        results = recommend_jobs(skills)

        backend = next(
            item for item in results
            if item["job"] == "Backend Developer"
        )

        self.assertEqual(backend["match_percentage"], 100.0)
        self.assertEqual(backend["missing_skills"], [])

    def test_no_matching_skills_produce_zero_match(self):
        results = recommend_jobs(["UnrelatedSkill"])

        self.assertTrue(
            all(
                item["match_percentage"] == 0.0
                for item in results
            )
        )

    def test_partial_match_is_calculated_correctly(self):
        results = recommend_jobs(["C#", "SQL"])

        backend = next(
            item for item in results
            if item["job"] == "Backend Developer"
        )

        # 2 matched skills out of 5 required skills = 40%
        self.assertEqual(backend["match_percentage"], 40.0)

        self.assertEqual(
            backend["missing_skills"],
            ["ASP.NET Core", "SQL Server", "REST API"]
        )

    def test_skill_matching_is_case_insensitive(self):
        results = recommend_jobs(["c#", "asp.net core", "sql"])

        backend = next(
            item for item in results
            if item["job"] == "Backend Developer"
        )

        # 3 matched skills out of 5 required skills = 60%
        self.assertEqual(backend["match_percentage"], 60.0)

    def test_results_are_sorted_by_match_percentage(self):
        results = recommend_jobs(
            ["C#", "ASP.NET Core", "SQL"]
        )

        scores = [
            item["match_percentage"]
            for item in results
        ]

        self.assertEqual(
            scores,
            sorted(scores, reverse=True)
        )


if __name__ == "__main__":
    unittest.main()
