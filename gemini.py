import os
from google import genai

from settings import GEMINI_API_KEY

client = genai.Client( api_key=GEMINI_API_KEY )


def handle_file_attachment(file_path):
  if file_path and os.path.exists(file_path):
    with open(file_path, 'rb') as file:
      file_content = file.read()
    return file_content
  return None



def ask_gemini(prompt, file_path=None, history = [], mime_type=None):
    """
    Ask Gemini a question and return the response.
    :param prompt: The question to ask.
    :param file_path: Optional file path to send to Gemini.
    :param history: Optional chat history.
    :return: The response from Gemini.
    """

    file_content = handle_file_attachment(file_path)

    response = client.models.generate_content(
      model='gemini-2.0-flash',
      
      config=genai.types.GenerateContentConfig(
        system_instruction="You are an AI assistant integrated into a Telegram bot. Your purpose is to provide helpful, accurate, and contextually relevant responses to user queries.",
        max_output_tokens=500,
        temperature=0.2
      ),

      contents=[
        genai.types.Part.from_bytes(
          data=file_content,
          mime_type=mime_type,
        ),
        prompt
      ] if file_content else [
        prompt
      ],
    )

    history.extend([
        { "role": "user", "parts": [file_path if file_content else '', prompt] },
        { "role": "model", "parts": [response.text] }
    ])

    return response.text
