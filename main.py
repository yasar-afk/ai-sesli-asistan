"""
Kişisel Yapay Zeka Asistanı - Ana Uygulama
Ollama ile yerelde çalışan AI + Sesli komut sistemi
"""
import sys
import os

# Modülleri import et
try:
    from modules.voice_input import VoiceInput
    from modules.voice_output import VoiceOutput
    from modules.ai_brain_groq import AIBrain
except ImportError as e:
    print(f"❌ Modül import hatası: {e}")
    print("💡 Lütfen gerekli kütüphaneleri yüklediğinizden emin olun.")
    print("   ai_ses ortamını aktif edip: pip install -r ai_ses_requirements.txt")
    print("   Ayrıca Ollama'nın kurulu olduğundan emin olun!")
    sys.exit(1)

class VoiceAssistant:
    def __init__(self, whisper_model="medium", groq_model="llama-3.3-70b-versatile"):
        """
        Sesli asistan başlatır
        
        Args:
            whisper_model: Whisper model boyutu (tiny, base, small, medium, large)
            groq_model: Groq AI modeli (llama-3.3-70b-versatile, llama-3.1-70b-versatile, mixtral-8x7b-32768)
        """
        print("=" * 50)
        print("🤖 KİŞİSEL YAPAY ZEKA ASİSTANI BAŞLATILIYOR...")
        print("=" * 50)
        
        # Modülleri başlat
        print("\n📌 Modüller yükleniyor...")
        try:
            self.voice_input = VoiceInput(model_size=whisper_model, language="tr")
            self.voice_output = VoiceOutput()
            self.ai_brain = AIBrain(model=groq_model)
            print("✅ Tüm modüller başarıyla yüklendi!\n")
        except Exception as e:
            print(f"❌ Modül yükleme hatası: {e}")
            sys.exit(1)
        
        self.running = False
    
    def start(self):
        """Asistanı başlatır ve sürekli dinleme moduna geçer"""
        self.running = True
        
        # Karşılama mesajı
        welcome_msg = "Merhaba! Ben sizin kişisel yapay zeka asistanınızım. Size nasıl yardımcı olabilirim?"
        print(f"🤖: {welcome_msg}")
        self.voice_output.text_to_speech(welcome_msg)
        
        print(f"\n💡 AI Model: {self.ai_brain.model}")
        print(f"💡 Ses Tanıma: Whisper {self.voice_input.model.__class__.__name__}")
        
        print("\n" + "=" * 50)
        print("🎤 DİNLEME MODU AKTİF")
        print("=" * 50)
        print("💡 Her turda Enter'a basarak konuşun")
        print("💡 Çıkmak için 'çık', 'dur' veya 'kapat' deyin")
        print("=" * 50 + "\n")
        
        try:
            while self.running:
                self.listen_and_respond()
        
        except KeyboardInterrupt:
            self.stop()
    
    def listen_and_respond(self):
        """Bir kez dinler ve yanıt verir"""
        try:
            # Kullanıcıdan ses al
            print("\n🎤 Konuşmaya hazır olunca Enter'a basın...")
            input()
            
            print("🔴 DİNLİYORUM... (5 saniye)")
            user_text = self.voice_input.listen_and_transcribe(duration=5, save_recording=True)
            
            if not user_text or user_text.strip() == "":
                print("⚠️  Ses algılanamadı, lütfen tekrar deneyin.\n")
                return
            
            print(f"👤 Siz: {user_text}")
            
            # Çıkış komutu kontrolü
            if any(word in user_text.lower() for word in ['çık', 'dur', 'kapat', 'görüşürüz', 'bye']):
                self.stop()
                return
            
            # Özel komutlar
            if 'geçmişi temizle' in user_text.lower() or 'hafızayı sil' in user_text.lower():
                self.ai_brain.reset_conversation()
                response = "Tamam, konuşma geçmişini sildim. Yeni bir konuşma başlayalım!"
            else:
                # AI Brain ile yanıt üret
                print("🧠 Düşünüyorum...")
                response = self.ai_brain.think(user_text, use_history=True)
            
            print(f"🤖 Asistan: {response}")
            
            # Sesli yanıt ver
            self.voice_output.text_to_speech(response)
        
        except Exception as e:
            print(f"❌ Hata oluştu: {e}")
            print("⚠️  Devam ediliyor...\n")
    
    def stop(self):
        """Asistanı durdurur"""
        self.running = False
        goodbye_msg = "Görüşürüz! İyi günler dilerim."
        print(f"\n🤖: {goodbye_msg}")
        self.voice_output.text_to_speech(goodbye_msg)
        print("\n" + "=" * 50)
        print("👋 ASİSTAN SONLANDIRILDI")
        print("=" * 50)
        sys.exit(0)


def main():
    """Ana fonksiyon"""
    # Komut satırı argümanları
    whisper_model = "medium"  # Varsayılan (daha iyi tanıma için)
    groq_model = "llama-3.3-70b-versatile"  # Varsayılan (en güçlü aktif model - 70B)
    
    if len(sys.argv) > 1:
        whisper_model = sys.argv[1]
    if len(sys.argv) > 2:
        groq_model = sys.argv[2]
    
    print("\n💡 Kullanım: python main.py [whisper_model] [groq_model]")
    print(f"   Örnek: python main.py medium llama-3.3-70b-versatile\n")
    
    # Asistanı başlat
    assistant = VoiceAssistant(whisper_model=whisper_model, groq_model=groq_model)
    assistant.start()


if __name__ == "__main__":
    main()
