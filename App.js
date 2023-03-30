import React , { useState }  from 'react';
import {StyleSheet, Text,TextInput, View ,StatusBar ,Button} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import Map from './components/Map';



const Stack = createNativeStackNavigator();


const YourApp = () => {

  return (

    <NavigationContainer>
    <Stack.Navigator>
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{ title: 'Home' }}
        />
        
        <Stack.Screen
          name="Map"
          component={Map}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}



const HomeScreen = ({ navigation }) => {
  const [text, setText] = useState('');
  return (
    <>
    <Button
      title="Go to Map"
      onPress={() =>
        navigation.navigate('Map')
      }
    />
    


    <View style={styles.container}>
    <Text style = {styles.text}>
        Try going to Map! 🎉   
      </Text>

      </View>
    </>
  );
};


const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: StatusBar.currentHeight,
    alignItems: 'center',
    justifyContent: 'center',
    textAlign: 'center',
    textcolor: 'black',
  },
  scrollView: {
    backgroundColor: 'pink',
    marginHorizontal: 20,
    flex:1,
  },
  text: {
    color: 'black',
  }
});

export default YourApp;