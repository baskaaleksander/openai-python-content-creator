import elevenlabs

elevenlabs.set_api_key(ELEVENLABSAPIKEY)

def generate_voice_over(script):
    voice = elevenlabs.Voice(
        voice_id = "ErXwobaYiN019PkySvjV",
        settings= elevenlabs.VoiceSettings(
            stability=0.5,
            similarity_boost=0.75
        )
    )

    voice_over = elevenlabs.generate(
        text=script, 
        voice=voice)
    elevenlabs.save(voice_over, "voice_over.mp3")