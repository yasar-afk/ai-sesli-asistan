# 🤖 Kişisel Yapay Zeka Asistanı

**Yerelde çalışan, tamamen ücretsiz ve offline sesli AI asistan!**

Ollama + Whisper + Coqui TTS ile güçlendirilmiş, Türkçe konuşan kişisel asistanınız.

## ✨ Özellikler

- 🎤 **Gelişmiş Ses Tanıma** - Whisper ile optimize edilmiş Türkçe ses tanıma
- 🗣️ **Doğal Sesli Yanıt** - Coqui TTS ile gerçekçi Türkçe konuşma
- 🧠 **Gerçek AI Zekası** - Ollama ile yerelde çalışan LLM (Llama 3.2)
- 💬 **Konuşma Hafızası** - Önceki konuşmaları hatırlar
- 🌐 **Network Desteği** - Evdeki diğer cihazlardan erişim
- 🔒 **Tamamen Offline** - İnternet bağlantısı gereksiz
- ⚡ **Hızlı ve Ücretsiz** - Bilgisayarınızda çalışır

## 🚀 Hızlı Başlangıç

### 1. Ollama'yı Kurun

**ÖNCE BUNU YAPIN!** Detaylı talimatlar için: [OLLAMA_KURULUM.md](OLLAMA_KURULUM.md)

```powershell
# Ollama'yı indirin: https://ollama.ai/download
# Kurulumdan sonra:
ollama pull llama3.2:3b
```
### 2. Sanal Ortamı Kurun

```powershell
cd c:\Users\52tuz\Desktop\ai_assistan
.\setup_ai_ses.bat
```

### 3. Asistanı Başlatın

```powershell
# Sanal ortamı aktif edin
.\ai_ses\Scripts\activate

# Programı çalıştırın
python main.py
```

## 📖 Kullanım

1. Program başladığında Enter'a basın
2. 5 saniye içinde konuşun
3. AI size yanıt verecek
4. Çıkmak için "çık", "dur" veya "kapat" deyin

### Özel Komutlar

- **"geçmişi temizle"** - Konuşma hafızasını siler
- **"saat kaç"** - Güncel saati söyler
- **"bugün hangi gün"** - Tarihi söyler

### Model Seçimi

```powershell
# Daha hızlı ses tanıma (daha az doğru)
python main.py small llama3.2:3b

# Daha iyi ses tanıma (önerilen)
python main.py medium llama3.2:3b

# Daha akıllı AI (daha yavaş)
python main.py medium llama3.2:7b
```

## 🌐 Evdeki Diğer Cihazlardan Erişim

Detaylı talimatlar için [OLLAMA_KURULUM.md](OLLAMA_KURULUM.md) dosyasının 6. bölümüne bakın.

**Kısaca:**
1. Ollama'yı network'te paylaşın
2. IP adresinizi öğrenin (`ipconfig`)
3. Diğer cihazlardan `http://[IP]:11434` ile erişin

## 🔧 Sorun Giderme

### Ollama Bağlantı Hatası
```powershell
# Ollama servisini başlatın
ollama serve
```

### Ses Tanıma Çok Yavaş
- Daha küçük Whisper modeli kullanın: `python main.py small`
- GPU desteğini kontrol edin

### AI Yanıt Vermiyor
- Ollama'nın çalıştığını kontrol edin: `ollama list`
- Modelin indirildiğini kontrol edin: `ollama pull llama3.2:3b`

## 📁 Proje Yapısı

```
ai_assistan/
├── main.py                    # Ana program
├── modules/
│   ├── voice_input.py        # Ses tanıma (Whisper)
│   ├── voice_output.py       # Ses sentezi (Coqui TTS)
│   └── ai_brain.py           # AI mantığı (Ollama)
├── OLLAMA_KURULUM.md         # Detaylı kurulum rehberi
└── README.md                 # Bu dosya
```

## 🎯 Sistem Gereksinimleri

**Minimum:**
- Windows 10/11
- 8 GB RAM
- 10 GB boş disk alanı
- Mikrofon ve hoparlör

**Önerilen:**
- 16 GB RAM
- NVIDIA GPU (opsiyonel, hızlandırır)
- İyi kaliteli mikrofon

## 📝 Lisans

Bu proje kişisel kullanım içindir. Kullanılan kütüphaneler kendi lisanslarına tabidir.

## 🤝 Katkıda Bulunma

Bu proje kişisel bir projedir. Önerilerinizi issue olarak açabilirsiniz.

---

**Not:** Bu sistem tamamen yerelde çalışır ve hiçbir veri internete gönderilmez. 🔒