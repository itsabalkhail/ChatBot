# 🤖 Arabic Voice Assistant

An interactive voice assistant that listens to your voice, understands your speech, and responds back audibly using AI from Cohere.

## ✨ Features

- 🎤 **Voice Recording**: Records your voice for 5 seconds
- 🧠 **Speech-to-Text**: Understands Arabic speech using Google Speech Recognition
- 🤖 **AI Intelligence**: Generates smart responses using Cohere AI
- 🔊 **Text-to-Speech**: Speaks back to you in Arabic using Google TTS
- 🔄 **Continuous Interaction**: Interactive loop until you say "خلاص" or "مع السلامة"

## 📦 Requirements

### Required Libraries

```bash
pip install sounddevice
pip install soundfile
pip install speechrecognition
pip install gtts
pip install playsound
pip install cohere
```

### Additional Requirements

- **Cohere API Key**: Get it from [dashboard.cohere.com](https://dashboard.cohere.com/api-keys)
- **Internet Connection**: Required for Google and Cohere services
- **Microphone**: For voice recording
- **Speakers**: To hear responses

## 🚀 Getting Started

### 1. Setup API Key

```python
co = cohere.Client("Your_API_Key_Here")
```

### 2. Run the Program

```bash
python voice_assistant.py
```

## 📝 How to Use

1. **Start the program** - You'll see "🎤 تكلم الآن..." (Speak now...)
2. **Speak for 5 seconds** - Say what you want
3. **Wait for processing** - It will understand and generate a response
4. **Listen to the reply** - The bot will speak back to you
5. **Repeat the process** - Or say "خلاص" (enough) to exit

### Example Questions

- "ما هو الطقس اليوم؟" (What's the weather today?)
- "اخبرني نكتة" (Tell me a joke)
- "ما هي عاصمة السعودية؟" (What's the capital of Saudi Arabia?)
- "خلاص" (Exit the program)

## ⚙️ Code Explanation

### Program Functions

#### `record_audio(filename, duration=5)`
- Records audio from microphone
- Default duration: 5 seconds
- Saves file in WAV format

#### `transcribe_audio(filename)`
- Converts recorded audio to text
- Uses Google Speech Recognition
- Supports Arabic language (ar-SA)

#### `get_reply(text)`
- Sends text to Cohere AI
- Gets intelligent response
- Handles errors gracefully

#### `speak(text)`
- Converts text to speech
- Uses Google Text-to-Speech
- Creates temporary file and plays it

## 🔧 Customizable Settings

### Change Recording Duration
```python
record_audio(duration=10)  # 10 seconds instead of 5
```

### Change Audio Quality
```python
fs = 48000  # Higher quality (default: 44100)
```

### Change Speech Recognition Language
```python
recognizer.recognize_google(audio, language="en-US")  # English
```

## ❗ Troubleshooting

### Common Issues and Solutions

#### Recording Error
```
❌ Issue: No module named 'sounddevice'
✅ Solution: pip install sounddevice
```

#### Speech Recognition Error
```
❌ Issue: "ما قدرت أفهم الكلام" (Couldn't understand speech)
✅ Solution: Speak more clearly, check microphone
```

#### Cohere Error
```
❌ Issue: "خطأ من Cohere" (Cohere error)
✅ Solution: Check API key, internet connection
```

#### Audio Playback Error
```
❌ Issue: playsound module issues
✅ Solution: Try alternative: pip install pygame
```

## 🛠️ Technical Details

### Audio Specifications
- **Sample Rate**: 44,100 Hz
- **Channels**: Mono (1 channel)
- **Format**: WAV
- **Bit Depth**: 16-bit

### API Services Used
- **Google Speech Recognition**: For speech-to-text
- **Cohere AI**: For intelligent responses
- **Google Text-to-Speech**: For text-to-speech

## 🔒 Security Notes

- Keep your Cohere API key secure
- Don't commit API keys to version control
- Consider using environment variables:

```python
import os
co = cohere.Client(os.getenv("COHERE_API_KEY"))
```

## 🚀 Enhancements Ideas

### Possible Improvements
- Add wake word detection
- Support multiple languages
- Save conversation history
- Add voice commands for settings
- Implement offline mode
- Add emotion detection in voice

### Performance Optimization
- Cache TTS responses
- Reduce API calls
- Optimize audio processing
- Add silence detection

## 🔄 Version History

- **v1.0**: Basic voice assistant functionality
- **v1.1**: Added error handling
- **v1.2**: Improved Arabic language support

