// frontend/App.js

import React, { useState } from 'react';
import { View, Button, Image, Text } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

export default function App() {
  const [image, setImage] = useState(null);
  const [analysis, setAnalysis] = useState(null);

  const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      quality: 1,
    });

    if (!result.cancelled) {
      setImage(result.uri);
      uploadImage(result.uri);
    }
  };

  const uploadImage = async (uri) => {
    let formData = new FormData();
    formData.append('image', {
      uri,
      name: 'photo.jpg',
      type: 'image/jpeg',
    });

    try {
      let response = await fetch('http://localhost:5000/ocr', {
        method: 'POST',
        body: formData,
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      let json = await response.json();
      setAnalysis(json);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <View>
      <Button title="Pick an image from camera roll" onPress={pickImage} />
      {image && <Image source={{ uri: image }} style={{ width: 200, height: 200 }} />}
      {analysis && (
        <View>
          <Text>OCR Output: {analysis.ocr_text}</Text>
          <Text>Recommended Action: {analysis.recommendation}</Text>
        </View>
      )}
    </View>
  );
}