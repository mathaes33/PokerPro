import React, { useState } from 'react';
import { View, Button, Image, Text } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

export default function App() {
  const [image, setImage] = try {
  setLoading(true);
  setError(null);
  const res = await axios.post('http://192.168.1.29:5000/ocr', { image: base64Img });
  setOcrResult(res.data.parsed_text);
  setGameState(res.data.game_state);
} catch (err) {
  console.error(err);
  setError('Failed to process image');
} finally {
  setLoading(false);
}

  const pickImage = async () => {
    const res = await ImagePicker.launchImageLibraryAsync({ base64: true });
    if (!res.cancelled) {
      setImage(res.uri);
      const formData = new FormData();
      formData.append('image', {
        uri: res.uri,
        name: 'photo.jpg',
        type: 'image/jpeg',
      });
      const response = await fetch('http://YOUR_FLASK_API/ocr', {
        method: 'POST',
        body: formData,
      });
      const json = await response.json();
      setResult(json);
    }
  };

  return (
    <View style={{ padding: 20 }}>
      <Button title="Upload Poker Image" onPress={pickImage} />
      {image && <Image source={{ uri: image }} style={{ width: 300, height: 300 }} />}
      {result && <Text>{JSON.stringify(result, null, 2)}</Text>}
    </View>
  );
}