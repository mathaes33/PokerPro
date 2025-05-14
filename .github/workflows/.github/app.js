import React, { useState } from 'react';
import { Button, Image, View, Platform, Text } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import axios from 'axios';

export default function App() {
  const [image, setImage] = useState(null);
  const [parsed, setParsed] = useState(null);

  const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      base64: false,
      quality: 1,
    });

    if (!result.cancelled) {
      setImage(result.uri);
      uploadImage(result);
    }
  };

  const uploadImage = async (result) => {
    let localUri = result.uri;
    let filename = localUri.split('/').pop();

    let match = /\.(\w+)$/.exec(filename);
    let type = match ? `image/${match[1]}` : `image`;

    let formData = new FormData();
    formData.append('image', {
      uri: localUri,
      name: filename,
      type,
    });

    const res = await axios.post('http://<YOUR-IP>:5000/ocr', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    setParsed(res.data);
  };

  return (
    <View style={{ marginTop: 50, padding: 20 }}>
      <Button title="Pick an image" onPress={pickImage} />
      {image && <Image source={{ uri: image }} style={{ width: 300, height: 300 }} />}
      {parsed && (
        <View>
          <Text style={{ marginTop: 20 }}>Raw Text:</Text>
          <Text>{parsed.raw_text}</Text>
          <Text style={{ marginTop: 20 }}>Parsed:</Text>
          <Text>{JSON.stringify(parsed.parsed)}</Text>
        </View>
      )}
    </View>
  );
}