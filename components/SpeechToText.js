import React, { useState } from 'react';
import { View, Text, Button } from 'react-native';
import Voice from 'react-native-voice';

const SpeechToText = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [text, setText] = useState('');

  const startRecording = async () => {
    setIsRecording(true);
    try {
      await Voice.start('en-US');
    } catch (error) {
      console.log(error);
    }
  };

  const stopRecording = async () => {
    setIsRecording(false);
    try {
      await Voice.stop();
    } catch (error) {
      console.log(error);
    }
  };

  const onSpeechResults = (event) => {
    setText(event.value[0]);
    console.log('Speech recognition result: ', event.value);
  };

  Voice.onSpeechResults = onSpeechResults;

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text style={{ marginBottom: 20  , color : 'black'}}>{text}</Text>
      <Button title={isRecording ? 'Stop recording' : 'Start recording'} onPress={isRecording ? stopRecording : startRecording} />
    </View>
  );
};

export default SpeechToText;
