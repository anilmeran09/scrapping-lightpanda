
# from openai import OpenAI
# from app.config.settings import settings


# client = OpenAI(
#     api_key=settings.GROQ_API_KEY,
#     base_url=settings.GROQ_BASE_URL,
# )


# def ask_llm(prompt: str) -> str:

#     response = client.chat.completions.create(
#         model=settings.GROQ_MODEL,
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt,
#             }
#         ],
#         temperature=0,
#     )

#     return response.choices[0].message.content



from openai import OpenAI
from app.config.settings import settings


client = OpenAI(
    api_key=settings.GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def ask_llm(prompt: str) -> str:

    response = client.chat.completions.create(
        model=settings.GEMINI_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
    )

    return response.choices[0].message.content
