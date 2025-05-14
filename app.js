import React, { useState } from 'react';
import { View, Button, Image, Text } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

export default function App() {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState(null);

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