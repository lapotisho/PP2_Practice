import json
import os

class PersistenceManager:
    def __init__(self):
        self.leaderboard_file = "leaderboard.json"
        self.settings_file = "settings.json"
        self._ensure_files_exist()

    def _ensure_files_exist(self):
        """Creates the files with default data if they don't exist."""
        if not os.path.exists(self.leaderboard_file):
            with open(self.leaderboard_file, 'w') as f:
                json.dump([], f) # Empty list for scores

        if not os.path.exists(self.settings_file):
            default_settings = {
                "sound_on": True,
                "car_color": "RED",
                "difficulty": "Medium"
            }
            with open(self.settings_file, 'w') as f:
                json.dump(default_settings, f)

    # --- LEADERBOARD LOGIC ---
    def save_high_score(self, name, score, distance):
        scores = self.get_scores()
        scores.append({"name": name, "score": score, "distance": round(distance, 2)})
        
        # Sort by score (highest first) and keep top 10
        scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:10]
        
        with open(self.leaderboard_file, 'w') as f:
            json.dump(scores, f, indent=4)

    def get_scores(self):
        with open(self.leaderboard_file, 'r') as f:
            return json.load(f)

    # --- SETTINGS LOGIC ---
    def save_settings(self, settings_dict):
        with open(self.settings_file, 'w') as f:
            json.dump(settings_dict, f, indent=4)

    def load_settings(self):
        with open(self.settings_file, 'r') as f:
            return json.load(f)