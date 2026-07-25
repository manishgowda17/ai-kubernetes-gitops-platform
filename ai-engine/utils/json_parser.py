import json
import re


class JSONParser:

    @staticmethod
    def parse(response: str):

        # Remove markdown code fences
        response = re.sub(r"```json", "", response)
        response = re.sub(r"```", "", response)

        response = response.strip()

        try:
            return json.loads(response)

        except json.JSONDecodeError:

            return {
                "status": "error",
                "raw_response": response
            }
