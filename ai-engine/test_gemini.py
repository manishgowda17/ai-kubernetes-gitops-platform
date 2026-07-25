from services.gemini_service import GeminiService

ai = GeminiService()

response = ai.generate_response(
    """
    Explain Kubernetes Deployment in 5 simple points.
    """
)

print(response)
