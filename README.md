# FastAPI TTS Indonesia (Wanita) Backend

## Cara Jalankan Lokal

1. Install requirements:
   ```sh
   pip install -r requirements.txt
   ```
2. Jalankan server:
   ```sh
   uvicorn app:app --reload
   ```
3. Endpoint TTS:
   - POST `/tts` (form field: `text`)
   - Response: file MP3 suara wanita Indonesia

## Cara Deploy ke Railway

1. Upload folder ini ke GitHub.
2. Di Railway, buat project baru dari repo GitHub ini.
3. Set deploy command:
   ```
   uvicorn app:app --host 0.0.0.0 --port $PORT
   ```
4. Tunggu deploy selesai, dapatkan URL public.

## Contoh Request dari Flutter

```dart
import 'package:http/http.dart' as http;
import 'package:audioplayers/audioplayers.dart';
import 'dart:io';

Future<void> speakWithTTS(String text) async {
  final url = Uri.parse('https://your-app.up.railway.app/tts');
  final request = http.MultipartRequest('POST', url)
    ..fields['text'] = text;
  final response = await request.send();

  if (response.statusCode == 200) {
    final bytes = await response.stream.toBytes();
    final tempDir = Directory.systemTemp;
    final file = await File('${tempDir.path}/tts.mp3').writeAsBytes(bytes);
    final player = AudioPlayer();
    await player.play(DeviceFileSource(file.path));
  } else {
    print('TTS error: ${response.statusCode}');
  }
}
``` 