import speech_recognition as sr
import openai
import pyttsx3

# Cài đặt API key của bạn từ OpenAI
openai.api_key = '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'

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hãy nói gì đó:")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='vi')
        return text
    except sr.UnknownValueError:
        print("Không thể nhận dạng giọng nói.")
    except sr.RequestError as e:
        print("Lỗi trong quá trình nhận dạng giọng nói; {0}".format(e))

def text_to_speech(text, lang='vi'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Tốc độ giọng nói (default: 200)
    engine.setProperty('volume', 1)  # Âm lượng giọng nói (default: 1)
    engine.setProperty('voice', 'vi')  # Chọn giọng nói tiếng Việt
    engine.say(text)
    engine.runAndWait()

# GPT-3.5 viết lại lời nói
def gpt_rewrite(input_text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=input_text,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Chương trình chính
while True:
    user_input = speech_to_text()
    if user_input:
        if "kết thúc chương trình" in user_input.lower() or "đóng chương trình" in user_input.lower():
            print("Trợ lí: Tạm biệt!")
            text_to_speech("Tạm biệt!")
            break
        else:
            response = gpt_rewrite(user_input)
            print("Trợ lí:", response)
            text_to_speech(response)
    else:
        print("Vui lòng thử lại.")
