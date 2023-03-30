import React, {useState, useRef, useEffect} from 'react';
import {Text, Button, PermissionsAndroid, StyleSheet} from 'react-native';
import MapView, {PROVIDER_GOOGLE, Marker} from 'react-native-maps';

import Geolocation from '@react-native-community/geolocation';

function Map() {
  {
    const mapRef = useRef(null);

    const [location, setLocation] = useState({
      latitude: 0,
      longitude: 0,
      latitudeDelta: 0.0922,
      longitudeDelta: 0.0421,
    });

    const [errorr, setError] = useState('');
    var watchID = useRef(null);

    const goToTokyo = () => {
      mapRef.current.animateToRegion(location, 3 * 1000);
    };

    useEffect(() => {
      const requestLocationPermission = async () => {
        if (Platform.OS === 'ios') {
          getOneTimeLocation();
        } else {
          try {
            const granted = await PermissionsAndroid.request(
              PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
              {
                title: 'Location Access Required',
                message: 'This App needs to Access your location',
              },
            );
            if (granted === PermissionsAndroid.RESULTS.GRANTED) {
              await getOneTimeLocation();
            } else {
              console.log('Permission Denied');
            }
          } catch (err) {
            console.warn(err);
          }
        }
      };
      requestLocationPermission();
      return () => {
        Geolocation.clearWatch(watchID);
      };
    }, []);

    const getOneTimeLocation = async () => {
      Geolocation.getCurrentPosition(
        pos => {
          let latitude = pos.coords.latitude;
          let longitude = pos.coords.longitude;
          let latitudeDelta = 0.092;
          let longitudeDelta = 0.0421;
          setLocation({latitude, longitude, latitudeDelta, longitudeDelta});
          // console.log(location);
          goToTokyo;
        },
        err => {
          console.warn(err.message);
          setError(err.message);
        },
        {enableHighAccuracy: false, timeout: 5000},
      );
    };

    if (errorr) {
      return <Text style={styles.text}>{errorr}</Text>;
    }
    
    return (  
      <>
        <MapView
          style={{flex: 1}}
          initialRegion={{
            latitude: 19.076,
            longitude: 72.8777,
            latitudeDelta: 0.0922,
            longitudeDelta: 0.0421,
          }}
          provider={PROVIDER_GOOGLE}
          ref={mapRef}
          // onRegionChangeComplete={(region) => setRegion(region)}
        >
          <Marker
            key="1"
            coordinate={{
              latitude: location.latitude,
              longitude: location.longitude,
            }}></Marker>
        </MapView>
        <Button onPress={() => goToTokyo()} title="Go to My location" />

        {/* <Button onPress={() => getOneTimeLocation()} title=" My location" /> */}
        <Text style={styles.text}>Current latitude: {location.latitude}</Text>
        <Text style={styles.text}>Current longitude: {location.longitude}</Text>
      </>
    );
  }
}

const styles = StyleSheet.create({
  map: {
    height: 400,
    marginTop: 80,
  },
  text: {
    color: 'black',
  },
});

export default Map;
